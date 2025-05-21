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
print("list - list all films")
#todo
print("add  - add a film")
#todo
print("del  - delete a film")
#todo
print("search - search a film")
#todo
print("mylist - list all films watched and marked to watch")
#Implemented
print("exit - exit program")

while True:
    match input("Enter command: "):
        case "list":
            command_list()
        case "add":
            command_add()
        case "mylist":
            command_mylist(currentUser)
        case "exit":
            break
        case _:
            print("Unknown command")


print("Goodbye")



# def searchForFilmFrom