mensaje = "¿Cuál es tu número favorito?"
min = -50
max = 50

def pedir_entero(mensaje , max, min):
    """ Esta funcion recive un numero entero maximo, un minimo y un mensaje,
    con esta informacion pide al usuario un numero entero, si se encuentra entre
    el minimo y el maximo, lo devuelve, de lo contrario devuelve un mensaje de error
    aclarando si es mayor, menor o no es un numero que cumpla los requisitos y 
    vuelve a pedir que se ingrese un numero que si cumpla.
    """
    mensaje = mensaje + " [ {}..{} ]: ".format(min,max)
    while True:
        marca = 0
        valor = input(mensaje)
        if valor[0] == "-":
            marca = 1
            auxiliar = valor
            valor = valor[1:]

        if valor.isdigit(): 
            if marca == 1:
                valor = auxiliar
            if int(valor) > max:
                print("el valor es mayor al maximo")
            elif int(valor) < min:
                print("el valor es inferior al minimo")
            else:
                return valor
        else:
            print("No a ingresado un numero entero")

print(pedir_entero(mensaje , max , min))
