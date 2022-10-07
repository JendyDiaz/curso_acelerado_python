'''
*********** Curso de programacion acelerado de Python*********** 
Date 07-10-2022

File: Sesion1/ejercicio3.py
Autor: Jendy Diaz
Action: Indice de masa corporal, peso en kg/estatura mtrs cuadrado
'''
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))