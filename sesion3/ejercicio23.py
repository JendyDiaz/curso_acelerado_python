'''
*********** Curso de programacion acelerado de Python*********** 
Date 09-10-2022

File: Sesion2/ejercicio23.py
Autor: Jendy Diaz
Action: Almacen de Vectores.
'''

a = (1, 2, 3)
b = (-1, 0, 2)
c = (0, 2, 1)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]*c[i]
print("El producto de los vectores" + str(a) + " y " + str(b) +  " y " + str(c) + " es " + str(product))