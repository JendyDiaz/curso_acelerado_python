'''
*********** Curso de programacion acelerado de Python*********** 
Date 07-10-2022

File: Sesion1/ejercicio3.py
Autor: Jendy Diaz
Action: imprime capital obtenido de una inversión
'''

cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
capital_final = round(cantidad * (interes / 100 + 1)**años, 2)

print("Capital final es: ", capital_final) 