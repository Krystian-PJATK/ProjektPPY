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
        break
    else:
        print("User not found or password incorrect\n")
        continue
pass

#Now user is logged in
#Present "Home screen" with all commands
print("Welcome " + currentUser.nickname)
print("Available commands:")
#Implemented
print("\tlist - list all films")
#Implemented
print("\tadd  - add a film")
#Implemented
print("\tdel  - delete a film")
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