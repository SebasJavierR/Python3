mensaje = "Ingrese un valor entre -10 y 10: "
min = -10
max = 10


def juzgar_numero(valor):
        if valor > max:
            return "el valor es mayor al maximo"
        elif valor < min:
            return "el valor es inferior al minimo"
        else:
            return valor

def pedir_entero(mensaje , max, min):
    while True:
        valor = input(mensaje)
        if valor.isdigit(): #Si es un numero positivo
            valor = int(valor)
            return juzgar_numero(valor)
        
        else: #Si es negativo o no es un numero
            valor = valor.split("-")
            valor = "".join(valor)
            if valor.isdigit():
                valor = int(valor)
                valor = int("-" + str(valor))
                return juzgar_numero(valor)
            else:
                return "No a ingresado un numero"

print(pedir_entero(mensaje , max , min))