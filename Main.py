import Film
import User



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
#todo
print("list - list all films")
#todo
print("add  - add a film")
#todo
print("del  - delete a film")
#todo
print("search - search a film")
#Implemented
print("exit - exit program")

while True:
    match input("Enter command: "):
        case "exit":
            break
        case _:
            print("Unknown command")


print("Goodbye")



# def searchForFilmFrom