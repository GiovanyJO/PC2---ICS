"""
• Crear un diagrama de dispersión en el cual se muestre la altura de los pokemones en centimetros en el eje X, y el peso de los pokemones en kg en el eje Y.
"""
import matplotlib.pyplot as plt
import json


def getAllPokemons():
    f = open('pokemon.json')
    return json.load(f)

def weiHei():
  p = getAllPokemons()

  x = []
  for i in p:
      s = float(i['height'].replace('m', "").replace(' ', ""))
      x.append(s * 100)

  y = []
  for j in p:
      e = float(j['weight'].replace('kg', "").replace(' ', ""))
      y.append(e)

  plt.scatter(x, y, color = 'mediumaquamarine')
  plt.ylabel('Peso(kg)')
  plt.xlabel('Altura(cm)')
  plt.show()

# Scatterplot
