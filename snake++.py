import random
import terminal


def niveles(numero_nivel):
    nombre_nivel="c:/Users/Matiiiitas/Desktop/nivel_"+str(numero_nivel)+".txt"
    with open(nombre_nivel) as nivel:
        parametros=nivel.readlines()
        for i in range(4):
            parametros[i]=parametros[i].split("\n")[0]
        return (parametros)
def lista_tipos_especiales():
    with open("c:/Users/Matiiiitas/Desktop/especiales.csv") as tipos_especiales:
        especiales=tipos_especiales.readlines()
        especiales.pop()
        for i in range(5):
            especiales[i]=especiales[i].split("\n")[0]
        return especiales

def crear_tablero(x_tablero,y_tablero):
    """crea un tablero de dimensiones x_tablero x y_tablero"""          
    tabla=[]
    for y in range(y_tablero):
            tabla.append(["-"]*x_tablero)
    return tabla

def asignar_snake(x_tablero,y_tablero,obstaculos):
    """hace aparecer la snake en un tablero x_tablero x y_tablero dimensiones"""
    while True:
            x_cabeza=random.randint(0,x_tablero-1)
            y_cabeza=random.randint(0,y_tablero-1)
            snake=[[x_cabeza,y_cabeza]]
            if snake[0] not in obstaculos:
                return(snake)

def asignar_fruta(x_tablero,y_tablero,snake,pos_especial,obstaculos):
    """hace aparecer una "fruta" en un tablero x_tablero x y_tablero dimensiones"""
    while True:
        x_fruta=random.randint(0,x_tablero-1)
        y_fruta=random.randint(0,y_tablero-1)
        if not ([x_fruta,y_fruta] in snake or [x_fruta,y_fruta] in obstaculos or [x_fruta,y_fruta] in pos_especial[:2]):
            return (x_fruta,y_fruta)

def asignar_especial(x_tablero,y_tablero,snake,especiales,obstaculos):
    """hace aparecer un especial al azar en un tablero x_tablero x y_tablero dimensiones"""
    while True:
        tipo_especial=random.randint(0,len(especiales)-1)
        x_especial=random.randint(0,x_tablero-1)
        y_especial=random.randint(0,y_tablero-1)
        if not ([x_especial,y_especial] in snake or [x_especial,y_especial] in obstaculos):
            return [x_especial,y_especial,tipo_especial]

def main():
    """ el juego snake en python """
    numero_nivel=0
    lista_especiales=lista_tipos_especiales()
    teclas_especiales=[]
    tipos_especiales=[]
    for i in range(1,5):
            tipos_especiales.append(lista_especiales[i].split(","))
            teclas_especiales.append(tipos_especiales[i-1][3])
    inventario=[0]*(len(tipos_especiales))
    while True:
        numero_nivel+=1
        try:
            parametros=niveles(numero_nivel)
        except FileNotFoundError:
            print("felicidades, ganaste todos los niveles!")
            return "felicidades, ganaste todos los niveles!"
        ganar=int(parametros[0])
        ganar=2
        tiempo=float(parametros[1])
        tablero=parametros[2].split("x")
        x_tablero=int(tablero[1])
        y_tablero=int(tablero[0])
        obstaculos=parametros[3].split(";")
        for i in range(len(obstaculos)):
            obstaculos[i]=obstaculos[i].split(",")
            numeros=[int(obstaculos[i][1]),int(obstaculos[i][0])]
            obstaculos[i]=numeros
        especiales=parametros[4].split(",")
        tabla=crear_tablero(x_tablero,y_tablero)
        snake=asignar_snake(x_tablero,y_tablero,obstaculos)
        pos_especial=asignar_especial(x_tablero,y_tablero,snake,especiales,obstaculos)
        pos_fruta=asignar_fruta(x_tablero,y_tablero,snake,pos_especial,obstaculos)
        puntuacion=0
        ultimo_movimiento="default"
        while True:
            movimiento=terminal.timed_input(tiempo)
            movimiento=validar_movimiento(movimiento,ultimo_movimiento,teclas_especiales)
            especial=usar_especial(snake,movimiento[1],tiempo,inventario,tipos_especiales)
            if especial:
                snake=especial[0]
                tiempo=especial[1]
                inventario=especial[2]
            snake=moverse(snake,movimiento[0])
            if movimiento[0]=="no":
                continue
            jugada=procesar_jugada(snake,x_tablero,y_tablero,pos_fruta,puntuacion,ganar,obstaculos,pos_especial,inventario,especiales)
            if jugada[2]==-2:
                return("tu puntuacion:",puntuacion)
            if jugada[2]==-1:
                print("ganaste")
                break
            inventario=jugada[3][0]
            pos_especial=jugada[3][1]
            terminal.clear_terminal()
            snake=jugada[0]
            pos_fruta=jugada[1]
            puntuacion=jugada[2]
            imprimir(tabla,snake,pos_fruta,pos_especial,obstaculos,tipos_especiales,inventario)
            if movimiento[0]=="default":
                ultimo_movimiento="no"
                print("muevete con w a s d")
                continue
            ultimo_movimiento=movimiento[0]
