def generar_fruta(serpiente,tablero):
    """Esta funcion resive la serpiente y el tablero y genera un objetivo
    dentro del tablero y que no coinsida con la serpiente
    """
    while True:
        objetivo = [random.randint(0,tablero[0]),random.randint(0,tablero[-1])] # [Fila,Columna]
        for h in range(len(serpiente)):
            if objetivo[0] == serpiente[h][0] and objetivo[-1] == serpiente[h][-1]: #evitar que el objetivo se genere sobre la serpiente
                break
            if h == len(serpiente)-1 and (objetivo[0] != serpiente[h][0] or objetivo[-1] != serpiente[h][-1]):
                return objetivo
    return objetivo


def esta_en_serp(serpiente,i,j):
    for v in range(len(serpiente)):
        if serpiente[v][0] == i and serpiente[v][-1] == j:
            return True
    return False

def generar_fruta(serpiente,tablero):
    """Esta funcion resive la serpiente y el tablero y genera un objetivo
    dentro del tablero y que no coinsida con la serpiente
    """
    while True:
        fruta = [random.randint(0,tablero[0]),random.randint(0,tablero[-1])] # [Fila,Columna]
        i,j = fruta:
        if esta_en_serp(serpiente,i,j)
            continue
        else:
            break

    return fruta