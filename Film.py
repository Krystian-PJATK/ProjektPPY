import os

class Film:
    ID: int
    Title: str
    Director: str
    Genre: str
    ProdYear: str

    def __init__(self,id:int, title: str, director: str, genre: str, prod_year: str):
        self.ID = id
        self.Title = title
        self.Director = director
        self.Genre = genre
        self.ProdYear = prod_year

    def init_from_string(fileline: str):
        attributes = str.replace(fileline, '\n', "").split(sep=';')
        return Film(int(attributes[0]), attributes[1], attributes[2], attributes[3], attributes[4])

    def __str__(self):
        output = str(self.ID) + ';'
        output += str(self.Title) + ';'
        output += str(self.Director) + ';'
        output += str(self.Genre) + ';'
        output += str(self.ProdYear) + ';'
        return f"{self.ID};{self.Title};{self.Director};{self.Genre};{self.ProdYear}"

    def user_friendly_str(self) -> str:
        return f"{self.ID} - {self.Title} ({self.ProdYear}) \n\t\tDirector: {self.Director} \n\t\tGenre: {self.Genre}"

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

    def editFilmFromFile(ID: int, attribute, new_value) -> bool:
        isEdited = False
        try:
            films = open("Data/Films.txt", "r")
            data = films.readlines()
            films.close()

            lines = ""

            for line in data:
                if ID == int(line.split(sep=';')[0]):
                    edited_film = Film.init_from_string(line)

                    tmp = edited_film.__getattribute__(attribute)
                    attribute_type = type(tmp)

                    if attribute_type == int:
                        try:
                            new_value = int(new_value)
                        except ValueError:
                            print("Invalid value")
                            return False

                    edited_film.__setattr__(attribute, new_value)

                    lines += edited_film.__str__()+"\n"
                    isEdited = True
                    continue
                else:
                    lines += line

            #delete at the end in case of error in previous lines
            if isEdited:
                os.remove("Data/Films.txt")

            new_films_file = open("Data/Films.txt", "x")
            new_films_file.write(lines)
            new_films_file.close()

            return isEdited
        except FileNotFoundError:
            print("Films.txt not found")
            return False
        except TypeError:
            print("Wrong value type")
            return False
        except Exception:
            print("Something went wrong")
            return False

    def getAvrageRating(self):
        total = 0
        count = 0
        try:
            with open("Data/Ratings.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(";")
                    if len(parts) >= 3:
                        movie_id = parts[1]
                        rating = parts[2]
                        if movie_id == str(self.ID):
                            try:
                                total += int(rating)
                                count += 1
                            except ValueError:
                                pass
            return total / count if count > 0 else 0.0
        except FileNotFoundError:
            print("Plik Ratings.txt nie został znaleziony.")
            return 0.0


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
            film = Film.init_from_string(line)
            films_list.append(film)

        return films_list


