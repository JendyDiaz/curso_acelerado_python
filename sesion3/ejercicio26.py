'''
*********** Curso de programacion acelerado de Python*********** 
Date 09-10-2022

File: Sesion2/ejercicio26.py
Autor: Jendy Diaz
Action: Tipo de moneda.
'''

monedas = {'Euro':'€', 'Dollar':'$', 'Peso':'$'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")