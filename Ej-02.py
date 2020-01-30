#Clase 22 Condicional If, elif y else

#Clase 025 Clases y Objetos

class ClaseSilla:
	color = "Blanco"
	precio = 100

objetoSilla1 = ClaseSilla()

print(objetoSilla1.color,objetoSilla1.precio)

objetoSilla2 = ClaseSilla()
objetoSilla2.color = "verde"
objetoSilla2.precio = 2

print(objetoSilla2.color,objetoSilla2.precio)

class Persona:

	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

	def saludar(self):
		print("Hola me llamo {} y tengo {} años".format(self.nombre, self.edad))

persona1 = Persona("Carlos",32)

persona1.saludar()

#Clase 026 Funciones

def saludar(nombre):
	print("Buenos dias {}".format(nombre))

saludar("Richar")

def sumar(n1,n2):
	return (n1 + n2)

print(sumar(10,32))

colores = ["Verde","Azul","Blanco"]
color = "Negro"

print(colores)

def insertarColor(lista,color):
	lista.append(color)

insertarColor(colores,color)

print(colores)

#CLase 027 Funciones Lambda

resultado = lambda numero: numero + 30

print(resultado(20))

resultado2 = lambda n1,n2,n3: n1 + n2 + n3

print(resultado2(1,2,3))

#Clase 028 Modulos






