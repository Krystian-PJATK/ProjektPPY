from Film import *

import Film

def getFilms() -> list[Film.Film]:
    #pobiera listę filmów, wczytuje do listy i foruje wypisując toStringi każdego z obiektów
    filmsList = []
    file = open('Data/Films.txt', 'r')
    for line in file:
        film = Film.Film.initfromstring(Film.Film(), line)
        filmsList.append(film)
    return filmsList

tmp = getFilms()

for film in tmp:
    print(film)



# def searchForFilmFrom