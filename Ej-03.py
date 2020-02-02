import pickle

fichero = open('ficheroBinario.pckl','rb')

print(pickle.load(fichero))