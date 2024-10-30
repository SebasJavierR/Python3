def _unix_timed_getch(timeout):
    '''
    Espera hasta _timeout_ segundos una pulsaci�n de tecla de la terminal.
    Si no se puls� ninguna tecla devuelve el valor por defecto.
    '''
    import string, select, sys

    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    
    if ready:
        character = sys.stdin.read(1)
        if ord(character) == 3:
            raise KeyboardInterrupt
        elif ord(character) == 4:
            raise EOFError
        return character
    
    return ''

def _unix_timed_input(timeout):
    import termios, tty, sys, time

    # Limpiar buffer de stdin
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    
    fd = sys.stdin.fileno()

    old_settings = termios.tcgetattr(fd)
    # Desactivar eco y buffering de la terminal
    tty.setraw(sys.stdin.fileno())

    buffer = ''

    try:
        start_time = time.time()
        elapsed = 0
        while elapsed < timeout:
            buffer += _unix_timed_getch(timeout - elapsed)
            elapsed = time.time() - start_time
    finally:
        # Restaurar eco y buffering de la terminal
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return buffer

def _unix_clear_terminal():
    import os
    os.system('clear')

def _win_timed_input(timeout):
    import msvcrt, time, sys
    
    # Limpiar el buffer de stdin
    while msvcrt.kbhit():
        msvcrt.getch()
    
    buffer = ''
    
    start_time = time.time()
    while time.time() - start_time < timeout:
        if msvcrt.kbhit():
            buffer += msvcrt.getch().decode(sys.stdout.encoding)
        time.sleep(timeout / 10)

    return buffer

def _win_clear_terminal():
    import os
    os.system('cls')

def timed_input(timeout):
    '''
    Lee entrada del usuario durante _timeout_ segundos. Devuelve una cadena
    con todas las teclas que el usuario presion� durante ese tiempo.
    
    Si pasan _timeout_ segundos y no se presion� ninguna tecla, devuelve una
    cadena vac�a.
    '''
    return _timed_input(timeout)

def clear_terminal():
    '''
    Borra todo el contenido de la terminal y restaura el cursor a la primera 
    posici�n.
    '''
    _clear_terminal()

try:
    # Detectar al cargar el m�dulo si estamos en Unix o Windows
    import msvcrt
    _timed_input = _win_timed_input
    _clear_terminal = _win_clear_terminal
except ImportError:
    _timed_input = _unix_timed_input
    _clear_terminal = _unix_clear_terminal

print(timed_input(1))
clear_terminal()

import random
import terminal
ganar=3
x_tablero=3
y_tablero=3
tiempo=1

def reglas():
    '''parametros del juego'''
    while True:
        ganar=input("elige el largo maximo de la serpiente")
        x_tablero=input("elige el largo del tablero")
        y_tablero=input("elige el ancho del tablero")
        dificultad=input("""elige la dificultad
        1:Facil
        2:normal
        3:dificil""")
        if not (ganar.isdigit() and x_tablero.isdigit() and y_tablero.isdigit() and dificultad.isdigit()):
            print("los datos deben ser numeros enteros positivos")
            continue
        if int(dificultad)==1:
            tiempo=3
            break
        if int(dificultad)==2:
            tiempo=2
            break
        if int(dificultad)==3:
            tiempo=1
            break
        else:
            tiempo=input("elige el tiempo para realizar movimientos")
            if tiempo.isdigit():
                break
    return (ganar,x_tablero,y_tablero,tiempo)

def crear_tablero(x_tablero,y_tablero):
    """crea un tablero de dimensiones x_tablero x y_tablero"""          
    tabla=[]
    for y in range(y_tablero):
            tabla.append(["-"]*x_tablero)
    return(tabla)

def aparece_fruta(x_tablero,y_tablero):
    """hace aparecer una "fruta" en un tablero x_tablero x y_tablero dimensiones"""
    x_fruta=random.randint(0,x_tablero-1)
    y_fruta=random.randint(0,y_tablero-1)
    return(x_fruta,y_fruta)

def inicio():
    """el juego snake en python, desmarcar comentarios para elegir los parametros o ingresar manualmente el movimiento"""
    #parametros=reglas()
    #ganar=parametros[0]
    #x_tablero=parametros[1]
    #y_tablero=parametros[2]
    #tiempo=parametros[3]
    tabla=crear_tablero(x_tablero,y_tablero)
    tabla=list(tabla)
    x_cabeza=random.randint(0,x_tablero-1)
    y_cabeza=random.randint(0,y_tablero-1)
    pos_fruta=aparece_fruta(x_tablero,y_tablero)
    puntuacion=0
    while (pos_fruta)==(x_cabeza,y_cabeza):
        pos_fruta=aparece_fruta(x_tablero,y_tablero)
    x_fruta=pos_fruta[0]
    y_fruta=pos_fruta[1]
    snake=[[x_cabeza,y_cabeza]]
    tabla[x_fruta][y_fruta]="G"
    tabla[x_cabeza][y_cabeza]="■"
    print(tabla[0])
    print(tabla[1])
    print(tabla[2])
    while True:
        movimiento=input("muevete con w a s d")
        ultimo_movimiento=0
        if movimiento in ("w","a","s","d"):
            break
    while True:
        mover=moverse(snake,ultimo_movimiento,movimiento)
        snake=mover[0]
        ultimo_movimiento=mover[1]
        if snake[0] in snake[1:]:
                print("perdiste")
                return("tu puntuacion:",puntuacion)
        if snake[0][0] in (-1,y_tablero) or snake[0][1] in (-1,x_tablero):
            print("perdiste")
            return("tu puntuacion:",puntuacion)
        if (snake[0][0],snake[0][1])==(x_fruta,y_fruta):
            puntuacion+=1
            if puntuacion==ganar:
                print("ganaste")
                return("has ganado")
            pos_fruta=aparece_fruta(x_tablero,y_tablero)
            parte_nueva=snake[:]
            snake.append(parte_nueva[0])
            while [pos_fruta] in snake:
                pos_fruta=aparece_fruta(x_tablero,y_tablero)
            x_fruta=pos_fruta[0]
            y_fruta=pos_fruta[1]
        for i in range(len(tabla)):
            for j in range(len(tabla[i])):
                tabla[i][j]="-"
        tabla[x_fruta][y_fruta]="G"
        for i in range(len(snake)):
            y=snake[i][0]
            x=snake[i][1]
            tabla[y][x]="■"
        for i in range(len(tabla)):
            print(tabla[i])
        movimiento=timed_input(tiempo)
        #movimiento=input("muevete con w a s d")

def moverse(snake,ultimo_movimiento,movimiento):
    """ mueve la snake y cambia la posicion de sus segmentos """
    if len(snake) > 1:
        k=[]
        n=snake[:]
        n=list(n)
        snake.pop()
        for i in n[0]:
            k.append(i)
        snake.reverse()
        snake.append(k)
        snake.reverse()
    if movimiento not in ("w","a","s","d"):
        movimiento=ultimo_movimiento
    if  movimiento=="d":
        snake[0][1]+=1
        ultimo_movimiento="d"
    if movimiento=="a":
        snake[0][1]-=1
        ultimo_movimiento="a"
    if movimiento=="w":
        snake[0][0]-=1
        ultimo_movimiento="w"
    if movimiento=="s":
        snake[0][0]+=1
        ultimo_movimiento="s"
    return(snake,ultimo_movimiento)


inicio()