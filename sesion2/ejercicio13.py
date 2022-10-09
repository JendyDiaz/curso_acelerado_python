'''
*********** Curso de programacion acelerado de Python*********** 
Date 07-10-2022

File: Sesion2/ejercicio13.py
Autor: Jendy Diaz
Action: Suma de 10 primeros numeros
'''

def sumaDigitos(num):
    s = 0
    while num > 0:
      s = s + num %10
      num = num//10
      return s

n = 10
sumaT = 0
while n > 0:
  num = int(input("Numero:"))
  sumaT = sumaT + sumaDigitos(num)
  n = n-1
  print(sumaT)
