from random import randint

funct_y=[]
funct_x=[]
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
