'''##Gens
Clase Estatica para generar datos e.e '''
import random
import Operations.MathOp as op
'''Importacion de la libreria random'''
class Gens:
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
        velocidades, temps, ys = Gens.velocidad_media
        ''' "Importacion" de los datos '''
        for element in velocidades:
            ve.append(str(element)+"+-"+op.error(ys,temps))
            ''' Se añade el error a cada velocidad media '''
        '''* Devuelce la lista con las velocidades y el error *'''
        return ve


    @staticmethod
    def acceleracion_media():
        acceleraciones=[]
        estado=0
        arry_velocidades,arry_tiempo, a=Gens.velocidad_media()
        x=0
        while x<len(arry_tiempo):
            try:
                x+=1
                acc=arry_velocidades[x+1]-arry_velocidades[x]/arry_tiempo[x+1]-arry_tiempo[x]
            except IndexError as ie:
                acc=arry_velocidades[0]-arry_velocidades[x]/arry_tiempo[0]-arry_tiempo[x]
            except Exception as e:
                print("Uncontrolled Exception....",e)
                acc=arry_velocidades[0]-arry_velocidades[x]/arry_tiempo[0]-arry_tiempo[x]
            acceleraciones.append(acc)
        return acceleraciones
    
    @staticmethod
    def aceleracionMedia():
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
        Devuelve la lista de datos calculando el caudal usando la equacion de Torricelli'''
        caudal = []
        ''' Iniciacion de la lista de datos a devolver '''
        alturas = Gens.gen_altura(7)
        ''' Generación de la lista de alturas '''
        for i in range(0,len(alturas)):
            H = 21 - alturas[i]
            caudal.append(str(op.torricelliEq(H))+"+-"+op.caudalError(alturas))
            ''' Se agrega a la lista el dato generado con la altura correspondiente de la lista '''
        '''* Devuelve la lista de datos *'''
        return caudal
        
             


            

        
    








    