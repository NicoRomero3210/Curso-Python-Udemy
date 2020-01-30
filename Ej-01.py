#Clase 07

numero = 5

cadena = str(5)

print(cadena)

print(type(cadena))

cadena = '25'

numero = int(cadena)

print(type(numero))


cadena = '25.7'

decimal = float(cadena)

print(type(decimal))

#Clase 8

cadena = "hola mundo"

cadena(5)

cadena(-1)

cadena(2:7)

cadena(2:)

cadena2 = "Carlos"

cadena = cadena + cadena2

#Clase 9

len(cadena)

cadena = cadena.upper()

print(cadena.split())

cadena2 = "frutas,manzanas,naranjas"

cadena2.split(',')

#Clase 10

nombre = "Richar"
edad = 18

print("Buenos dias {} feliz {} cumpleaños".format(nombre,edad))

resultado = 10 / 3

print("El resultado es: {r:1.3f}}".format(r=resultado))

print(f"Buenos dias {nombre} feliz {edad} cumpleaños")

#Clase 11

print('Introduzca un Nombre')

entrada = input()

print(f"Hola {entrada}")

#Clase 12 Operadores aritmeticos

resto = 5 % 2

cociente = 5 // 2 #Solo me da el numero entero, no me da los decimales

exponente = 2 ** 3

#Clase 13 Operadores de asignacion

numero = 1

numero1 += 2

numero1 =** 2

#Clase 14 Operadores de Comparacion

1 == 1 # Uno es igual a 1

#Clase 15 Operadores Logicos: En Python son: and, or y not

not(3>4)

#Clase 16

frutas1 = ['manzana','peras']
frutas2 = ['manzana','peras']
frutas3 = frutas1

frutas3 is frutas1 #frutas3 es el misimo objeto que frutas1?

frutas3.append('naranja') #Agrego un elemento a frutas3 y esto tmb impacta en frutas1 ya que son el mismo objeto

frutas3 is not frutas2

#Clase 17 Operadores de pertenencia

frutas1 = ['manzana','pera','naranja']

'pera' in frutas1

'frutilla' not in frutas1

#Clase 18 Listas

colores = ['rojo','azul','blanco']

colores[0] = 'azul'

len(colores)

colores.append('verde')

colores.remove('azul')

print(colores)

colores.clear()

print(colores)

#Clase 19 Tuplas

tuplaColores =  ('rojo','verde','amarilo')

print(tuplaColores[2])

len(tuplaColores)

#Clase 20 Conjuntos

conjuntoColores = {'azul','verde','rojo'}

conjuntoColores[2] #Esto da error porque es una coleccion desordenada

len(conjuntoColores)

conjuntoColores.add('negro')

print(conjuntoColores) #Como es una coleccion desordenada me inserto el elemento en cualquier lugar

conjuntoColores.remove('verde')

#Clase 21 Diccionarios

diccionarioColores = {'verde':'green','rojo':'red','azul':'blue'}

print(diccionarioColores)

diccionarioColores['red']

diccionarioColores['black'] = 'negro'

print(diccionarioColores)

diccionarioColores.pop('green')

del(diccionarioColores['black'])

for color in diccionarioColores:
	print(color) #Me va a mostrar solo la clave
	
for clave,valor in diccionarioColores.items():
	print(clave,valor) #Aca me muestra el par clave valor

	


