'''##CSV_Controller
Clase Estatica de Manejo de Archivos CSV'''
from csv import writer, QUOTE_MINIMAL
'''Importacion de elementos necesarios para CSV'''
file = "Resultados.csv"
'''Nombre del archivo de Salida'''
#------------------------------------#
'''***** Revision Requerida *****'''
''' # TODO
- Verificar posibles Excepciones de Salida '''
@staticmethod
def exportar_csv(velM,ac,velS):
    '''# Exportar CSV\n
    Método invocable para exportar los datos a un archivo CSV\n
    Requiere\n
    - Lista de Velocidad Media\n
    - Lista de Aceleración Media\n
    - Lista de Velocidad de Salida\n
    Notas\n
    - Todas las listas deben tener 30 Posiciones '''
    renglon = []
    '''Iniciacion de la lista 'renglon' que servira para imprimir las variables en el CSV'''
    try:
        ''' Debido al manejo de archivos, es necesario manejo de Excepciones '''
        with open(file,"w",newline='') as csv_file:
            '''Usando un archivo 'creable' llamado #csv_file#'''
            f_write = writer(csv_file, delimiter = ',', quotechar='"', quoting=QUOTE_MINIMAL)####
            '''Iniciacion del writer de CSV. ##LINEA OBLIGATORIA##'''
            f_write.writerow(["Repetición","Velocidad Media","Aceleracion Media","Velocidad de Salida"])
            '''Titulos del CSV'''
            for i in range(0,30):
                 renglon = [i,str(velM[i]),str(ac[i]),str(velS[i])]
                 f_write.writerow(renglon)
                 ''' Variables de Salida. En orden:
                [" ", Velocidad Media, Aceleracion Media, Velocidad de Salida]'''
        print("Resultados exportados a: ",file)
        ''' Mensaje de Operacion Completada'''
    except Exception as e:
        ''' TODO Verifiacion de Excepciones '''
        print("Error no controlado...")
        print(e) #Impresion del Error