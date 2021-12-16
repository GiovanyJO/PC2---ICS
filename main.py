"""
• Crear un diagrama de dispersión en el cual se muestre la altura de los pokemones en centimetros en el eje X, y el peso de los pokemones en kg en el eje Y.
"""
opc = input('Hola, ¿qué gráfico deseas ver?\n[1] Gráfico de Barras\n[2] Gráfico de Pie\n[3] Scatterplot\n[4] Mapa de Kanto\nTu elección es: ')
while opc not in ['1','2','3','4']:
  opc = input('No existe esa opción, elige otra: ')
opc = int(opc)
if opc == 1:
  print('Este gráfico nos indica la cantidad de debilidades totales en todos los pokemones en la 1ra Generación')
  from grafico_de_barras import grafBarras
  grafBarras()
elif opc == 2:
  print('Este gráfico nos indica el porcentaje de todos los tipos que existen en la 1ra Generación')
  from graficoPie import graficoPie
  graficoPie()
elif opc == 3:
  print('Este gráfico nos indica el peso y la altura de todos los pokemones')
  from scatt import weiHei
  weiHei()
else:
  print('En este mapa de Kanto, podemos ver a los pokemones cuyo ID es un número primo')
  from idPrimo import pkmPrimo
  pkmPrimo()