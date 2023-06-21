#Clase 1 Proyecto - Definiendo la aventura Equipamiento - Costos de monedas Trekjuls
print("Hola, bienvenido al universo de acertijos más grande de todo Egipto, por favor define tu equipo y su valor en Trekjuls")

brujula = 40.66
amuleto = 10.2
mapa = 32.56
block = 23.22
snacks = 1.2
agua = 2
linterna = 4
lapiz = 0.2
baterias = 1.5

print("Lista ahora tres elementos de tu equipo: nombre y valor")

print("brujula",brujula)
print("agua",agua)
print("snacks",snacks)

#operadores
print("¿Puedes combinar los equipos para prepararte mejor")

mapa_y_brujula = mapa + brujula
linterna_baterias = linterna + baterias

print("Guía con mapa y brújula",mapa_y_brujula)
print("Linterna funcional",linterna_baterias)

print("¿El precio de la guía es menor al de la linterna funcional?")
print(mapa_y_brujula < linterna_baterias)

print("Si tengo 150 puntos, ¿me alcanza para comprar los 3 productos más caros?")

#Trabajando en las listas
recursos = [40.66,10.2,32.56,23.22,1.2,2,4,0.2,1.5]
max_recursos = max(recursos, key = int)
