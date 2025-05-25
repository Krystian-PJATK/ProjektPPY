import Film
from Film import all_films
from datetime import date

class User:
    #todo nickname must be unique. Check file
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password

    def getFilms(self, status):
        class FilmWithDate:
            def __init__(self, film, date,state):
                self.film = film
                self.date = date
                self.state = state

            def __str__(self):
                return self.film.user_friendly_str()+"\n"+self.state+": "+ self.date

        finalfilms = []

        with open('Data/Users.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if self.nickname in line:
                    userParts = line.split(";")
                    if len(userParts) < 3:
                        print("user does not have any saved films")
                        return []

                    userfilms = {}
                    filmpairs = userParts[2].split(',')
                    for pair in filmpairs:
                        film_id, flag, time = pair.split(":")
                        userfilms[film_id] = (flag, time)

                    with open('Data/Films.txt', 'r') as filmfile:
                        for film_line in filmfile:
                            film_line = film_line.strip()
                            filmData = film_line.split(";")
                            film_id = filmData[0]
                            if film_id in userfilms:
                                flag, date = userfilms[film_id]
                                flag = flag.lower()

                                if status == "watched" and flag == "true":
                                    film = Film.Film(int(filmData[0]), filmData[1], filmData[2], filmData[3],
                                                     filmData[4])
                                    finalfilms.append(FilmWithDate(film, date,"watched at"))

                                elif status == "notwatched" and flag == "false":
                                    film = Film.Film(int(filmData[0]), filmData[1], filmData[2], filmData[3],
                                                     filmData[4])
                                    finalfilms.append(FilmWithDate(film, date,"added at"))

                                elif status == "all":
                                    if flag == "true":
                                        film = Film.Film(int(filmData[0]), filmData[1], filmData[2], filmData[3],
                                                         filmData[4])
                                        finalfilms.append(FilmWithDate(film, date,"watched at"))
                                    elif flag == "false":
                                        film = Film.Film(int(filmData[0]), filmData[1], filmData[2], filmData[3],
                                                         filmData[4])
                                        finalfilms.append(FilmWithDate(film, date, "added at"))
                    return finalfilms

        return finalfilms

    def watch(self, filmId):
        idFoundInListOfFilms = False

        userFilms = self.getFilms("all")
        for film in userFilms:
            if str(film.film.ID) == str(filmId):
                idFoundInListOfFilms = True
                break
        found = False
        if idFoundInListOfFilms:
            with open('Data/Users.txt', 'r') as file:
                lines = file.readlines()
            with open('Data/Users.txt', 'w') as file:
                for line in lines:
                    line = line.strip()
                    parts = line.split(";")
                    nickname, password, film_data = parts[0], parts[1], parts[2]
                    if password == self.password:
                        film_line = film_data.split(",")
                        newFilm_line = []
                        for film in film_line:
                            film_id, status, time = film.split(":")
                            if film_id == filmId and status == "false":
                                newFilm_line.append(f"{film_id}:true:"+str(date.today()))
                                found = True
                            else:
                                newFilm_line.append(film)
                        new_line = f"{nickname};{password};{','.join(newFilm_line)}"
                        file.write(new_line + "\n")
                    else:
                        file.write(line + "\n")
                if found:
                    print(f"Film with id: {filmId} successfully watched")
                else:
                    print(f"Film with id: {filmId} was already watched")
        else:
            print("user does not have that film saved")

    def addToMyWatchlist(self,filmId):
        userFilms = self.getFilms("all")
        idFoundInListOfFilms = False
        for film in userFilms:
            if str(film.film.ID) == str(filmId):
                idFoundInListOfFilms = True
                break
        if idFoundInListOfFilms:
            print("You already have that film")
        else:
            idFoundInSystemListOfFilms = False
            systemFilms = all_films()
            for film in systemFilms:
                if str(film.ID) == str(filmId):
                    idFoundInSystemListOfFilms = True
                    break
            if idFoundInSystemListOfFilms:
                with open('Data/Users.txt', 'r') as file:
                    lines = file.readlines()
                with open('Data/Users.txt', 'w') as file:
                    for line in lines:
                        line = line.strip()
                        parts = line.split(";")
                        nickname, password, film_data = parts[0], parts[1], parts[2]
                        if password == self.password:
                            film_line = film_data.split(",")
                            film_line.append(f"{filmId}:false:"+str(date.today()))
                            new_line = f"{nickname};{password};{','.join(film_line)}"
                            file.write(new_line + "\n")
                        else:
                            file.write(line + "\n")
            else:
                print("film not found")

    def deleteFilmFromMyWatchlist(self,filmId):
        idFoundInListOfFilms = False

        userFilms = self.getFilms("all")
        for film in userFilms:
            if str(film.ID) == str(filmId):
                idFoundInListOfFilms = True
                break
        found = False
        if idFoundInListOfFilms:
            with open('Data/Users.txt', 'r') as file:
                lines = file.readlines()
            with open('Data/Users.txt', 'w') as file:
                for line in lines:
                    line = line.strip()
                    parts = line.split(";")
                    nickname, password, film_data = parts[0], parts[1], parts[2]
                    if password == self.password:
                        film_line = film_data.split(",")
                        newFilm_line = []
                        for film in film_line:
                            film_id, status = film.split(":")
                            if film_id == filmId:
                                found = True
                                print("Film successfully deleted from your watchlist")
                            else:
                                newFilm_line.append(film)

                        new_line = f"{nickname};{password};{','.join(newFilm_line)}"
                        file.write(new_line + "\n")
                    else:
                        file.write(line + "\n")
        else:
            print("user does not have that film saved")

    def search(self,userinput):
        userinput = userinput.lower().strip()
        with open('Data/Films.txt', 'r') as file:
            found = False
            for line in file:
                line = line.strip()
                film_parts = line.split(";")
                if len(film_parts) < 3:
                    continue

                title = film_parts[1].lower().strip()
                director = film_parts[2].lower().strip()

                if userinput in title or userinput in director:
                    print(film_parts)
                    found = True

            if not found:
                print("Nie znaleziono żadnego filmu z podaną frazą.")

    def export_films(self) -> bool:
        watched_films = self.getFilms('watched')
        notwatched_films = self.getFilms('notwatched')

        lines = "Your watch list\n"
        lines += "Films you watched\n"
        for film in watched_films:
            lines += film.film.user_friendly_str()+'\n'

        lines += "Films you want to watch\n"
        for film in notwatched_films:
            lines += film.film.user_friendly_str()+'\n'

        try:
            file = open('ExportedWatchlist.txt', 'w')
            file.write(lines)
            file.close()
            return True
        except Exception:
            return False

    def rateFilm(self, filmId, rating, comment):
            checkIfAlreadyRated = False

            #kokatenacja tekstu, który sprawdzamy, czy istnieje w pliku, czyli patrzymy czy osoba o danym nicku dodała już opinię na dany film
            searchingText = f"{self.nickname};{str(filmId)}"
            try:
                with open("Data/Ratings.txt",'r') as file:
                    for line in file:
                        if searchingText in line:
                            checkIfAlreadyRated = True
            except FileNotFoundError:
                print("Raitngs.txt not found")
            if checkIfAlreadyRated:
                print("cannot rate same film more than once")
            else:

                with open('Data/Users.txt', 'r') as lines:
                    for line in lines:
                        line = line.strip()
                        parts = line.split(";")
                        password, film_data = parts[1], parts[2]
                        userHasFilmAndWatchedIt = False
                        if password == self.password:
                            film_data = film_data.split(",")
                            for film in film_data:
                                idAndRating = film.split(":")
                                if idAndRating[0] == str(filmId) and idAndRating[1] == "true":
                                    userHasFilmAndWatchedIt = True
                                    break
                    if userHasFilmAndWatchedIt:
                        with open("Data/Ratings.txt", 'a') as file:
                            file.write(f"\n{self.nickname};{filmId};{rating};{comment}")
                        print("rating added")
                    else:
                        print("cannot add rating because user did not watched that film")

                # with open("Data/Ratings.txt",'a') as file:
                #     file.write(f"{self.nickname};{filmId};{rating};{comment}\n")
                #     print("rating added")


pass

def getAllUsers() -> list[User]:
    with open('Data/Users.txt', 'r') as file:
        users = []
        for line in file:
            userParts = line.split(";")
            user = User(userParts[0], userParts[1])
            users.append(user)

        return users

def user_exists(checked_user) -> bool:
    for user in getAllUsers():
        if checked_user.nickname == user.nickname:
            if checked_user.password == user.password:
                return True
    return False

