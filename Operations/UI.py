'''##UI
Clase Estatica de Interfaz de Usuario'''
import Operations.CSV_Controller
from Operations.Gens import Gens as gens
import os,time
'''Importacion de los otros modulos del paquete'''

def getArray():
    '''# Get Array\n
    Metodo invocable para generar una lista obteniendo valores introducidos por el usuario.\n
    Notas:\n
    - En desuso'''
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
    '''# Start \n
    Método principal del Programa.
    Se pregunta si quiere iniciar el programa o si quiere salir.\n
    - El metodo directo que invoca es el de CSV_Controller.exportar_csv(args)'''
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