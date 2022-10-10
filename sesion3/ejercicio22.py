'''
*********** Curso de programacion acelerado de Python*********** 
Date 09-10-2022

File: Sesion2/ejercicio22.py
Autor: Jendy Diaz
Action: Loteria.
'''

list=[]
for i in range(6):
  list.append(int(input('Ingrese número ganador: ')))
list.sort()
print('Números ganadores: ')
print(*list, sep=', ')
