import Film
import User

#User commands
def command_list():
    print("Available films:")
    for film in Film.all_films():
        print(film.user_friendly_str())

def command_add():
    new_film = Film.Film()
    new_film.Title = input("Title: ")
    new_film.ProdYear = input("Year: ")
    new_film.Genre = input("Genre: ")
    new_film.Director = input("Director: ")
    new_film.ID = Film.getBiggestID() + 1
    Film.Film.addToFile(new_film)
    print("Film Added")

def command_delete():
    film_id = int(input("ID of film to remove: "))
    if Film.Film.deleteFilmFromFile(film_id):
        print("Film Deleted")
    else:
        print("Film not found")

def command_edit():
    film_id = int(input("ID of film to edit: "))
    print("Editing Film")

    filmToBeEdited = None

    films = Film.all_films()
    for film in films:
        if film.ID == film_id:
            filmToBeEdited = film
            break

    print("[Attribute name]: [Value]")
    for key, value in filmToBeEdited.__dict__.items():
        print(f"\t{key}: {value}")
    #which attribute?
    while True:
        atr_name = input("Give attribute name to edit: ")
        if atr_name == "ID":
            print("ID can't be edited")
            continue
        else:
            if filmToBeEdited.__dict__.keys().__contains__(atr_name):
                break
            else:
                print("Attribute not found")
                continue

    #give new value
    atr_value = input("Give attribute value: ")

    if Film.Film.editFilmFromFile(film_id, atr_name, atr_value):
        print("Film Edited")
    else:
        print("Film wasn't edited")

def command_search():
    searched_phrase = input("Search film with title: ").lower()
    films = Film.all_films()
    returned_films = []
    for film in films:
        if film.Title.lower().find(searched_phrase) != -1:
            returned_films.append(film)

    for film in returned_films:
        print(film.user_friendly_str())

#todo Fix user.GetFilms() returning null >:(
def command_mylist(user):
    films = user.getFilms()
    print("Films you watched:")
    for film in films:
        print(film.user_friendly_str())


#Login loop
while True:
    #Get prompt
    nickname = input("Nickname: ")
    password = input("Password: ")
    currentUser = User.User(nickname, password)

    #Check if user exists
    if User.user_exists(currentUser):
        print("Welcome " + currentUser.nickname)
        break
    else:
        print("User not found or password incorrect\n")
        continue
pass

#Now user is logged in
#Present "Home screen" with all commands
print("Available commands:")
#Implemented
print("\tlist - list all films")
#Implemented
print("\tadd  - add a film")
#Implemented
print("\tdel  - delete a film")
#Implemented
print("\tedit  - edits film information")
#Implemented
print("\tsearch - search a film")
#todo
print("\tmylist - list all films watched and marked to watch")
#Implemented
print("\texit - exit program")

while True:
    match input("Enter command: ").lower().strip():
        case "list":
            command_list()
        case "add":
            command_add()
        case "del":
            command_delete()
        case "edit":
            command_edit()
        case "search":
            command_search()
        case "mylist":
            command_mylist(currentUser)
        case "exit":
            break
        case _:
            print("Unknown command")


print("Goodbye")



# def searchForFilmFrom