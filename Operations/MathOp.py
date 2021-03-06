'''## MathOp
Clase Estatica de Calculos'''
from math import sqrt, pow
import Operations
'''Importación de sqrt() y pow'''
class MathOp:
    '''
    # MathOP\n
    - Clase Estática de Cálculos
    '''
    @staticmethod
    def promedio(lista):
        ''' # Promedio\n
        Método invocable para obtener el promedio\n
        Requiere:\n
        - Lista de Datos'''
        s = 0
        try:
            '''Manejo de Excepciones en caso de obtener solo un valor en la lista '''
            for i in range (0,len(lista)):
                s += float(lista[i])
            result = s/len(lista)
        except Exception as e:
            result =lista/1
        ''' * Devuelve el promedio '''
        return result
    @staticmethod
    def standardDev(lista):
        ''' # Desviacion Estandar\n 
        Método invocable para obtener la Desviación Standard de una lista\n
        Requiere:\n
        - Lista de Datos '''
        ''' Iniciacion de variables'''
        if type(lista) == float:
            '''Manejo de Excepciones en caso de recibir solo un valor.'''
            listan = Operations.Gens.Gens.generateData(lista,10)
        else: 
            listan = lista
        N = len(listan)
        xProm = promedio(listan)
        s =  0
        ''' Suma de los datos'''
        for i in range (0,N):
            s += (float(listan[i])-xProm)
        '''* Aplicacion de la formula de Desviacion Standard *'''
        return sqrt(abs(s/N))
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
    @staticmethod
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
        k = ((0.5*getDensity(2600,(21*121)))*pow(float(caudal),2))/pow(10,7)
        '''* Devuelve el dato *'''
        return k
    @staticmethod
    def energiaKError(caudalList,vel):
        '''# Error de la Energía Cinética\n
        Devuelve el error de la Energía Cinética\n
        Requiere:\n
        - Lista de Valores de Caudal
        - Lista de velocidades'''
        return 0.5*((2*getDensity(2600,121*21)*promedio(caudalList)*caudalError(caudalList))+((pow(promedio(vel),2))*(promedio(121*21)*standardDev(getDensity(2600,21*121)))+promedio(2.6)*standardDev(getDensity(2600,21*121))/pow(promedio(121*11),2)))