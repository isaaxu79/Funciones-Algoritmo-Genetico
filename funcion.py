from random import randint

funct_y=['0,0798','0,7741','0,1221','0,4388','1,0291','0,1070',-'0,1179','0,3997','-0,4426','-0,7845','0,0568','-0,2774','-0,5127','0,5686','0,5437','0,0548','0,8502','0,7436','-0,2100','0,1904','0,1803']
funct_x=['0,0000','0,2500','0,5000','0,7500','1,0000','1,2500','1,5000','1,7500','2,0000','2,2500','2,5000','2,7500','3,0000','3,2500','3,5000','3,7500','4,0000','4,2500','4,5000','4,7500','5,0000']
param_ab=[]
param_ab_bin=[]

def seleccion():
    pass
def bin_to_int():
    pass

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
    print(param_ab_bin)
    # Iniciamos el proceso de seleccion
    seleccion(array)
