'''##UI
Clase Estatica de Interfaz de Usuario'''
import Operations.CSV_Controller
from Operations.Gens import Gens as gens
import os,time
'''Importacion de los otros modulos del paquete'''

def getArray():
    lista = []
    print("Ingresa cada valor necesario para la lista.")
    print("Por cada valor presiona Enter para introducir un nuevo valor...")
    print("Para no introducir más valores, introduce la letra: s")
    inp = "a"
    while inp != 's':
        '''Letra 's' como valor para ya no introducir más valores a la lista'''
        lista.append(int(input("Ingresa valor: ")))
        ''' Se introducen los valores en la lista'''
    '''* Devuelve la lista generada *'''
    return lista

def start():
    print("****BIENVENIDOS******")
    print("Cargando.",end="")
    for i in range(0,6): 
        print(".",end="")
        time.sleep(0.3)
    os.system('cls')
    op = input("Iniciar Exportacion de Datos S / N: ")
    if op == "S" or op == "s":
        Operations.CSV_Controller.exportar_csv(gens.velocidadMedia(),gens.aceleracionMedia(),gens.velocidadCaudal(),gens.kinectic(),gens.getTiempo(),gens.getAltura())
    else: "Sakc alv"
    print("Fin del Programa....")
    p = input("Presione cualquier tecla...")
    exit()