'''##CSV_Controller
Clase Estatica de Manejo de Archivos CSV'''
from csv import writer, QUOTE_MINIMAL
'''Importacion de elementos necesarios para CSV'''
csv_File = "Resultados.csv"
'''Nombre del archivo de Salida''''
#------------------------------------#
'''*****Clase incompleta*****'''
'''
# TODO
- Definir Parametros
- Cambiar las variables y nombres de Salida
- Verificar posibles Excepciones de Salida
'''
@staticmethodu
def exportar_csv(params):
    #TODO
    '''Definicion de Parametros para el manejo de CSV'''
    renglon = []
    '''Iniciacion de la lista 'renglon' que servira para imprimir las variables en el CSV'''
    try:
        ''' Debido al manejo de archivos, es necesario manejo de Excepciones '''
        with open(file,"w",newline='') as csv_file:
            '''Usando un archivo 'creable' llamado #csv_file#'''
            f_write = writer(csv_file, delimiter = ',', quotechar='"', quoting=QUOTE_MINIMAL)####
            '''Iniciacion del writer de CSV. ##LINEA OBLIGATORIA##'''
            #f_write.writerow(["x" , "y" , "Distancia", "Radio de Curvatura", "Vel Max"])
            #TODO
            '''Titulos del CSV'''
            for i in range (0, len(x)):
                #renglon = [str(x[i]), str(y[i]), str(dist[i]),str(curvas[i]),str(vmax[i])]
                #TODO
                ''' Cambiar variables de salida'''
                f_write.writerow(renglon)
                '''Escritura del 'renglon' en el CSV'''
        print("Resultados exportados a: ",file)
        ''' Mensaje de Operacion Completada'''
    except Exception as e:
        ''' TODO Verifiacion de Excepciones '''
        print("Error no controlado...")
        print(e) #Impresion del Error