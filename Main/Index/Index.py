############################################
# Primer commit main Calculadora
# *Subir a Github
# *Index.py
# Ejecutable.exe
# Release: 11/11/2022
# Developer: Lucas Leon
###########################################

number = int(input("Ingresa un numero"))
numberr = int(input("Ingresa otro numero"))

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
        print("Resultado: ", number, "+", numberr, "=", number+numberr)

    if eleccion == 2:
        print(" ")
        print("Resultado: ", number, "-", numberr, "=", number-numberr)

    if eleccion == 3:
        print(" ")
        print("Resultado: ", number, "*", numberr, "=", number*numberr)

    if eleccion == 4:
        print(" ")
        print("Resultado: ", number, "/", numberr, "=", number/numberr)

    if eleccion == 5:
        number = int(input("Ingresa un numero"))
        numberr = int(input("Ingresa otro numero"))

    if eleccion == 6:
        print("Gracias por usar la calculadora. Creada por: Lucas Leon")