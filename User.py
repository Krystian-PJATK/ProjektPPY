class User:


    #todo nickname must be unique. Check file
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password

    def getFilms(self):
        #zwraca toStringi Filmów z listy filmów użytkownika na którym metoda zostaje wywoałana
        return True

    def rateFilm(self, filmId, rating, comment):
        checkIfAlreadyRated = False

        #kokatenacja tekstu który sprawdzamy czy itnieje w pliku czyli patrzymy czy osoba o danym nicku dodała już opinię na danyc film
        searchingText = f"{self.nickname} {str(filmId)}"
        try:
            with open("Data/ratingsAndComments.txt",'r') as file:
                for line in file:
                    if searchingText in line:
                        checkIfAlreadyRated = True
        except FileNotFoundError:
            print("RatingsAndComments.txt not found")
        if checkIfAlreadyRated:
            print("cannot rate same film more than once")
        else:
            with open("Data/ratingsAndComments.txt",'a') as file:
                file.write(f"{self.nickname};{filmId};{rating};{comment}\n")
            print("rating added")

