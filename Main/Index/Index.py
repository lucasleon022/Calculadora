############################################
# Primer commit main Calculadora
# *Subir a Github
# *Index.py
# Ejecutable.exe
# Release: 11/11/2022
# Developer: Lucas Leon
###########################################

import math 

numero = float(input("Ingresa un numero"))
numeroo = float(input("Ingresa otro numero"))

eleccion = 0

while eleccion != 7:
    print("""
    Indique la operacion a realizar:
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Cambio de valores
    6) Seguir calculando
    7) Salir
    """)

    eleccion = float(input())

    if eleccion == 1:
        print(" ")
        print("Resultado: ", numero, "+", numeroo, "=", numero+numeroo)
        resultado = numero+numeroo

    if eleccion == 2:
        print(" ")
        print("Resultado: ", numero, "-", numeroo, "=", numero-numeroo)
        resultado = numero-numeroo

    if eleccion == 3:
        print(" ")
        print("Resultado: ", numero, "*", numeroo, "=", numero*numeroo)
        resultado = numero*numeroo

    if eleccion == 4:
        print(" ")
        print("Resultado: ", numero, "/", numeroo, "=", numero/numeroo)
        resultado = numero/numeroo

    if eleccion == 5:
        numero = float(input("Ingresa un numero"))
        numeroo = float(input("Ingresa otro numero"))

    if eleccion == 6:
        numero = resultado
        print(numero)
        numeroo = float(input("Ingrese nuevo valor"))

    if eleccion == 7:
        print("Gracias por usar la calculadora. Creada por: Lucas Leon")    