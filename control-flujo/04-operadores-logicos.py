#  and, or, not

# gas = False
# encendido = True


# #Cuando se utiliza AND ambos tienen que ser true para que el resultado evalue en true
# if gas and encendido:
#     print("Puedes avanzar")
# else:
#     print("No pudes avanzar con And, ya que un valor es False")
    
# # sin importar la condicion de true o false toma el true.
# if gas or encendido:
#     print("Puedes avanzar con OR")
    
# # not lo que hace es tomar el valor y cambiarlo al opuesto
# if not gas and encendido:
#     print("Puedes avanzar con Not")
    
# si queremos podemos agregar mas variales y condicones como por ejemplo la edad

# gas = True
# encendido = True
# edad = 18

# if gas and encendido and edad > 17:
#     print("Puedes avanzar")
# else:
#     print("No pudes avanzar ya que un valor es False o eres menor de 18")
    
    
# #PRIMERO SIEMPRE SE EVALUAN LOS PARENTESIS, ahora vamos a trabajar con el elemento or

gas = False
encendido = True
edad = 18

# if not gas and (encendido or edad > 17):
#     print("Puedes avanzar")
# else:
#     print("No pudes avanzar ya que un valor es False o eres menor de 18")
    
#OPERACIONES DE CORTO CIRCUITO

if not gas and encendido and edad > 17:
    print("Puedes avanzar")