def procesar_jugada(snake,x_tablero,y_tablero,pos_fruta,puntuacion,ganar,obstaculos,pos_especial,inventario,especiales):
    perdio=perdiste(snake,x_tablero,y_tablero,obstaculos)
    jugada=comer(snake,pos_fruta,pos_especial,puntuacion,ganar,x_tablero,y_tablero,obstaculos)
    comio_especial=comer_especial(x_tablero,y_tablero,snake,especiales,obstaculos,pos_especial,inventario)
    jugada.append(comio_especial)
    if perdio=="si":
        print("perdiste")
        jugada[2]=-2
    return jugada
def usar_especial(snake,tecla_especial,tiempo,inventario,tipos_especiales):
    if tecla_especial:
        for i in range(len(tipos_especiales)):
            if tecla_especial==tipos_especiales[i][3]:
                if inventario[i]==0:
                    continue
                if tipos_especiales[i][1]=="VELOCIDAD" and tiempo > float(tipos_especiales[i][2]):
                    tiempo+=float(tipos_especiales[i][2])
                elif int(tipos_especiales[i][2])==1:
                    snake.append(snake[0])
                elif len(snake)>1:
                    snake.pop()
                else:
                    continue
                inventario[i]-=1
        return (snake,tiempo,inventario)
    return None
def perdiste(snake,x_tablero,y_tablero,obstaculos):
    if snake[0] in snake[1:] or snake[0][0] in (-1,x_tablero) or snake[0][1] in (-1,y_tablero) or snake[0] in obstaculos:
        return "si"
def comer_especial(x_tablero,y_tablero,snake,especiales,obstaculos,pos_especial,inventario):
    if snake[0]==pos_especial[:2]:
        inventario[pos_especial[2]]+=1
        pos_especial=asignar_especial(x_tablero,y_tablero,snake,especiales,obstaculos)
    return (inventario,pos_especial)    
def comer(snake,pos_fruta,pos_especial,puntuacion,ganar,x_tablero,y_tablero,obstaculos):    
    puntuacion=int(puntuacion)
    if (snake[0][0],snake[0][1])==pos_fruta:
        puntuacion+=1
        if ganaste(puntuacion,ganar)=="si":
            puntuacion=-1
        parte_nueva=snake[:]
        snake.append(parte_nueva[0])
        pos_fruta=asignar_fruta(x_tablero,y_tablero,snake,pos_especial,obstaculos)
    return [snake,pos_fruta,puntuacion]
def ganaste(puntuacion,ganar):
    if puntuacion==ganar:
        return("si")
def imprimir(tabla,snake,pos_fruta,pos_especial,obstaculos,tipos_especiales,inventario):
    x_fruta=pos_fruta[0]
    y_fruta=pos_fruta[1]
    x_especial=pos_especial[0]
    y_especial=pos_especial[1]
    simbolo_especial=pos_especial[2]
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            tabla[i][j]="-"
    tabla[y_fruta][x_fruta]="O"
    tabla[y_especial][x_especial]=tipos_especiales[simbolo_especial][0]
    for i in range(len(snake)):
        y=snake[i][0]
        x=snake[i][1]
        tabla[x][y]="■"
    for i in range(len(obstaculos)):
        y=obstaculos[i][0]
        x=obstaculos[i][1]
        tabla[x][y]="#"
    for i in range(len(tabla)):
        print(tabla[i])
    print("""INVENTARIO
SIMBOLO|CANTIDAD|TECLA|DESCRIPCION""")
    for i in range(len(inventario)):
        print(" {}  |  {}  | {} | {}".format(tipos_especiales[i][0],inventario[i],tipos_especiales[i][3],tipos_especiales[i][4]))

def validar_movimiento(movimiento,ultimo_movimiento,teclas_especiales):
    """ verifica si se realizo un movimiento y lo devuelve y sino devuelve el ultimo movimiento """
    teclas=[ultimo_movimiento,0]
    for letra in movimiento:    
        if letra in teclas_especiales:
            teclas[1]=letra
        if letra in ("w","a","s","d"):
            teclas[0]=letra
    return teclas

def moverse(snake,movimiento):
    """ mueve la snake y cambia la posicion de sus segmentos """
    if len(snake) > 1:
        #esta tabla nueva sirve para que no se igualen las posiciones
        segmento=[]
        snake.pop()
        for i in snake[0]:
            segmento.append(i)
        snake.insert(0,segmento)
    if  movimiento=="d":
        snake[0][0]+=1
    if movimiento=="a":
        snake[0][0]-=1
    if movimiento=="w":
        snake[0][1]-=1
    if movimiento=="s":
        snake[0][1]+=1
    return snake


main()