############################################
# Primer commit main Calculadora
# *Subir a Github
# *Index.py
# Ejecutable.exe
# Release: 11/11/2022
# Developer: Lucas Leon
###########################################

numero = int(input("Ingresa un numero"))
numeroo = int(input("Ingresa otro numero"))

eleccion = 0

while eleccion != 6:
    print("""
    Indique la operacion a realizar:
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Cambio de valores
    6) Salir
    """)

    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("Resultado: ", numero, "+", numeroo, "=", numero+numeroo)

    if eleccion == 2:
        print(" ")
        print("Resultado: ", numero, "-", numeroo, "=", numero-numeroo)

    if eleccion == 3:
        print(" ")
        print("Resultado: ", numero, "*", numeroo, "=", numero*numeroo)

    if eleccion == 4:
        print(" ")
        print("Resultado: ", numero, "/", numeroo, "=", numero/numeroo)

    if eleccion == 5:
        numero = int(input("Ingresa un numero"))
        numeroo = int(input("Ingresa otro numero"))

    if eleccion == 6:
        print("Gracias por usar la calculadora. Creada por: Lucas Leon")