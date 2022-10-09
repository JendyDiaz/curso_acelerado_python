'''
*********** Curso de programacion acelerado de Python*********** 
Date 07-10-2022

File: Sesion2/ejercicio15.py
Autor: Jendy Diaz
Action: Suma valores ingresados por teclado.
'''

n = 10
suma = 0
i = 1
while (i <= 10):
  print("Ingrese valor :",i)
  nota = float(input())
  suma = suma + nota
  i+=1
  promedio = suma / 10
  print("La suma es",suma)
  print("El promedio es:", promedio)
