from random import randint
import math 
import random

funct_y=[0.0798,0.7741,0.1221,0.4388,1.0291,0.1070,-0.1179,0.3997,-0.4426,-0.7845,0.0568,-0.2774,-0.5127,0.5686,0.5437,0.0548,0.8502,0.7436,-0.2100,0.1904,0.1803]
funct_x=[0.0000,0.500,0.5000,0.7500,1.0000,1.2500,1.5000,1.7500,2.0000,2.2500,2.5000,2.7500,3.0000,3.2500,3.5000,3.7500,4.0000,4.2500,4.5000,4.7500,5.0000]
param_ab=[]
param_ab_bin=[]
res_func=[] #Guarda los resultados de la funcion
res_fit=[] #Guarda el fit de cada uno en una lista
best = [] #Guarda los 5 mejores individuos. 
POBLACION=10 
res_sum=0 #La suma de todas las respuestas de la funcion


def seleccion():
    pass

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
            print(corte)
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
            

def searchInfo():
    ObtenerPoblacion() #Se obtienen los resultados y se agregan a una lista. 
    getFit() #Se genera una lista con el fit de cada uno de los resultados. 

def getMenor():
    pass
    #for i in res_fit:
           
def getFit():
    for i in res_func:
        e = i / res_sum
        res_fit.append(e) #Aqui se agrega el fit de cada uno a una lista
    print(res_fit)

def ObtenerPoblacion():
    global res_sum
    indice = random.randint(0, len(funct_x)-1) #Obtiene un numero aleatorio entre 0 y el final del arreglo
    print("INDICE "+str(indice))
    x = funct_x[indice]
    for i in range(POBLACION):
        a =  random.uniform(0.1, 5.9)
        b =  random.uniform(0.1, 5.9)
        res_func.append(funcionEjecutada(x,a,b)) #Guarda los resultados de la funcion en una lista
    res_sum=sum(res_func) #Suma de todos los resultados. 
   
## Esta función recibe los parametros para ejecutar los resultados.         
def funcionEjecutada(num,a,b):
    resultado = float(math.cos(a*num)*math.sin(b*num))
    return resultado

#
# Transforma los valores enteros a binarios dentro de un arreglo
#
def int_to_bin(value):
    binary="{0:06b}".format(value)
    return [int(x) for x in str(binary)]
#
# Crea los parametros del rango 1-59
#
def _generate_params():
    param_ab.append(randint(1,59))
    param_ab.append(randint(1,59))
    param_ab_bin.append(int_to_bin(param_ab[0]))
    param_ab_bin.append(int_to_bin(param_ab[1]))

if __name__ == "__main__":
    _generate_params()
    print(param_ab)
    #print(param_ab_bin)
    # Iniciamos el proceso de seleccion
    #seleccion(array)
    #print(crossover([[0,1,1,0,1,0],[1,0,1,0,1,1]]))
    ObtenerPoblacion()