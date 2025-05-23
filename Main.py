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

#todo Fix user.GetFilms() returning null >:(
def command_mylist(user,status):
    films1 = user.getFilms(status)
    print("Your films with status: "+status)
    for film in films1:
        print(film)


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
#Implemented
print("add  - add a film")
#Implemented
print("del  - delete a film")
#todo
print("search - search a film")
#todo
print("mylist - list all films watched and marked to watch")
#Implemented
print("exit - exit program")

while True:
    match input("Enter command: ").lower().strip():
        case "list":
            command_list()
        case "add":
            command_add()
        case "del":
            command_delete()
        case "mylist":
            match input("Select type: watched, notWatched, all").lower().strip():
                case "watched":
                    command_mylist(currentUser,"watched")
                case "notwatched":
                    command_mylist(currentUser, "notwatched")
                case "all":
                    command_mylist(currentUser, "all")
                case _:
                    print("invalid status")
        case "exit":
            break
        case _:
            print("Unknown command")


print("Goodbye")



# def searchForFilmFrom