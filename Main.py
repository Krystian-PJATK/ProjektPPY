import Film
import User


# def get_films() -> list[Film.Film]:
#     #pobiera listę filmów, wczytuje do listy i foruje wypisując toStringi każdego z obiektów
#     filmsList = []
#     file = open('Data/Films.txt', 'r')
#     for line in file:
#         film = Film.Film.initfromstring(Film.Film(), line)
#         filmsList.append(film)
#     return filmsList
#
# tmp = get_films()
#
# for film in tmp:
#     print(film)



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
print("(commands)")

print("Koniec")



# def searchForFilmFrom