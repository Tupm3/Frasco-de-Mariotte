'''##CSV_Controller
Clase Estatica de Manejo de Archivos CSV'''
from csv import writer, QUOTE_MINIMAL
import os
'''Importacion de elementos necesarios para CSV'''
file = "ResultadosEx.csv"
path = os.getcwd()
resultPath = path+"\Resultados"
'''Nombre del archivo de Salida'''
def exportar_csv(velM,ac,velS,kinectic,tiempo,altura):
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
        os.chdir(resultPath)
        print(resultPath)
    except Exception as e:
        print(e)
    try:
        ''' Debido al manejo de archivos, es necesario manejo de Excepciones '''
        with open(file,"w",newline='') as csv_file:
            '''Usando un archivo 'creable' llamado #csv_file#'''
            f_write = writer(csv_file, delimiter = ',', quotechar='"', quoting=QUOTE_MINIMAL)####
            '''Iniciacion del writer de CSV. ##LINEA OBLIGATORIA##'''
            f_write.writerow(["Repetición","Velocidad Media","Aceleracion Media","Velocidad de Salida","Energía Cinética","Tiempo (s)","Altura (cm)"])
            '''Titulos del CSV'''
            for i in range(0,30):
                 renglon = [i+1,str(velM[i]),str(ac[i]),str(velS[i]),str(kinectic[i]),str(tiempo[i]),str(altura[i])]
                 f_write.writerow(renglon)
                 ''' Variables de Salida. En orden:
                [" ", Velocidad Media, Aceleracion Media, Velocidad de Salida]'''
        print("Resultados exportados a: ",file)
        ''' Mensaje de Operacion Completada'''
    except PermissionError as pe:
        print("Verifique que el archivo no esté en uso...")
        p = input("[ENTER]")
        exportar_csv(velM,ac,velS,kinectic,tiempo,altura)
    except Exception as e:
        ''' TODO Verifiacion de Excepciones '''
        print("Error no controlado...")
        print(e) #Impresion del Error
    
