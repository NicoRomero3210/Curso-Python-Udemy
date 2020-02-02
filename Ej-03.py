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
"""
#Clase 40 Bases de Datos



