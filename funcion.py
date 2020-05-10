from random import randint
import math 
import random
import matplotlib.pyplot as plt
import numpy as np


funct_y=[0.0798,0.7741,0.1221,0.4388,1.0291,0.1070,-0.1179,0.3997,-0.4426,-0.7845,0.0568,-0.2774,-0.5127,0.5686,0.5437,0.0548,0.8502,0.7436,-0.2100,0.1904,0.1803]
funct_x=[0.0000,0.2500,0.5000,0.7500,1.0000,1.2500,1.5000,1.7500,2.0000,2.2500,2.5000,2.7500,3.0000,3.2500,3.5000,3.7500,4.0000,4.2500,4.5000,4.7500,5.0000]
param_ab=[]
minu=[]
res_func=[] #Guarda los resultados de la funcion
gen_fit=[] #Guarda el fit
bestfit = []
gen_best_fit=[]
gen_bad_fit=[]

def selection(params_gen):
    global bestfit
    generation_function=[]
    the_best_gene=[]
    gen_pass=[]
    auxiliar=[]
    for prob in params_gen:  #[2,2]
        aux=[]
        fits =0
        ind = 0
        for z in funct_x: #x desma
            if prob[0] ==0:
                prob[0]=1
            if prob[1]==0:
                prob[1]=1
            if prob[0]>59:
                prob[0]=59
            if prob[1]>59:
                prob[1]=59
            var = fitProbability(z,prob[0],prob[1])
            fits+=(math.pow((funct_y[ind]-var),2))
            ind+=1
            aux.append(round(var,4))
        fits=fits/21
        generation_function.append([aux,fits,prob])
        auxiliar.append(fits)
    ro=0
    for da in generation_function:
        if len(the_best_gene) == 0 or len(the_best_gene) == 1:
            the_best_gene.append([da[1],da[2]])
        else:
            for s in range(len(the_best_gene)):
                if the_best_gene[s][0]> da[1]:
                    the_best_gene[s] = [da[1],da[2]]
                    break

        if ro == 0:
            ro= da[1]
        else:
            if ro < da[1]:
                ro = da[1]

    gen_bad_fit.append(ro) 

    best_fitness(generation_function)

    if the_best_gene[0][0]> the_best_gene[1][0]:
        gen_best_fit.append(the_best_gene[1][0])
    else:
        gen_best_fit.append(the_best_gene[0][0])

    for x in the_best_gene:
        gen_pass.append(x[1])
    return gen_pass

def best_fitness(muestra):
    global bestfit
    for da in muestra:
        if len(bestfit)==0 and da[1] > 0:
            bestfit.extend(da)
        else:
            if bestfit[1] > da[1] and da[1]> 0:
                bestfit = da

def fitProbability(num,a,b):
    return float(math.cos(a*num*0.1)*math.sin(b*num*0.1))

def bin_to_int(num_bin):
    letra=""
    for x in num_bin:
        letra+=str(x)
    return int(letra,2)
    
def crossover(datas):
    aux_par=[]
    aux_impar=[]
    for x in range(len(datas)):
        if x%2==0:
            corte=randint(1,len(datas[x])-2)
        aux_par.append(datas[x][0:corte])
        aux_impar.append(datas[x][corte:len(datas[x])])
    datos = []
    for y in range(len(aux_par)):#2
        aux=[]
        if y%2 == 0:#0|1
            x=y+1#1| 
        else:
            x=y-1#0
        aux.extend(aux_par[y])
        aux.extend(aux_impar[x])
        datos.append(aux)#y0a1|y1a0
    return datos

def mutation(datos):
    aux = []
    index = 0
    for x in datos:
        ans = bool(random.getrandbits(1))
        if ans:
            for y in range(len(x)):
                if bool(random.getrandbits(1)):
                    if datos[index][y] == 1:
                        datos[index][y] = 0
                    else:
                        datos[index][y] = 1
        index+=1
    return datos
   
def int_to_bin(value):
    binary="{0:06b}".format(value)
    return [int(x) for x in str(binary)]

def _generate_params(): # Poblacion inicial
   param_ab.extend([[51, 19], [23,37], [13, 43], [12, 39]])

def tranform_bin_int(param_j):
    d = []
    for x in param_j:
        ls=[]
        a = bin_to_int(x[0:6])
        ls.append(a)
        a = bin_to_int(x[6:12])
        ls.append(a)
        d.append(ls)
    return d
        
def generateGraphic(x,y,z):
    plt.plot(x, label = "Mejor Caso")   # Dibuja el gráfico
    plt.xlabel("abscisa")   # Inserta el título del eje X
    plt.ylabel("ordenada")   # Inserta el título del eje Y
    plt.ioff()   # Desactiva modo interactivo de dibujo
    plt.ion()   # Activa modo interactivo de dibujo
    plt.plot(y, label = "Peor Caso")   # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()   # Desactiva modo interactivo
    plt.ion()   # Activa modo interactivo de dibujo
    plt.plot(z, label = "Caso promedio")   # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()   # Desactiva modo interactivo
    # plt.plot(lista3)   # No dibuja datos de lista3
    plt.legend()
    plt.show()   # Fuerza dibujo de datos de lista3

def getFirstGraphic(x,y):
    plt.plot(x,label = "Real")   # Dibuja el gráfico
    plt.xlabel("abscisa")   # Inserta el título del eje X
    plt.ylabel("ordenada")   # Inserta el título del eje Y
    plt.ioff()   # Desactiva modo interactivo de dibujo
    plt.ion()   # Activa modo interactivo de dibujo
    plt.plot(y,label = "Generada")   # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()   # Desactiva modo interactivo
    # plt.plot(lista3)   # No dibuja datos de lista3
    plt.legend()
    plt.show()   # Fuerza dibujo de datos de lista3

def fitProm(x, y):
    auxs = []
    for s in range(len(x)):
        data = (x[s]+y[s])/2
        auxs.append(data)
    return auxs


if __name__ == "__main__":
    _generate_params()
    print("----",param_ab,"----")
    auc = param_ab
    for z in range(100):
        print("gen ", z)
        auc = selection(auc)
        das= []
        for aus in auc:
            da = []
            for a in aus:
                da.extend(int_to_bin(a))
            das.append(da)
        cross_data = crossover(das)
        muta_data = mutation(cross_data)
        new = tranform_bin_int(muta_data)
        auc.extend(new)

    print("la mejor seleccion: \n\n", bestfit[0])
    print("A = ",bestfit[2][0]*0.1)
    print("B = ",bestfit[2][1]*0.1)
    print("fitness", (bestfit[1])/21)
    mejor_fit=bestfit[0]
    getFirstGraphic(funct_y,mejor_fit)
    ten_best=gen_best_fit[90:]
    promedio_fit=fitProm(gen_bad_fit,gen_best_fit)
    ten_worst=gen_bad_fit[90:]
    generateGraphic(gen_best_fit,gen_bad_fit,promedio_fit)  
