import os

class Film:
    ID: int
    Title: str
    Director: str
    Genre: str
    ProdYear: str

    biggestID = 0

    def __init__(self,id:int, title: str, director: str, genre: str, prod_year: str):
        #self.getBiggestID()
        self.ID = id
        Film.biggestID += 1
        self.Title = title
        self.Director = director
        self.Genre = genre
        self.ProdYear = prod_year

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

    def addToFile(self):
        #przerób siebie na tekst i dopisz linijkę w films.txt
        line = "\n" + self.__str__()

        try:
            films = open("Data/Films.txt", "a")
            films.write(line)
            films.close()
        except FileNotFoundError:
            print("Films.txt not found")

    def deleteFilmFromFile(ID: int) -> bool:
        #usuń rekord z pliku Films.txt gdzie jest takie samo ID co na obiekcie, z którego wywołujemy tę metodę
        isDeleted = False
        try:
            films = open("Data/Films.txt", "r")
            data = films.readlines()
            films.close()
            os.remove("Data/Films.txt")

            lines = ""

            for line in data:
                if ID == int(line.split(sep=';')[0]):
                    isDeleted = True
                    continue
                else:
                    lines += line

            new_films_file = open("Data/Films.txt", "x")
            new_films_file.write(lines)
            new_films_file.close()
            return isDeleted
        except FileNotFoundError:
            print("Films.txt not found")
            return False

    #todo
    def editFilmFromFile(ID):
        #Po id dostarczonym rzez argument metoda przeszukuje plik testowy, pobiera linijkę i edytuje wybraną część.
        #Program pyta się o id filmu, potem o pole, które chce edytować np. tytuł, a następnie wprowadza nową wartość.
        return True
    #todo
    def rateFilmFromFile(filmID, userID, rating, comment):
        #Najpierw sprawdź, czy nie wystawił już opinii.
        #Przed wprowadzeniem oceny do pliku sprawdzamy, czy nie istnieje już ocena danego użytkownika do danego filmu.
        #Rating jest w skali od 0 do 10, w innym wypadku wyrzuca exception.
        #Zapisujemy do pliku ocen i komentarzy w kolejności: filmID, userid, rating, comment
        return True

def getBiggestID() -> int | None:
    current_biggest_id = 0
    #Wczytaj plik i znajdź największe id w Films.txt,
    try:
        films = open("Data/Films.txt", "r")
        for line in films:
            id = int(line.split(sep=';')[0])
            if id > current_biggest_id:
                current_biggest_id = id
        films.close()
        return current_biggest_id
    except:
        return None

pass


# Returns all films from file Films.txt
def all_films() -> list[Film]:
    with open('Data/Films.txt', 'r') as file:
        films_list = []

        for line in file:
            film = Film.init_from_string(Film(), line)
            films_list.append(film)

        return films_list
