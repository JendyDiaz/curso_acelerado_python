'''
*********** Curso de programacion acelerado de Python*********** 
Date 07-10-2022

File: Sesion2/ejercicio17.py
Autor: Jendy Diaz
Action: Ingresar un valor del 1-10 y muestrar la tabla de multiplicar del mismo.
'''
n = int(input("Introduce un numero: "))
for f in range(1,13):
	multiplicacion = n * f 
	print(f'n x {f} = {multiplicacion}') 