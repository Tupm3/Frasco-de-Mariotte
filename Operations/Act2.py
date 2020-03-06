import matplotlib.pyplot as p
from Operations.MathOp import MathOp
from csv import writer, QUOTE_MINIMAL
from math import sqrt
import os
from DB import *
class Act2(MathOp):
    ''' # MathOpExtension\n
    - Clase con Métodos para la Actividad 2 del Experimento\n
    Notas:\n
    - Hereda de MathOp'''
    Aout = 1
    Ain = 0
    Ah = 0
    g =9.81
    tiempos = []
    cmA2 = []
    Hagua = []
    hPopote = []

    @staticmethod
    def import_Data():
        '''# Hi'''
        path = os.getcwd()
        resultPath = path+"\DB"
        os.chdir(resultPath)
        with open("tiemposA2.txt","r") as f: 
            for element in f.readlines(): 
                Act2.tiempos.append(float(element))
        with open("cmA2.txt","r") as f: 
            for element in f.readlines(): 
                Act2.cmA2.append(float(element))
        with open("Hagua.txt","r") as f: 
            for element in f.readlines(): 
               Act2.Hagua.append(float(element))
        with open("hPopote.txt","r") as f: 
            for element in f.readlines(): 
                Act2.hPopote.append(float(element))
        os.chdir(path)

    @staticmethod
    def minimos_cuadrados(lx,ly):
        '''# Minimos Cuadrados\n
        Metodo invocable para obtener minimos cuadrados de dos listas.\n
        Requiere:\n
        - Lista de Valores lx
        - Lista de Valores ly\n
        Notas:\n
        - Ambas listas deben tener la misma cantidad de elementos'''
        s1 = 0
        sx = 0
        sx2 = 0
        sy = 0
        '''Iniciacion de Variables de:
        - Sumatoria de xiyi
        - Sumatoria de valores en lx
        - Sumatoria del cuadrado de cada valor en lx
        - Sumatoria de valores en ly'''
        for i in range(0,len(lx)):
            '''Ciclo For de Sumatoria de valores'''
            s1 += lx[i]*ly[i]
            '''Sumatoria de xiyi'''
            sx += lx[i]
            '''Sumatoria de valores en x'''
            sy += ly[i]
            '''Sumatoria de valores en y'''
            sx2 += lx[i]*lx[i]
            '''Sumatoria del cuadrado de los valores en x'''
        num = s1 - ((1/len(lx))*(sx)*(sy))
        '''Numerador de la formula de minimos cuadrados en la forma:
            sumatoria(xiyi) - (1/n)*(sumatoria(xi) * (sumatoria(yi))) '''
        den = sx2 - ((1/len(lx))* sx * sx)
        '''Denominador de la formula de minimos cuadrados en la forma:
            sumatoria(xi^2) - (1/n)*(sumatoria(xi)^2)'''
        minimosCuadrados = num/den
        '''Aplicacion de la formula'''
        '''Regresa el valor obtenido'''
        print("Minimos Cuadrados")
        print("-"*57)
        print("Numerador: ",num)
        print("Denum: ",den)
        print("Minimos Cuadrados: ",minimosCuadrados)
        print("-"*57)
        return minimosCuadrados

    @staticmethod
    def B0(x,y,B1):
        '''# Beta 0\n
        Encuentra la variable con la forma:\n
        B0 = promY - (Beta1 * promX)'''
        py = Act2.promedio(y)
        '''Promedio de Y'''
        px = Act2.promedio(x)
        '''Promedio de X'''
        b0 = py - (B1*px)
        '''Aplicacion de la formula'''
        '''Regresa el calculo'''
        return b0

    @staticmethod
    def plot_graph(lx,ly,graph,xName = "X",yName = "Y"):
        try:
            path = os.getcwd()
            resultPath = path+"\Resultados"
        except Exception as e: pass
        '''# Plot Graph\n
        Metodo invocable para graficar datos y guardarlos'''
        plt = p
        plt.xlabel(xName)
        '''Nombre del eje X'''
        plt.ylabel(yName)
        '''Nombre del eje Y'''
        plt.plot(lx,ly)
        '''Grafica'''
        name = "Grafica_{}.png".format(graph)
        plt.savefig(name)
        plt.clf()
        '''Exportacion de la grafica'''
        print("Gráfica "+name+" exportada...")
    
    @staticmethod    
    def Mediciones():
        '''# Medicion de Datos
        Genera la medición de H y genera las gráficas correspondientes'''
        path = os.getcwd()
        resultPath = path+"\Resultados"
        os.chdir(resultPath)
        '''Primera Medicion'''
        file = "Vh_CSV.csv"
        aIndex = 0
        fIndex = 10
        rep = 0
        hList = []
        vhlist = []
        print("##PRIMERA MEDICION##") 
        print("="*57)
        for i in range(0,5):
            print("Repeticion #"+str(i+1))
            print("-"*57)
            print("-"*57)
            times = Act2.tiempos[aIndex:fIndex]
            b1 = Act2.minimos_cuadrados(times,Act2.Hagua[aIndex:fIndex])
            b0 = Act2.B0(times,Act2.Hagua[aIndex:fIndex],b1)
            print("B0: "+str(b0))
            print("B1: "+str(b1))
            for c in range(0,10):
                hList.append(b0+(b1*times[c]))
                print("Time: "+str(times[c])+" "*10,end="")
                print("h: "+str(b0+(b1*times[c]))+" cm")
            vhlist.append(b1)
            rep += 1
            graphName = "h_Repeticion"+ str(rep)
            Act2.plot_graph(times,Act2.Hagua[aIndex:fIndex],graphName,"Tiempos","Alturas")
            print("-"*57)
            aIndex += 10
            fIndex += 10
        # print(Act2.Hagua)
        # print(Act2.tiempos)
        print("##SEGUNDA MEDICION##")
        print("-"*57)
        squaredh = []
        times2 = []
        squaredT = []
        aIndex = 0
        fIndex = 10
        for element in Act2.Hagua:
            squaredh.append(element*element)
        for clock in Act2.tiempos:
            squaredT.append(clock*clock)
        for s in range(0,5):
            print("Repeticion #"+str(s+1))
            print("-"*57)
            print("-"*57)
            times2 = squaredh[aIndex:fIndex]
            b1 = Act2.minimos_cuadrados(Act2.hPopote,vhlist)
            b0 = Act2.B0(Act2.hPopote,vhlist,b1)
            print("B0: "+str(b0))
            print("B1: "+str(b1))
            Vh2 = b0 + (b1 * Act2.hPopote[s])
            print("Vh2: ",Vh2)
            print("-"*57)
        print("**END**")
        os.chdir(path)