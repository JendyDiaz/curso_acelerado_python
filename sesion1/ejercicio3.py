'''
*********** Curso de programacion acelerado de Python*********** 
Date 07-10-2022

File: Sesion1/ejercicio3.py
Autor: Jendy Diaz
Action: Pago del trabajador
'''

horas = float(input("Introduce tus horas de trabajo"))
coste = float(input("Introduce lo que cobras por hora:"))
horas_extras = float(input("Introduce las horas extras:"))
paga = (horas*coste)+(horas_extras*coste)
print("Tu paga es",paga)
