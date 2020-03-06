import matplotlib as p
from Operations.MathOp import MathOp
from math import sqrt
import os
class Act2(MathOP):
    ''' # MathOpExtension\n
    - Clase con Métodos para la Actividad 2 del Experimento\n
    Notas:\n
    - Hereda de MathOp'''
    Aout = 1
    Ain = 0
    Ah = 0
    g =9.81
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
        def plot_graph(lx,ly,graph,xName = "X",yName = "Y"):
            p.plot(lx,ly)
            p.xlabel(xName)
            p.ylabel(yName)
            name = "Grafica_{}.png".format(graph)
            p.savefig(name)
        
        @staticmethod
        def gravedad(H):
            Vh = -(Aout/Ah) * sqrt(2*g*H)

    print("x")
