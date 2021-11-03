import random
numero=random.randint(0,99)
intento=int(input("Por favor introduzca un numero entre 0 y 99: "))
intentosrealizados=0
while intento != numero:
    if intento<0 or intento>99:
        print("El numero escogido no es valido")
        intentosrealizados=intentosrealizados+1
        intento=int(input("Por favor introduzca un nuevo numero: "))
    if numero>intento:
        print("El numero escogido es demasiado pequeño")
        intentosrealizados=intentosrealizados+1
        intento=int(input("Por favor introduzca un nuevo numero: "))
    if numero<intento:
        print("El numero escogido es demasiado grande")
        intentosrealizados=intentosrealizados+1
        intento=int(input("Por favor introduzca un numero nuevo: "))
if intento == numero:
    print("¡Has ganado!")
    intentosrealizados=intentosrealizados+1
    print("el numero era el", numero)
    print("has necesitado", intentosrealizados, "intentos")