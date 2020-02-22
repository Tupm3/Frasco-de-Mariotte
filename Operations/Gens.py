'''##Gens
Clase Estatica para generar datos e.e '''
import random
'''Importacion de la libreria random'''
@staticmethod
def generateData(data, num):
    '''# Generate Data\n
    Metodo invocable para generar datos con una vaiacion pequeña e.e\n
    Requiere:
    - El dato base
    - Numero de datos que va a generar la lista '''
    lista = []
    for i in range(0,num):
        lista.append(float(random.uniform(data+0.1,data+0.6)))
        ''' Agrega a la lista un numero aleatorio del dato + una variacion entre 0.1 y 0.6 '''
    '''* Regresa la lista *'''
    return lista