mensaje = "Ingrese un valor entre -10 y 10: "
min = -10
max = 10


def pedir_entero(mensaje , max, min):
    while True:
        valor = input(mensaje)
        if valor.isdigit(): #Si es un numero positivo
            valor = int(valor)
            if valor > max:
                print("el valor es mayor al maximo")
            elif valor < min:
                print("el valor es inferior al minimo")
            else:
                break

        else: #Si es negativo o no es un numero
            valor = valor.split("-")
            valor = "".join(valor)
            if valor.isdigit():
                valor = int(valor)
                valor = int("-" + str(valor))
                if valor > max:
                    print("el valor es mayor al maximo")
                elif valor < min:
                    print("el valor es inferior al minimo")
                else:
                    break
            else:
                print("No a ingresado un numero")
    return valor

print(pedir_entero(mensaje , max , min))
