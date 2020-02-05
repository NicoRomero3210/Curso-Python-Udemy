"""
#Clase 35 Lectura archivo Binario

import pickle

fichero = open('ficheroBinario.pckl','rb')

print(pickle.load(fichero))

#Clase 36 Gestion de Errores

try:
    print(5/1)
except ZeroDivisionError:
    print('Surgio alto error ') #Este Except se ejecuta si sucede el error de Division por Cero
except:
    print('Error desconocido')  #Este se ejecuta si sucede un error desconocido
else:
    print('La division funciono Correctamente') #Este funciona con el try
finally:
    print('Acabo la prueba')

#Clase 37 Expresiones regulares

import re #Esta es la libreria que tiene los metodos de las expresiones regulares

texto1 = "Que ni la pija, te queda hermano, ni la pija me queda a mi"

print(re.search("pija",texto1))

res1 = re.search("pija",texto1)

re.search("mi$",texto1) #Busca que la cadena dada este en el final

re.search("^pija",texto1) #Busca qe la palabra este ene el inicio del texto

re.search("ni.*pija",texto1) #Busca que esas dos palabras formen parte de una oracion sin importar lo que haya en el medio

print(re.findall("ni.*pija",texto1)) #Encuentra todas las coincidencias

re.split(" ",texto1)

re.sub("pija","pene",texto1)

#Clase 38 JSON

import json

producto1 = {"nombre":"silla","color":"blanco","precio":1000}

estJsonProd1 = json.dumps(producto1) #Me convierte el diccionario en un JSON(osea un string)

print(estJsonProd1)

producto1retorno = json.loads(estJsonProd1) #Me convierte un JSON en un diccionario

print(producto1retorno["precio"])

#Clase 39 Fecha y Hora

from datetime import datetime

print(datetime.now())

fecha = datetime.now()

print(fecha.year)
print(fecha.month)
print(fecha.day)
print(fecha.hour)
print(fecha.minute)
print(fecha.second)

#Clase 40 Bases de Datos, crear una conexion

import sqlite3

conexion = sqlite3.connect("basededatos.db") #Me crea este archivo de extension db y eso se abre en sqlite

conexion.close()

#Clase 41 Crear una tabla en la BD

import sqlite3

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

cursor.execute('CREATE TABLE PERSONAS(nombre text, apellido text, edad integer)')

conexion.commit()

conexion.close()

#Clase 42 Insertar una fila en la BD

import sqlite3

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

cursor.execute('INSERT INTO PERSONAS VALUES("Ricardo","Iorio","57")')

conexion.commit()

conexion.close()

#Clase 43 Insertar varias Filas a la vezs

import sqlite3

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

Personas = [('Pablo','Perez',35),('Juan','Perez',55),('Mariano','Moreno',34),('Pedro','Perez',22),('Marcelo','Polino',44)]

cursor.executemany('INSERT INTO PERSONAS VALUES (?,?,?)',Personas)

conexion.commit()

conexion.close()

#Clase 44 Consultar datos

import sqlite3

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")

personas = cursor.fetchall()

for persona in personas:
    print(persona)

conexion.close()

#Clase 45 Consultar Datos con clausula Where

import sqlite3

conexion = sqlite3.connect('basededatos.db')

cursor = conexion.cursor()

cursor.execute('SELECT * FROM PERSONAS WHERE edad > 40')

personas = cursor.fetchall()

for persona in personas:
    print(persona)

conexion.close()

#Clase 46 Ordenar Datos

import sqlite3

conexion = sqlite3.connect('basededatos.db')

cursor = conexion.cursor()

cursor.execute('SELECT * FROM PERSONAS ORDER BY EDAD DESC')

personas = cursor.fetchall()

for persona in personas:
    print(persona)

conexion.close()

#Clase 47 Borrar Datos

import  sqlite3

conexion = sqlite3.connect('basededatos.db')

cursor = conexion.cursor()

cursor.execute('DELETE FROM PERSONAS WHERE apellido like "%POLINO%"')

conexion.commit()

conexion.close()

#Clase 48 Actualizar Datos en la Base

import sqlite3

conexion = sqlite3.connect('basededatos.db')

cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET edad = 19 WHERE nombre like '%Juan%'")

conexion.commit()

conexion.close()
"""

