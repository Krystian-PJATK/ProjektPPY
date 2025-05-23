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
        print(film.user_friendly_str())

def command_watch(user,filmId):
    user.watch(filmId)

def command_addtomywatchlist(user,filmId):
    user.addToMyWatchlist(filmId)


def command_deleteFilmFromWatchlist(user,filmId):
    user.deleteFilmFromMyWatchlist(filmId)

def command_search(user,userinput):
    user.search(userinput)






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
print("addToWatch - add film to watchlist")
#Implemented
print("rate - add rating to the selected film")
#Implemented
print("deleteFromWatchList - deletes a film from watchlist")
#Implemented
print("myList - list all films")
#Implemented
print("add  - add a film")
#Implemented
print("del  - delete a film")
#Implemented
print("watch - watch a film")
#Implemented
print("search - search a film")
#Implemented
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
            match input("Select type: watched, notWatched, all\n").lower().strip():
                case "watched":
                    command_mylist(currentUser,"watched")
                case "notwatched":
                    command_mylist(currentUser, "notwatched")
                case "all":
                    command_mylist(currentUser, "all")
                case _:
                    print("invalid status")
        case "watch":
            filmId = input("Type id of the film from your list that you want to watch: \n")
            command_watch(currentUser,filmId)
        case "addtowatch":
            filmId = input("Type id of the film from your list that you want to add to your watchlist: \n")
            command_addtomywatchlist(currentUser,filmId)
        case "deletefromwatchlist":
            filmId = input("Type id of the film from your list that you want to delete from your watchlist: \n")
            command_deleteFilmFromWatchlist(currentUser,filmId)
        case "search":
            userInput = input("Enter search term: \n")
            command_search(currentUser,userInput)
        case "rate":
            filmid = input("type film ID: \n")

            rating = input("type rating from 1-10 \n")
        case "exit":
            break
        case _:
            print("Unknown command")


print("Goodbye")



# def searchForFilmFrom