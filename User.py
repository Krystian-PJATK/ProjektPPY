from collections import defaultdict

import Film
from datetime import date
import matplotlib.pyplot as plt

# additional class for handling user films and additional data around them
class FilmWithDate:
    def __init__(self, film, related_date, state):
        self.film = film
        self.date = related_date
        self.state = state

    def __str__(self):
        return self.film.user_friendly_str() + "\n" + self.state + ": " + self.date

#Main user class
class User:
    #todo nickname must be unique. Check file
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password

    def get_films(self, status) -> list[FilmWithDate]:
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

        userFilms = self.get_films("all")
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
        userFilms = self.get_films("all")
        idFoundInListOfFilms = False
        for film in userFilms:
            if str(film.film.ID) == str(filmId):
                idFoundInListOfFilms = True
                break
        if idFoundInListOfFilms:
            print("You already have that film")
        else:
            idFoundInSystemListOfFilms = False
            systemFilms = Film.all_films()
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

        userFilms = self.get_films("all")
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
        watched_films = self.get_films('watched')
        notwatched_films = self.get_films('notwatched')

        lines = "Your watch list\n"
        lines += "Films you watched\n"
        for one_film in watched_films:
            lines += one_film.__str__() + '\n\n'

        lines += "Films you want to watch\n"
        for one_film in notwatched_films:
            lines += one_film.__str__() + '\n\n'

        try:
            file = open('ExportedWatchlist.txt', 'w')
            file.write(lines)
            #Te dwie linijki mają zapewnić, że zapiszę się plik jeszcze w trakcie wykonywanie programu
            # Jednak nie działają >:(
            # file.flush()
            # os.fsync(file.fileno())
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
                    userHasFilmAndWatchedIt = False
                    for line in lines:
                        if userHasFilmAndWatchedIt:
                            break
                        line = line.strip()
                        parts = line.split(";")
                        password, film_data = parts[1], parts[2]
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

    def statistics(self):
        all_movies = Film.all_films()
        movie_rating_map = {}
        for movie in all_movies:
            avg_rating = movie.getAverageRating()
            if avg_rating is not None:
                movie_rating_map[movie] = avg_rating

        sorted_movies = sorted(movie_rating_map.items(), key=lambda x: x[1], reverse=True)
        top3 = sorted_movies[:3]

        movie_names = [film.Title for film, _ in top3]
        avg_scores = [rating for _, rating in top3]

        plt.figure(figsize=(8, 5))
        plt.bar(movie_names, avg_scores, color='orange')
        plt.xlabel('Film')
        plt.ylabel('Średnia ocena')
        plt.title('Top 3 filmy wg średniej oceny')
        plt.ylim(0, 10)
        for i, score in enumerate(avg_scores):
            plt.text(i, score + 0.1, f"{score:.2f}", ha='center')
        plt.tight_layout()
        plt.show()

        watch_count = defaultdict(int)
        with open("Data/Users.txt", 'r') as f:
            for line in f:
                parts = line.strip().split(';')
                if len(parts) < 3:
                    continue

                film_entries = parts[2:]
                for entry in film_entries:
                    for film_data in entry.split(','):
                        try:
                            film_id_str, watched_str, _ = film_data.strip().split(':')
                            film_id = int(film_id_str)
                            watched = watched_str.lower() == 'true'

                            if watched:
                                watch_count[film_id] += 1
                        except ValueError:
                            continue

        film_map = {film.ID: film.Title for film in Film.all_films()}

        sorted_watches = sorted(watch_count.items(), key=lambda x: x[1], reverse=True)
        top_movies = sorted_watches[:3]

        movie_titles = [film_map.get(film_id, f"Film {film_id}") for film_id, _ in top_movies]
        view_counts = [count for _, count in top_movies]

        plt.figure(figsize=(10, 6))
        plt.bar(movie_titles, view_counts, color='purple')
        plt.xlabel('Tytuł filmu')
        plt.ylabel('Liczba obejrzeń')
        plt.title(f'Top 3 najczęściej oglądanych filmów')
        # plt.xticks(rotation=30, ha='right')
        for i, count in enumerate(view_counts):
            plt.text(i, count + 0.2, str(count), ha='center')
        plt.tight_layout()
        plt.show()

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





