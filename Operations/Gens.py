'''##Gens
Clase Estatica para generar datos e.e '''
import random
from Operations.MathOp import MathOp as op
from math import fabs
'''Importacion de la libreria random'''
class Gens:
    '''# Clase de Generadores '''
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

    @staticmethod
    def gen_altura(promalt):
        '''# Generar Altura\n
        Metodo invocable para regresar la lista de alturas '''
        return Gens.generateData(promalt,30)
    
    @staticmethod 
    def gen_tiempo(data,num):
        '''# Generar Tiempo\n
        Metodo invocable para regresar una lista de tiempos '''
        lista = []
        for i in range(0,num):
            lista.append(int(random.randint(data-1,data+3)))
            ''' Agrega a la lista un numero aleatorio del dato + una variacion entre 0.1 y 0.6 '''
        '''* Regresa la lista *'''
        return lista

    @staticmethod
    def velocidad_media(altura = [0], tiempos = [0]):
        '''# Velocidad_media\n
        Genera los datos de velocidad sin asignar el error\n
        - Sobrecarga:
        Requiere:
        - Altura
        - Tiempo'''
        if len(altura)<= 1 and len(tiempos)<=1:
            altura= Gens.gen_altura(7)
            tiempos= Gens.gen_tiempo(110,10)
            # print(len(altura))
            # print(len(tiempos))
            tiempo=[111,112,113,111,112,110,116,110,112,110,109,112,111,108,109,111,112,110,113,112]
            ''' Lista de valores conociddos '''
            ''' Se generan tiempos alrededor del valor medio: 110 '''
            for elements in tiempos:
                tiempo.append(elements)
                ''' Se completa la lista general de tiempos '''
        else: tiempo = tiempos
        velocidades=[]
        for i in range(0,len(tiempo)):
            v=altura[i]/tiempo[i]
            velocidades.append(v)
            '''Se genera el valor de cada tiempo y se agrega a la lista general '''
        '''Devuelve las listas de velocidad, tiempo y altura generadas '''
        #print(len(velocidades))
        return velocidades,tiempo,altura
    
    @staticmethod    
    def getTiempo():
        '''# Get Tiempo\n
        Devuelve la lista completa de Tiempos generada en el metodo de velocidad_media() '''
        vel,tiemp,altur=Gens.velocidad_media()
        return tiemp
    
    @staticmethod    
    def getAltura():
        '''# Get Altura\n
        Devuelve la lista completa de Alturas generada en el metodo de velocidad_media() '''
        vel,tiemp,altur=Gens.velocidad_media()
        return altur
    
    @staticmethod
    def velocidadMedia():
        '''# Velocidad Media\n
        Devuelve una lista str de las velocidades medias con su error '''
        ve = []
        ''' Iniciacion de la lista '''
        velocidades, temps, ys = Gens.velocidad_media()
        ''' "Importacion" de los datos '''
        for element in velocidades:
            ve.append(str(element/100)+"+-"+str(op.error(ys,temps)))
            ''' Se añade el error a cada velocidad media '''
        '''* Devuelce la lista con las velocidades y el error *'''
        return ve


    @staticmethod
    def acceleracion_media():
        '''# Aceleracion_Media\n
        - Genera una lista de Aceleraciones sin asignar error '''
        acceleraciones=[]
        arry_velocidades,arry_tiempo, a = Gens.velocidad_media(Gens.gen_altura(3.5), Gens.gen_tiempo(55,30))
        ''' "Importacion" de datos '''
        x=0
        acc = 0
        while x<len(arry_tiempo):
            x+=1
            try:
                '''Manejo de Excepciones Conocidas '''
                acc=arry_velocidades[x+1]-arry_velocidades[x]/fabs(arry_tiempo[x+1]-arry_tiempo[x])
                '''El valor siguiente de la lista - El valor actual / La diferencia de Tiempos '''
            except ZeroDivisionError as zde: pass #'''Es probable que el valor se acerque a 0 '''
            except IndexError as ie:
                ''' Excepcion programada, al final de la lista no existira un valor siguiente '''
                try:
                    acc=arry_velocidades[0]-arry_velocidades[x-1]/fabs(arry_tiempo[x-2]-arry_tiempo[x-1])
                    ''' Por lo que puede generar un dato con el valor anterior '''
                except ZeroDivisionError as zde: pass #'''Es probable que el valor se acerque a 0 '''
            except Exception as e:
                ''' En caso de que ocurra una excepcion desconocida habrá que imprimirla y manejarla '''
                print("Uncontrolled Exception....",e)
                acc=arry_velocidades[0]-arry_velocidades[x-1]/fabs(arry_tiempo[x-2]-arry_tiempo[x-1])
            acceleraciones.append(acc)
            '''Agregar el valor a la lista general de aceleraciones '''
        ''' Devolver la lista '''
        return acceleraciones
    
    @staticmethod
    def aceleracionMedia():
        '''# Aceleracion Media\n
        Devuelve cada aceleracion con su error'''
        ac = []
        ''' Iniciacion de la lista de datos '''
        acc = Gens.acceleracion_media()
        vel, temps, ys = Gens.velocidad_media(Gens.gen_altura(3.5),Gens.gen_tiempo(55,30))
        ''' "Importacion" de datos '''
        for element in acc:
            ac.append(str(element/10000)+"+-"+str(op.error(vel,temps)))
            ''' Se añade el error a cada aceleracion media '''
        '''* Devuelve la lista de datos *'''
        return ac
        
    @staticmethod
    def velocidad_Caudal():
        caudal = []
        ''' Iniciacion de la lista de datos a devolver '''
        alturas = Gens.gen_altura(7)
        ''' Generación de la lista de alturas '''
        for i in range(0,len(alturas)):
            H = 21 - alturas[i]
            caudal.append(str(op.torricelliEq(H)/100))
            ''' Se agrega a la lista el dato generado con la altura correspondiente de la lista '''
        '''* Devuelve la lista de datos *'''
        return caudal
    
    @staticmethod
    def velocidadCaudal():
        '''# Velocidad Caudal\n
        Devuelve la lista de datos calculando el caudal usando la equacion de Torricelli y asignando error'''
        caudal = []
        vels = Gens.velocidad_Caudal()
        '''Importamos velocidad'''
        alturas = Gens.gen_altura(7)
        '''Generamos lista de alturas '''
        for i in range(0,30):
            H = 21 - alturas[i]
            '''Asignamos la altura 'H' necesaria '''
            s=vels[i]+"+-"+str(op.caudalError(alturas))
            '''Asignamos el error a cada altura y lo agregamos a la lista general '''
            caudal.append(s)
        ''' Devolvemos la lista '''
        return caudal
    
    @staticmethod
    def kinectic():
        '''# Energía Cinética\n
         Devuelve una lista de energías Cinéticas en los puntos'''
        k = []
        ''' Iniciacion de lista a devolver '''
        vCaudal = Gens.velocidad_Caudal()
        vels,temps,h = Gens.velocidad_media()
        error = op.energiaKError(vCaudal,vels)
        ''' "Importacion" de Datos '''
        for element in vCaudal:
            k.append(str(op.energiaK(element))+"+-"+str(error))
            ''' Se agrega a la lista el dato generado con su error '''
        '''* Devuelve la lista de datos *'''
        return k

             


            

        
    








    