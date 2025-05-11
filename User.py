class User:
    #todo nickname must be unique. Check file
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password

    def getFilms(self):
        #zwraca toStringi Filmów z listy filmów użytkownika na którym metoda zostaje wywoałana
        with open('Data/Users.txt', 'r') as file:
            for line in file:

                #szukamy danych użytkownika
                if self.nickname in line:
                    userParts = line.split(";")
                    userFilms = userParts[1].split(',')
                    for filmInfo in userFilms:
                        with open('Data/Films.txt', 'a') as filmfile:
                            for film in filmfile:
                                filmData = film.split(";")
                                if filmData[0] in userFilms:
                                    print(film)


    def rateFilm(self, filmId, rating, comment):
        checkIfAlreadyRated = False

        #kokatenacja tekstu który sprawdzamy czy itnieje w pliku czyli patrzymy czy osoba o danym nicku dodała już opinię na danyc film
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
            with open("Data/ratingsAndComments.txt",'a') as file:
                file.write(f"{self.nickname};{filmId};{rating};{comment}\n")
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