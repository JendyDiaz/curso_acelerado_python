'''
*********** Curso de programacion acelerado de Python*********** 
Date 07-10-2022

File: Sesion2/ejercicio8.py
Autor: Jendy Diaz
Action: Detecta numeros negativos, positivos y neutros.
'''

num= input("Escriba un número: ")
numero = float(num)
if numero == 0:
  print("Neutro")
elif numero < 0:
  print("Negativo")
elif numero > 0:
  print("Positivo")

