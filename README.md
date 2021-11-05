# adivina-el-numero

Mi direccion de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/jzazooro/adivina-el-numero.git)
https://github.com/jzazooro/adivina-el-numero.git

Hemos resuelto un juego de adivinar un numero aleatorio entre 0 y 99.
El diagrama de flujo que tenemos en nuestro codigo es el siguiente: 

![diagrama de flujo adivine el numero](/jzazooro/divina-el-numero/2.2DIAGRAMADEFLUJOADIVINAELNUMERO.jpeg)
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
