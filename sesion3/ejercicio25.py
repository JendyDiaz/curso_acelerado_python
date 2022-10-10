'''
*********** Curso de programacion acelerado de Python*********** 
Date 09-10-2022

File: Sesion2/ejercicio25.py
Autor: Jendy Diaz
Action: Diccionario.
'''

diccionario = {}
words = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in words.split(','):
    key, value = i.split(':')
    diccionario[key] = value
phrase = input('Introduce una frase en español: ')
for i in phrase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')