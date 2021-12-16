# ID Primo
import matplotlib.pyplot as plt
from aux_functions import getAllPokemons, getPokemonByName, getLocationsByName, getTypesByName, getWeaknessesByName


def numPrimo(id):
  esPrimo = True
  for num in range(2,id):
    if id % num == 0:
      esPrimo = False
      break
  return esPrimo

def pkmPrimo():
    im = plt.imread('Kanto.png')
    plt.imshow(im)
    pokedex = getAllPokemons()
    lista = []
    numCont = 0
    ejeX = []
    ejeY = []
    for dato in pokedex:
        pkmID = dato["id"]
        pkmName = dato["name"]
        if numPrimo(pkmID) and numCont != 0:
            lista.append(pkmID)
            lista.append(pkmName)
            loc = getLocationsByName(pkmName)
            for x in loc[0]:
                ejeX.append(x)
            for y in loc[1]:
                ejeY.append(y)

        numCont += 1

    plt.plot(ejeX, ejeY, 'o', color='lawngreen')
    plt.legend(["Prime ID's Locations"], loc="lower right")
    plt.show()