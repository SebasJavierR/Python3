
def generar_tablero(tablero):
    columna = []
    filas = []
    for _ in range(tablero[-1]):
        columna.append(" ")
    for _ in range(tablero[0]):
        filas.append(columna)
    return filas

def display(tablero, mostrar):
    for j in range(tablero[0]):
        linea = ""
        for i in range(tablero[-1]):
            linea = linea + str(mostrar[j][i] +".")
        print(linea)
    return

tablero = [5,6]
fruta = [1,2]
serpiente = [[1,2],[1,3],[1,4],[1,5]]

def esta_en_serp(serpiente,i,j):
    for v in range(len(serpiente)):
        if serpiente[v][0] == i and serpiente[v][-1] == j:
            return True
    return False

def convinar(tablero,fruta,serpiente):
    matriz = []
    for i in range(tablero[0]): #filas
        fila = []
        for j in range(tablero[-1]): #columnas  
            if esta_en_serp(serpiente,i,j):
                fila.append("#")
            elif fruta[0] == i and fruta[-1] == j:
                fila.append("*")
            else:
                fila.append(" ")
        matriz.append(fila)
    return matriz

def pantalla(serpiente,fruta, tablero):
    """Esta funcion recive la serpiente, la fruta y el tablero,
    con estos parametros genera un tablero del juego
    """
    mostrar = convinar(tablero,fruta,serpiente)
    print("")
    display(tablero, mostrar)
    print(mostrar)
    print("")
    print("Muevete con A/S/D/W")
    return

pantalla(serpiente,fruta, tablero)

