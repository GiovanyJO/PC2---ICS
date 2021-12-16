"""
Crear un gráfico de barras en el cual se muestre los tipos de pokemon en el eje X, y la cantidad de pokemones que tienen dicho tipo como una debilidad en el eje Y.
"""
import matplotlib.pyplot as plt

from aux_functions import getAllPokemons, getPokemonByName, getLocationsByName, getTypesByName, getWeaknessesByName

# Gráficos de barras
def grafBarras():
    print("Ejecutando grafico_de_barras")
    debs = {}
    pokedex = getAllPokemons()
    colors = ['forestgreen', 'purple', 'red', 'skyblue', 'dodgerblue', 'greenyellow', 'lightgray', 'yellow',
              'darkgoldenrod', 'sienna', 'fuchsia', 'maroon', 'cyan', 'slateblue', 'midnightblue']
    for pkms in pokedex:
        for deb in pkms['weaknesses']:
            if deb not in debs.keys():
                debs[deb] = 1
            else:
                debs[deb] += 1

    ejeX = []
    ejeY = []
    for i, v in debs.items():
      ejeX.append(i)
      ejeY.append(v)
    plt.bar(ejeX, ejeY,color = colors, edgecolor = 'black')
    plt.ylabel('Cantidad de pokemones con esa debilidad')
    plt.show()