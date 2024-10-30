def pangrama(texto):
    import string
    abc = string.ascii_lowercase
    for letra in abc:
        if not letra in texto:
            return False
    return True

#print(pangrama(""))

def minima_unidad(numero):
    contador = 0
    while numero > 10:
        for i in range (len(str(numero))):
            contador = contador + int(str(numero)[i])
            print(contador)
        break
    return contador

print(minima_unidad(546))