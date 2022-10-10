'''
*********** Curso de programacion acelerado de Python*********** 
Date 09-10-2022

File: Sesion2/ejercicio20.py
Autor: Jendy Diaz
Action: Menor y el mayor de los precios.
'''

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
  if price < min:
    min = price
  elif price > max:
    max = price
    
print("El mínimo es " + str(min))
print("El máximo es " + str(max))

listSum = sum(prices)
print(f"Sum of list -> {listSum}")