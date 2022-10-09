'''
*********** Curso de programacion acelerado de Python*********** 
Date 07-10-2022

File: Sesion2/ejercicio16.py
Autor: Jendy Diaz
Action: Imprime un triangulo.
'''

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
  for j in range(0, i):
    print("*", end="")
  print("")

