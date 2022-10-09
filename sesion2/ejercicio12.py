'''
*********** Curso de programacion acelerado de Python*********** 
Date 07-10-2022

File: Sesion2/ejercicio12.py
Autor: Jendy Diaz
Action: estructura condicional anidada.
'''

mes = int(input("Introduzca el mes de año: "))

if 1 <= mes <= 12:
  print("Se ha introducido un mes válido.")
else:
  print("El mes es incorrecto. Por defecto se elige Enero.")

mes = 1

print("Se utilizará mes", mes)