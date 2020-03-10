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
    Aout = 0.1257
    Ain = 0
    Ah = 142.7173
    g =9.81
    tiempos = []
    cmA2 = []
    Hagua = []
    hPopote = []

    @staticmethod
    def lineaAjuste(lenX,m,b = 0,initX = 0):
        '''# Linea de Ajuste'''
        lx = []
        ly = []
        for c in range(int(initX),int(lenX)+1):
            y = m*c + b
            ly.append(y)
            lx.append(c)
        return lx,ly

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
        den = sx2 - ((1/len(lx))* (sx * sx))
        '''Denominador de la formula de minimos cuadrados en la forma:
            sumatoria(xi^2) - (1/n)*(sumatoria(xi)^2)'''
        minimosCuadrados = num/den
        '''Aplicacion de la formula'''
        '''Regresa el valor obtenido'''
        print("Minimos Cuadrados")
        print("-"*57)
        print("Len X: ", len(lx))
        print("Len Y: ",len(ly))
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
    def plot_graph(lx,ly,graph,xName = "X",yName = "Y",clear = True):
        try:
            path = os.getcwd()
            resultPath = path+"\Resultados"
        except Exception as e: pass
        '''# Plot Graph\n
        Metodo invocable para graficar datos y guardarlos'''
        plt = p
        plt.title(graph)
        plt.xlabel(xName)
        '''Nombre del eje X'''
        plt.ylabel(yName)
        '''Nombre del eje Y'''
        plt.plot(lx,ly)
        '''Grafica'''
        name = "Grafica_{}.png".format(graph)
        if clear: 
            plt.savefig(name)
            plt.clf()
        '''Exportacion de la grafica'''
        print("Gráfica "+name+" exportada...")

    
    @staticmethod
    def sy(N,ly,est):
        sys = 0
        index = 0
        for element in ly:
            item = element-est[index]
            sys+= item * item
            index += 1
        result = sqrt(sys/(N-2))
        return result
    
    @staticmethod
    def incertidumbre(N,lx,ly,est):
        sy = Act2.sy(N,ly,est)
        sx2 =0
        sx = 0
        for element in lx:
            sx+=element
            sx2 += element * element
        denum = (N*sx2) - (sx*sx)
        #r = sqrt(N/denum)
        r = sqrt(sx2/denum)
        result = sy * r
        return result
    
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
        dVhlist = []
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
            print("Error de Vh: ",dVhlist)
            for c in range(0,10):
                hList.append(b0+(b1*times[c]))
                print("Time: "+str(times[c])+" "*10,end="")
                print("h: "+str(b0+(b1*times[c]))+" cm")
            rep += 1
            if rep>= 2: vhlist.append(b1)
            graphName = "h_Repeticion"+ str(rep)
            Act2.plot_graph(times,Act2.Hagua[aIndex:fIndex],graphName,"Tiempos","Alturas",False)
            nx,ny = Act2.lineaAjuste(times[len(times)-1],b1,b0)
            Act2.plot_graph(nx,ny,graphName,"Tiempos","Alturas")
            dVhlist.append(Act2.incertidumbre(len(times),times,Act2.Hagua[aIndex:fIndex],ny))
            print("-"*57)
            aIndex += 10
            fIndex += 10
        # print(Act2.Hagua)
        # print(Act2.tiempos)
        print("##SEGUNDA MEDICION##")
        print("-"*57)
        squaredVh = []
        dVh2list = []
        index = 0
        for element in vhlist:
            squaredVh.append(element * element)
            print(element)
            print(element*element)
            dVh2list.append(2*element*dVhlist[index])
            index+=1
        b1 = Act2.minimos_cuadrados(Act2.hPopote,squaredVh)
        b0 = Act2.B0(Act2.hPopote,squaredVh,b1)
        print("B0: ",b0)
        print("B1: ",b1)
        Act2.plot_graph(Act2.hPopote,squaredVh,"Vh2","H","Vh^2",False)
        nx2,ny2 = Act2.lineaAjuste(Act2.hPopote[len(Act2.hPopote)-1],b1,b0,Act2.hPopote[0])
        Act2.plot_graph(nx2,ny2,"Vh2","H","Vh^2")
        g = (b1 * (Act2.Ah * Act2.Ah))/(2 * (Act2.Aout*Act2.Aout))
        db1 = Act2.incertidumbre(len(Act2.hPopote),Act2.hPopote,squaredVh,ny2)
        print("-"*57)
        print("Gravedad: ",g)
        print("="*57)
        print("-"*57)
        print("##CALCULO DE INCERTIDUMBRES")
        print("="*57)
        print("Incertidumbres de Vh:")
        print(dVhlist)
        print("-"*57)
        print("Incertidumbres de Vh^2:")
        print(dVh2list)
        print("-"*57)
        print("Vh")
        print("="*57)
        # index = 0
        # for element in vhlist:
        #     print(str(element)+" +- "+str(dVhlist[index]))
        #     index+=1
        # print("Vh^2")
        # print("="*57)
        # for element in squaredVh:
        #     print(str(element)+" +- "+str(dVh2list[index]))
        #     index+=1
        # print("-"*57)
        print("Error de la segunda B1: ", db1)
        dAh = 1.2025
        dAout = 0.1257
        dg = (1/2) * ((2*Act2.Ah*dAout*b1*pow(Act2.Aout,-2)) + (db1*(Act2.Ah * Act2.Ah)* pow(Act2.Aout,-2)) + (2*pow(Act2.Aout,-3)*dAout*b1*(Act2.Ah * Act2.Ah)))
        print("El error de la gravedad es: ",dg)
        print("La wea con su error es: "+str(g+dg))
        print("VH")
        print("="*57)
        for element in vhlist:
            print(element)
        print("-"*57)
        print("Vh^2")
        print("="*57)
        for element in squaredVh:
            print(element)
        print("-"*57)