from random import randint
import math 
import random

funct_y=[0.0798,0.7741,0.1221,0.4388,1.0291,0.1070,-0.1179,0.3997,-0.4426,-0.7845,0.0568,-0.2774,-0.5127,0.5686,0.5437,0.0548,0.8502,0.7436,-0.2100,0.1904,0.1803]
funct_x=[0.0000,0.2500,0.5000,0.7500,1.0000,1.2500,1.5000,1.7500,2.0000,2.2500,2.5000,2.7500,3.0000,3.2500,3.5000,3.7500,4.0000,4.2500,4.5000,4.7500,5.0000]
param_ab=[]
minu=[]
res_func=[] #Guarda los resultados de la funcion
res_fit=[] #Guarda el fit
bestfit = []


POBLACION=10 
res_sum=0 #La suma de todas las respuestas de la funcion


#
# [1,3],[23,59],[2,5],[]
#
def selection(params_gen):
    #primero sacamos el resultado de la funcion y despues el fitness
    generation_function=[]
    the_best_gene=[]
    for prob in params_gen:  #[2,2]
        aux=[]
        for z in funct_x: #x desma
            var = fitProbability(z,prob[0],prob[1])
            aux.append(round(var,4))
        fit = fitnessCal(aux)
        fit = abs(fit)
        generation_function.append([aux,fit,prob])

    for da in generation_function:
        if len(the_best_gene) == 0 or len(the_best_gene)==1 :
            the_best_gene.append(da[2])
        else:
            for index in range(len(the_best_gene)):
                if da[1] < the_best_gene[index][1]:
                    the_best_gene[index]=da[2]
                    break
    return the_best_gene

    return generation_function

def fitnessCal(datas):
    valor=0
    for dato in datas:
        valor +=dato
    return valor/len(datas)

def fitProbability(num,a,b):
    convert_radians_a=math.radians(a*num*0.1)
    convert_radians_b = math.radians(b*num*0.1)
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
   
def int_to_bin(value):
    binary="{0:06b}".format(value)
    return [int(x) for x in str(binary)]

def _generate_params():
    aux=[]
    aux.append(randint(1,59))
    aux.append(randint(1,59))
    param_ab.append(aux)

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
        

if __name__ == "__main__":
    for _ in range(4):
        _generate_params()
    print(param_ab)
    auc = selection(param_ab)
    print("---",auc)
    das= []
    for aus in auc:
        da = []
        for a in aus:
            da.extend(int_to_bin(a))
        das.append(da)
    print(das)
    cross_data = crossover(das)
    print(cross_data)
    muta_data = mutation(cross_data)
    print(muta_data)
    new = tranform_bin_int(muta_data)
    auc.extend(new)
    print(auc)

    