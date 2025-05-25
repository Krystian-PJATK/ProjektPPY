import Film
import User

#User commands
def command_list():
    print("Available films:")
    for film in Film.all_films():
        print(film.user_friendly_str())

def command_add():
    new_film_title = input("Title: ")
    new_film_prodYear = input("Year: ")
    new_film_genre = input("Genre: ")
    new_film_director = input("Director: ")
    new_film_ID = Film.getBiggestID() + 1

    new_film = Film.Film(new_film_ID, new_film_title, new_film_director, new_film_genre, new_film_prodYear)
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

def command_mylist(user,status):
    films1 = user.getFilms(status)
    print("Your films with status: "+status)
    for film in films1:
        print(film)
        print("Average rating: "+str(film.film.getAvrageRating())+"\n")

def command_watch(user,filmId):
    user.watch(filmId)

def command_addtomywatchlist(user,filmId):
    user.addToMyWatchlist(filmId)

def command_deleteFilmFromWatchlist(user,filmId):
    user.deleteFilmFromMyWatchlist(filmId)

def command_export(user: User.User):
    if user.export_films():
        print("Films exported")
    else:
        print("Could not export films")

def command_rate(user,filmid,rating,comment):
    user.rateFilm(filmid,rating,comment)

def command_commands():
    # Present all commands
    print("Available commands:")
    # Implemented
    print("\tlist - list all films")
    # Implemented
    print("\tadd  - add a film")
    # Implemented
    print("\taddToWatch - add film to watchlist")
    # Implemented
    print("\trate - add rating to the selected film")
    # Implemented
    print("\tdeleteFromWatchList - deletes a film from watchlist")
    # Implemented
    print("\tdel  - delete a film")
    # Implemented
    print("\tedit  - edits film information")
    # Implemented
    print("\twatch - watch a film")
    # Implemented
    print("\tsearch - search a film")
    # Implemented
    print("\tmylist - list all films watched and marked to watch")
    # Implemented
    print("\texport - exports user's watchlist onto desktop")
    #Implemented
    print("\tcommands - list all commands")
    # Implemented
    print("\texit - exit program")

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
command_commands()

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
        case "rate":
            filmid = input("type film ID: \n")
            rating = input("type rating from 1-10 \n")
            comment = input("type comment briefly summarizing the film\n")
            command_rate(currentUser,filmid,rating,comment)
        case "export":
            command_export(currentUser)
        case "help" | "commands":
            command_commands()
        case "exit":
            break
        case _:
            print("Unknown command")


print("Goodbye")



# def searchForFilmFrom