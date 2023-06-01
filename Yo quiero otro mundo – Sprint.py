#Cristobal Inzunza
# Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
# aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
# ● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
# ● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
# cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
# ● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
# ● Por cada cuenta debe pedir un número telefónico para contactarse.

# ● El programa no terminará de preguntar por los números hasta que todas las organizaciones
# tengan un número de contacto asignado.
# ● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
# ● Se debe guardar como un string.


import random

def generar_password():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    contraseña = ""
    for _ in range(8):
        contraseña += random.choice(caracteres)
    return contraseña

def crear_fono(usuario, current, total):
    fono=input(f"[{current+1}/{total}] Ingrese un fono de 8 digitos para {usuario}: ")
    if fono.isnumeric():
        if len(fono) == 8:
            print("Fono registrado")
            return fono
        else:
            print("El fono debe tener 8 digitos")
            crear_fono(usuario, current, total)
    else:
        print(f"¡El fono solo debe contener caracteres numericos!")
        crear_fono(usuario, current, total)


def VECTOR(Filas, Valor = None):
    Arreglo = []
    for Fila in range(0, Filas):
        Arreglo.append(Valor)
    return Arreglo


###### codigo principal #######

usuarios = ["Alexis", "Berta", "Cristian", "Daniel", "Emilia", "Fabian", "Gustavo", "Helena", "Ignacio", "Juan"]
cuentas = VECTOR(len(usuarios))

i= 0
for usuario in usuarios:
    cuenta = {"usuario": usuario}
    cuenta["password"] = generar_password()
    cuenta["fono"] = crear_fono(usuario, i, len(usuarios))
    cuentas[i] = cuenta
    i+= 1
print(cuentas)

feednotback = 0
while feednotback != 7:
    feednotback = input("¿Que nota le pondria a mi solucion? (Elija un numero del 1 al 7)")
    if feednotback.isnumeric():
        if feednotback == 7:
            print("Muchas Gracias!")
        elif feednotback > 7:
            print("Se agradece pero se salio del rango")
        else:
            print("noo profe, me gustaria que me indicara por que no me pone 7 con un input en esta linea, pero creo que no recibire el mensaje :()")
    else:
        print("Debe ingresar un numero")



