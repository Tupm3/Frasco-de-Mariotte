'''##UI
Clase Estatica de Interfaz de Usuario'''
import CSV_Controller, MathOp
'''Importacion de los otros modulos del paquete'''

@staticmethod
def getArray():
    lista = []
    print("Ingresa cada valor necesario para la lista.")
    print("Por cada valor presiona Enter para introducir un nuevo valor...")
    print("Para no introducir más valores, introduce la letra: s")
    while inp != 's':
        '''Letra 's' como valor para ya no introducir más valores a la lista'''
        lista.append(int(input("Ingresa valor: ")))
        ''' Se introducen los valores en la lista'''
    '''* Devuelve la lista generada *''''
    return lista