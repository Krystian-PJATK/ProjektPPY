class Film:
    ID: int
    Title: str
    Director: str
    Genre: str
    ProdYear: str

    biggestID = 0

    # def __init__(self, title: str, director: str, genre: str, prod_year: str):
    #     self.getBiggestID()
    #     self.ID = Film.biggestID
    #     Film.biggestID += 1
    #     self.Title = title
    #     self.Director = director
    #     self.Genre = genre
    #     self.ProdYear = prod_year
    #     self.addToFile()

    def init_from_string(self, fileline: str):
        fileline = str.replace(fileline, '\n', "")
        attributes = fileline.split(sep=';')
        self.ID = int(attributes[0])
        self.Title = attributes[1]
        self.Director = attributes[2]
        self.Genre = attributes[3]
        self.ProdYear = attributes[4]
        return self




    def __str__(self):
        output = str(self.ID) + ';'
        output += str(self.Title) + ';'
        output += str(self.Director) + ';'
        output += str(self.Genre) + ';'
        output += str(self.ProdYear) + ';'
        return f"{self.ID};{self.Title};{self.Director};{self.Genre};{self.ProdYear}"

    def user_friendly_str(self) -> str:
        return f"{self.ID} - {self.Title} ({self.ProdYear}) \n\tDirector: {self.Director} \n\tGenre: {self.Genre}"

    #todo
    def getBiggestID(self):
        currentBiggestID = 0
        #Wczytaj plik i znajdź największe id w Films.txt,
        # jeśli nie ma największego nic nie rób
        return currentBiggestID

    #todo
    def addToFile(self):
        #przerób siebie na tekst i dopisz linijkę w films.txt
        #po uruchomieniu konstruktora automatycznie dodajemy do pliku z wszystkim filmami
        return True

    #todo
    def deleteFilmFromFile(ID):
        #usuń rekord z pliku Films.txt gdzie jest takie samo ID co na obiekcie, z którego wywołujemy tę metodę
        return True

    #todo
    def editFilmFromFile(ID):
        #po id dostarczonym rzez argument metody przeszukuje plik testowy, pobiera linijkę i edytuje wybraną część
        #program pyta sie o id filmu, potem o pole które chce edytować np. tytuł a następnie wprowadza nową wartość.
        return True

    def rateFilmFromFile(filmID, userID, rateing, comment):
        #Najpierw sprawdź czy nie wystawił już opini
        # przed wprowadzeniem oceny do pliku sprawdzamy czy nie istnieje już ocena danego użytkownika do danego filmu
        #rating w skali od 0-10 w innym wypadku pluje exception
        #zapisujemy do pliku ocen i komentarzy w kolejności, filmId, userid, rating, comment
        return True

pass


# Returns all films from file Films.txt
def all_films() -> list[Film]:
    with open('Data/Films.txt', 'r') as file:
        films_list = []

        for line in file:
            film = Film.init_from_string(Film(), line)
            films_list.append(film)

        return films_list
