'''
*********** Curso de programacion acelerado de Python*********** 
Date 09-10-2022

File: Sesion2/ejercicio18.py
Autor: Jendy Diaz
Action: Autorizacion.
'''

personas_autorizadas = ["Alberto", "Carmen"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
  print("Está autorizado")
else:
  print("No está autorizado")