n1 = input("Ingresa primer numero")
n2 = input("Ingresa segundo numero")

n1 = int(n1) #convierte el string a un numero
n2 = int(n2) #convierte el string a un numero

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
El resultado de la suma es {suma}.
El resultado de la resta es {resta}.
El resultado de la multiplicacion es {multi}.
El resultado de la division es {div}.
"""

print(mensaje)