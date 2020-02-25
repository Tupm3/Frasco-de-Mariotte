'''## MathOp
Clase Estatica de Calculos'''
from math import sqrt, pow 
'''Importación de sqrt() y pow'''
@staticmethod
def promedio(lista):
    ''' # Promedio\n
    Método invocable para obtener el promedio\n
    Requiere:\n
    - Lista de Datos'''
    s = 0
    for i in range (0,len(lista)):
        s += lista[i]
    ''' * Devuelve el promedio '''
    return s/len(lista)

@staticmethod
def standardDev(lista):
    ''' # Desviacion Estandar\n 
    Método invocable para obtener la Desviación Standard de una lista\n
    Requiere:\n
    - Lista de Datos '''
    ''' Iniciacion de variables'''
    N = len(lista)
    xProm = promedio(lista)
    s =  0
    ''' Suma de los datos'''
    for i in range (0,N):
        s += (lista[i]-xProm)
    '''* Aplicacion de la formula de Desviacion Standard *'''
    return sqrt(s/N)

@staticmethod
def error(flist, slist):
    ''' # Error \n
    Método invocable para obtener el error para un dato usando la forma \n
    ((sp*f)+(fp*s))/pow(sp,2)\n
    Requiere: \n
    - Lista de Primer Dato
    - Lista de Segundo Dato '''
    ''' De la primera lista se obtiene la Desviacion Estandar y el Promedio'''
    f = standardDev(flist)
    fp = promedio(flist)
    ''' De la segunda lista se obtiene la Desviacion Estandar y el Promedio'''
    s = standardDev(slist)
    sp = promedio(slist)
    '''* Aplicacion de la formula para devolver el error *'''
    return ((sp*f)+(fp*s))/pow(sp,2)

@staticmethod
def torricelliEq(H):
    ''' # Teorema de Torricelli \n
    Metodo invocable para obtener velocidad siguiendo la ecuacion:
    v = sqrt((2*g)*H)\n
    Requiere:\n
    - Altura (H)'''
    '''* Aplicacion de la formula para devolver la velocidad *'''
    return sqrt((19.62)*H)

@staticmethod
def getDensity(m,v):
    ''' # Get Density\n
    Método para obtener la densidad de un liquido por la forma
    den = m/V \n
    Requiere:\n
    - Masa
    - Volumen '''
    return m/v

def caudalError(H):
    '''# Error del Caudal\n
    Devuelve el error a partir de la ecuacion de Torricelli '''
    return sqrt(19.62) * (0.5*(pow(promedio(H),-0.5))) * standardDev(H)

@staticmethod
def energiaK(caudal):
    '''# Energia Cinética \n 
    Devuelve un valor de acuerdo al valor del caudal. \n
    Requiere:\n
    - Valor del Caudal'''
    k = (0.5*getDensity(2.6,(21*121)))*pow(caudal,2)
    '''* Devuelve el dato *'''
    return k

@staticmethod
def energiaKError(caudalList,vel):
    '''# Error de la Energía Cinética\n
    Devuelve el error de la Energía Cinética\n
    Requiere:\n
    - Lista de Valores de Caudal
    - Lista de velocidades'''
    return 0.5((2*getDensity(2.6,121*21)*promedio(caudalList)*caudalError(caudalList))+((pow(promedio(vel),2))*(promedio(121*21)* standardDev(2.6))+promedio(2.6)*standardDev(121*21))/pow(promedio(121*11),2))