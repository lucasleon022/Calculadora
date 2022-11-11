############################################
# Primer commit main Calculadora
# *Subir a Github
# *Index.py
# Ejecutable.exe
# Release: 11/11/2022
# Developer: Lucas Leon
###########################################

number = int(input("ingresa un numero"))
numberr = int(input("ingresa otro numero"))

eleccion = 0

while eleccion != 6:
    print("""
    indique la operacion a realizar:
    1) suma
    2) resta
    3) multiplicacion
    4) divicion
    5) cambio de valores
    6) salir
    """)

    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("resultado: ", number, "+", numberr, "=", number+numberr)

    if eleccion == 2:
        print(" ")
        print("resultado: ", number, "-", numberr, "=", number-numberr)

    if eleccion == 3:
        