'''##Gens
Clase Estatica para generar datos e.e '''
import random
import Operations.MathOp as op
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
        return Gens.generateData(promalt,30)
    
    @staticmethod 
    def gen_tiempo(data,num):
        lista = []
        for i in range(0,num):
            lista.append(int(random.randint(data-1,data+3)))
            ''' Agrega a la lista un numero aleatorio del dato + una variacion entre 0.1 y 0.6 '''
        '''* Regresa la lista *'''
        return lista

    @staticmethod
    def velocidad_media():
        velocidades=[]
        tiempo=[111,112,113,111,112,110,116,110,112,110,109,112,111,108,109,111,112,110,113,112]
        tiempos=Gens.gen_tiempo(110,10)
        altura=Gens.gen_altura(7)
        for elements in tiempos:
            tiempo.append(elements)
        for i in range(0,len(tiempo)):
            v=altura[i]/tiempo[i]
            velocidades.append(v)
        return velocidades,tiempo,altura
    
    @staticmethod
    def velocidadMedia():
        '''# Velocidad Media\n
        Devuelve una lista str de las velocidades medias con su error '''
        ve = []
        ''' Iniciacion de la lista '''
        velocidades, temps, ys = Gens.velocidad_media()
        ''' "Importacion" de los datos '''
        for element in velocidades:
            ve.append(str(element)+"+-"+str(op.error(ys,temps)))
            ''' Se añade el error a cada velocidad media '''
        '''* Devuelce la lista con las velocidades y el error *'''
        return ve


    @staticmethod
    def acceleracion_media():
        acceleraciones=[]
        arry_velocidades,arry_tiempo, a=Gens.velocidad_media()
        x=0
        while x<len(arry_tiempo):
            try:
                x+=1
                acc=arry_velocidades[x+1]-arry_velocidades[x]/fabs(arry_tiempo[x+1]-arry_tiempo[x])
            except IndexError as ie:
                acc=arry_velocidades[0]-arry_velocidades[x-1]/fabs(arry_tiempo[x-2]-arry_tiempo[x-1])
            except ZeroDivisionError as zde: pass
            except Exception as e:
                print("Uncontrolled Exception....",e)
                acc=arry_velocidades[0]-arry_velocidades[x-1]/fabs(arry_tiempo[x-2]-arry_tiempo[x-1])
            acceleraciones.append(acc)
        return acceleraciones
    
    @staticmethod
    def aceleracionMedia():
        '''# Aceleracion Media\n
        Devuelve cada aceleracion con su error'''
        ac = []
        ''' Iniciacion de la lista de datos '''
        acc = Gens.acceleracion_media()
        vel, temps, ys = Gens.velocidad_media()
        ''' "Importacion" de datos '''
        for element in acc:
            ac.append(str(element)+"+-"+str(op.error(vel,temps)))
            ''' Se añade el error a cada aceleracion media '''
        '''* Devuelve la lista de datos *'''
        return ac
        
    @staticmethod
    def velocidadCaudal():
        '''# Velocidad Caudal\n
        Devuelve la lista de datos calculando el caudal usando la equacion de Torricelli y asignando error'''
        caudal = []
        ''' Iniciacion de la lista de datos a devolver '''
        alturas = Gens.gen_altura(7)
        ''' Generación de la lista de alturas '''
        for i in range(0,len(alturas)):
            H = 21 - alturas[i]
            caudal.append(str(op.torricelliEq(H))+"+-"+str(op.caudalError(alturas)))
            ''' Se agrega a la lista el dato generado con la altura correspondiente de la lista '''
        '''* Devuelve la lista de datos *'''
        return caudal
    
    @staticmethod
    def kinectic():
        '''# Energía Cinética\n
         Devuelve una lista de energías Cinéticas en los puntos'''
        k = []
        ''' Iniciacion de lista a devolver '''
        vCaudal = Gens.velocidadCaudal()
        vels,temps,h = Gens.velocidad_media()
        error = op.energiaKError(vCaudal)
        ''' "Importacion" de Datos '''
        for element in vCaudal:
            k.append(str(op.energiaK(element))+"+-"+str(error))
            ''' Se agrega a la lista el dato generado con su error '''
        '''* Devuelve la lista de datos *'''
        return k

             


            

        
    








    