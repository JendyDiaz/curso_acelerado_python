'''
*********** Curso de programacion acelerado de Python*********** 
Date 09-10-2022

File: Sesion2/ejercicio19.py
Autor: Jendy Diaz
Action: Palindomio
'''

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
  print("Es un palíndromo")
else:
  print("No es un palíndromo")


'''
str="LearnPython"

length_str=len(str)

sliced_str=str[length_str::-1] 
print ("The sliced string is:",sliced_str)
'''


