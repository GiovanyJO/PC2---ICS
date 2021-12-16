import matplotlib.pyplot as plt

from aux_functions import getAllPokemons, getPokemonByName, getLocationsByName, getTypesByName, getWeaknessesByName

#Grafico Pie
def graficoPie():
    tip = {}
    pokedex = getAllPokemons()

    for pkms in pokedex:
        for t in pkms["type"]:
            if t not in tip.keys():
                tip[t] = 1
            else:
                tip[t] += 1

    colores = ['forestgreen', 'purple', 'red', 'skyblue', 'dodgerblue', 'greenyellow', 'lightgray', 'yellow',
              'darkgoldenrod', 'sienna', 'fuchsia', 'maroon', 'cyan', 'slateblue', 'skyblue']
    ejeX = []
    ejeY = []
    for i, v in tip.items():
        ejeY.append(v)
        ejeX.append(i)
    desfase = (0.1, 0.1, 0.2, 0.3, 0.1, 0.3, 0.1, 0.3, 0.3, 0.1, 0.3, 0.35, 0.375, 0.4, 0.4)
    plt.pie(ejeY, labels = ejeX, autopct="%0.1f %%", shadow = True, startangle = 45, colors = colores, explode = desfase)
    plt.show()