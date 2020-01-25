#Paso 1 - Ingreso de datos

ingreso_a = 0
ingreso_b = 0
num_a = 0
num_b = 0
vec_a = []
vec_b = []
sum_a = 0
sum_b = 0

#La funcion input convierte el ingreso del usuario a string
ingreso_a = input("Ingrese un numeros")
ingreso_b = input("Ingrese otro numero")

#Puedo convertir de string a int con la funcion int
num_a = int(ingreso_a)
num_b = int(ingreso_b)

#NO HACER, num_a= int(input("ingreso de datos"))

#Paso 2 - Divisores
for i in range(1, num_a):
    if num_a % i == 0:
        vec_a.append(i)

for i in range(1, num_b):
    if num_b % i == 0:
        vec_b.append(i)

# Paso 3 - Sumatoria
for k in vec_a:
    sum_a = sum_a + k

for k in vec_b:
    sum_b = sum_b + k

#Paso 4
if sum_b == num_a and sum_a == num_b:
    print("Son amigos")
else:
    print("No son amigos")

