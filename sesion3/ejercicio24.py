'''
*********** Curso de programacion acelerado de Python*********** 
Date 09-10-2022

File: Sesion2/ejercicio24.py
Autor: Jendy Diaz
Action: Diccionario.
'''

persona = {}
continuar = True
while continuar:
  clave = input('¿Qué dato quieres introducir? ')
  valor = input(clave + ': ')
  persona[clave] = valor
  print(persona)
  continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
  