import Film
from Film import all_films


class User:


    #todo nickname must be unique. Check file
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password

    def getFilms(self,status):
        finalfilms = []
        #zwraca toStringi Filmów z listy filmów użytkownika, na którym metoda zostaje wywołana
        with open('Data/Users.txt', 'r') as file:
            for line in file:
                line = str.replace(line, '\n', '')
                #szukamy danych użytkownika
                if self.nickname in line:
                    userParts = line.split(";")
                    if len(userParts) <3:
                        print("user does not have any saved films")
                        return []
                    #pobieramy filmy z listy użytkownika
                    userfilms = {}
                    filmpairs = userParts[2].split(',')
                    for pair in filmpairs:
                        film_id, flag = pair.split(":")
                        userfilms[film_id] = flag
                    with open('Data/Films.txt', 'r') as filmfile:
                        for film in filmfile:
                            film = str.replace(film, '\n', '')
                            filmData = film.split(";")
                            if filmData[0] in userfilms :
                                match status:
                                    case "watched":
                                        if userfilms[filmData[0]].lower() == 'true':
                                            film = Film.Film(int(filmData[0]), filmData[1], filmData[2],filmData[3],filmData[4])
                                            finalfilms.append(film)
                                    case "notwatched":
                                        if userfilms[filmData[0]].lower() == 'false':
                                            film = Film.Film(int(filmData[0]), filmData[1], filmData[2], filmData[3],
                                                             filmData[4])
                                            finalfilms.append(film)
                                    case "all":
                                        if userfilms[filmData[0]].lower() == 'true':
                                            film = Film.Film(int(filmData[0]), filmData[1], filmData[2], filmData[3],
                                                             filmData[4])
                                            finalfilms.append(film)
                                        elif userfilms[filmData[0]].lower() == 'false':
                                            film = Film.Film(int(filmData[0]), filmData[1], filmData[2], filmData[3],
                                                             filmData[4])
                                            finalfilms.append(film)
                    return finalfilms
        return finalfilms

    def watch(self, filmId):
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
                            if film_id == filmId and status == "false":
                                newFilm_line.append(f"{film_id}:true")
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
            if str(film.ID) == str(filmId):
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
                            film_line.append(f"{filmId}:false")
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


def rateFilm(self, filmId, rating, comment):
        checkIfAlreadyRated = False

        #kokatenacja tekstu, który sprawdzamy, czy istnieje w pliku, czyli patrzymy czy osoba o danym nicku dodała już opinię na dany film
        searchingText = f"{self.nickname} {str(filmId)}"
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
                        with open("Data/ratingsAndComments.txt", 'a') as file:
                            file.write(f"{self.nickname};{filmId};{rating};{comment}\n")
                        print("rating added")
                    else:
                        print("cannot add rating because user did not watched that film")

            with open("Data/ratingsAndComments.txt",'a') as file:
                file.write(f"{self.nickname};{filmId};{rating};{comment}\n")
                print("rating added")
            print("rating added")

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
            if checked_user.password == user.nickname:
                return True
    return False

