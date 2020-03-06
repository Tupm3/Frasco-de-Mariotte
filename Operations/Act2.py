import matplotlib as p
from Operations.MathOp import MathOp
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
        path = os.getcwd()
        resultPath = path+"\DB"
        os.chdir(resultPath)
        with open("tiemposA2.txt","r") as f: 
            for element in f.readlines(): tiempos.append(float(element))
        with open("cmA2.txt","r") as f: 
            for element in f.readlines(): cmA2.append(float(element))
        with open("Hagua.txt","r") as f: 
            for element in f.readlines(): Hagua.append(float(element))
        with open("hPopote.txt","r") as f: 
            for element in f.readlines(): hPopote.append(float(element))


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
        return minimosCuadrados

        @staticmethod
        def B0(x,y,B1):
            '''# Beta 0\n
            Encuentra la variable con la forma:\n
            B0 = promY - (Beta1 * promX)'''
            py = super().promedio(y)
            '''Promedio de Y'''
            px = super().promedio(x)
            '''Promedio de X'''
            B1 = minimosCuadrados(x,y)
            '''Beta 1 con minimos cuadrados'''
            b0 = py - (B1*px)
            '''Aplicacion de la formula'''
            '''Regresa el calculo'''
            return b0

        @staticmethod
        def plot_graph(lx,ly,graph,xName = "X",yName = "Y"):
            '''# Plot Graph\n
            Metodo invocable para graficar datos y guardarlos'''
            p.xlabel(xName)
            '''Nombre del eje X'''
            p.ylabel(yName)
            '''Nombre del eje Y'''
            p.plot(lx,ly)
            '''Grafica'''
            name = "Grafica_{}.png".format(graph)
            p.savefig(name)
            '''Exportacion de la grafica'''
            print("Gráfica "+name+" exportada...")
        
        @staticmethod
        def Vh():
            aIndex = 0
            fIndex = 10
            rep = 0
            for i in range(0,10):
                H = hPopote[rep]
                b1 = minimos_cuadrados(tiempos[aIndex:fIndex],Hagua)
                b0 = B0(tiempos[aIndex:fIndex],Hagua,b1)
                Vh = b0 + b1*H
                aIndex += 10
                fIndex += 10
                rep += 1
                print(Vh)
                print("-"*57)
            print("**END**")

Vh()

