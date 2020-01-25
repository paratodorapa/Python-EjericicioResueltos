#Paso 1 - Ingreso de datos
ingreso_a = ""
ingreso_b = ""
num_a = 0
num_b = 0
vec_a = []
vec_b = []
sum_a = 0
sum_b = 0

#La funcion input convierte el ingreso del usuario a string
ingreso_a = input("Ingrese un numero")
ingreso_b = input("Ingrese otro numero")

#La funcion int para convertir de string a int
num_a = int(ingreso_a)
num_b = int(ingreso_b)

#NO HACER COMPOSICION, num_a = int(input("Ingrese un numero")

#Paso 2 - Divisiores
def divisores(num):
    vec = []
    for i in range(1, num):
        if num % i == 0:
            vec.append(i)
    return vec

vec_a = divisores(num_a)
vec_b = divisores(num_b)

#Paso 3 - Sumatorias
def sumatoria(vec):
    sumatoria = 0
    for c in vec:
        sumatoria = sumatoria + c
    return sumatoria

sum_a = sumatoria(vec_a)
sum_b = sumatoria(vec_b)

#Paso 4 - Son amigos?
if sum_b == num_a and sum_a == num_b:
    print("Son amigos")
else:
    print("No son amigos")
