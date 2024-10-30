import terminal
import random
#terminal.timed_input(timeout)
#terminal.clear_terminal() #Limpiar terminal
#random.randint(a, b) #numero random entre a y b

def generar_objetivo(serpiente,tablero):
    """Esta funcion resive la serpiente y el tablero y genera un objetivo
    dentro del tablero y que no coinsida con la serpiente
    """
    while True:
        objetivo = [random.randint(0,len(tablero[0])),random.randint(0,len(tablero))] # [Fila,Columna]
        for h in range(len(serpiente)):
            if objetivo[0] == serpiente[h][0] and objetivo[-1] == serpiente[h][-1]: #evitar que el objetivo se genere sobre la serpiente
                break
            if h == len(serpiente)-1 and (objetivo[0] != serpiente[h][0] or objetivo[-1] != serpiente[h][-1]) :
                return objetivo
    return objetivo

def chequear_si_choco(nuevo_punto,serpiente):
    """La funcion resive el nuevo punto de la serpiente y la serpiente, 
    devolviendo True si ese punto se encuentra dentro de la serpiente
    o False si no
    """
    for h in range(len(serpiente)-1):
        if nuevo_punto[0] == serpiente[h][0] and nuevo_punto[-1] == serpiente[h][-1]:
            return True
        else:
            return False

def generar_tablero(tablero):
    """Esta funcion recive el tablero y devuelve uno nuevo""" 
    paso = 1
    terminal.clear_terminal
    print("""Puedes introducir "cancelar" para volver atras
    """)
    while True:
        if paso == 1:
            n_filas = input("¿Cuantas filas quieres que alla? [Numero Positivo] ")
            if n_filas.isdigit():
                paso = 2
            elif n_filas == "atras":
                break
            else:
                print("No es un valor valido")
        if paso == 2:
            n_columnas = input("¿Cuantas Columnas quieres que alla? [Numero Positivo] ")
            if n_columnas.isdigit():
                paso = 3
            elif n_columnas == "atras":
                break
            else:
                print("No es un valor valido")
        if paso == 3:
            tablero = []
            fila = []
            for _ in range(int(n_filas)):
                fila.append("   ")
            for _ in range(int(n_columnas)):
                tablero.append(fila)
            return tablero
    return tablero

def bienvenido():
    """Esta funcion genera un mensaje de "bienvenida"
    """ 
    terminal.clear_terminal()
    print("")
    print("Bienvenid@, usted esta apunto de empezar a jugar al Snake")
    print("")
    print("Echo por Sebastian Roca")
    print("")
    return

def tutorial():
    """Esta funcion genera un mensaje con un tutorial de como
    jugar al snake al ser llamada
    """
    print("""     Bienvenido al Snake, tu objetivo es lograr,
    obtener la serpiente mas larga posible
    sin chocarte con tigo mismo, para
    que tu serpiente cresca debes "comer"
    todos los * posibles. 
    
    Para moverte usa A/S/D/W

    dale a enter para volver al menu principal
    """)
    esperar_enter = input()
    terminal.clear_terminal()
    return

def modificar_v(velocidad):
    """esta funcion recive la velocidad y devuelve un nuevo parametro de velocidad
    cambiado a gusto del jugador
    """
    while True:
        print("""Puedes introducir "atras" para volver sin modificar nada """)
        valor2 = input("Introduce la nueva velocidad en segundos(Numero positivo): ")
        if valor2.isdigit():
            terminal.clear_terminal()
            velocidad = valor2
            print("la velocidad fue cambiada a" + velocidad)
            return velocidad
        elif valor2 == "atras":
            terminal.clear_terminal()
            break
        else:
            terminal.clear_terminal()
            print("No as introducido un valor valido")
    return velocidad

def configuracion(velocidad,tablero):
    """Esta funcion recive la velocidad y el tablero para generar
    un menu que permite al usuario acceder a su vez a otras opciones
    para editar el juego, finalmente devuelve la nueva velocidad y el nuevo 
    tablero si fue cambiado.
    """
    while True:
        terminal.clear_terminal()
        print("""       Configuracion Actual""")
        print("")
        print("Filas del tablero: ",len(tablero[0]))
        print("Columnas del tablero: ",len(tablero))
        print("Velocidad,", velocidad , "segundos para mover")
        print("")
        print("""- Ingrese 1 para modificar el tablero.
- Ingrese 2 para modificar la velocidad.
- Introdusca 3 para volver atras.
        """)
        valor = input("[Opciones: 1/2/3] ")
        if valor.isdigit() and int(valor) == 1:
            terminal.clear_terminal()
            tablero = generar_tablero(tablero)
        if valor.isdigit() and int(valor) == 2:
            terminal.clear_terminal()
            velocidad = modificar_v(velocidad)
        if valor.isdigit() and int(valor) == 3:
            terminal.clear_terminal()
            print("Volviendo al menu...")
            break
        else:
            terminal.clear_terminal()
            print("No as introducido un valor valido")
    return velocidad , tablero

def pantalla(serpiente,objetivo, tablero):
    """Esta funcion recive la serpiente, el objetivo y el tablero,
    con estos parametros genera un tablero del juego
    """
    terminal.clear_terminal()
    mostrar = [[]]
    mostrar = tablero #[Fila,Columna]
    a , b = objetivo 
    mostrar[a][b] = " * "
    for j in range(len(serpiente)):
        mostrar[serpiente[j][0]][serpiente[j][-1]] = " # "
    for f in range(len(mostrar)):
        print(mostrar[f])
    print("")
    print("Muevete con A/S/D/W")
    print("debug:" , serpiente, "matriz serpiente") #Esta linea solo esta para poder ver informacion adicional, sera borrada al finalizar el trabajo
    return

def mod_serpiente(direccion,alargar_alargarserpiente,serpiente):
    """Esta funcion recive la direccion, si el jugador a echo punto y la serpiente
    para modificarla de acuerdo a las normas del juego, si capturo un punto
    se agranda y se mueve, de lo contrario solo se desplaza, devuelve la ultima 
    posicion a la que se desplazo la serpiente.
    """
    #punto == 1 #Serpiente NO pierde el punto mas viejo
    #punto == 0 #Serpiente SI pierde el punto mas viejo
    #direccion == "a" #columna disminulle en 1
    #direccion == "d" #columna aumenta en 1
    #direccion == "s" #fila aumenta en 1
    #direccion == "w" #fila disminulle en 1

    if alargar_alargarserpiente == 1 :
        if direccion == "a":
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] -1]
        if direccion == "d":
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] +1]
        if direccion == "s":
            nuevo_punto = [serpiente[-1][0] +1 , serpiente[-1][-1]]
        if direccion == "w":
            nuevo_punto = [serpiente[-1][0] -1 , serpiente[-1][-1]]

        serpiente.append(nuevo_punto)
        alargar_alargarserpiente = 0
        return nuevo_punto

    else:
        if direccion == "a":
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] -1]
        if direccion == "d":
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] +1]
        if direccion == "s":
            nuevo_punto = [serpiente[-1][0] +1 , serpiente[-1][-1]]
        if direccion == "w":
            nuevo_punto = [serpiente[-1][0] -1 , serpiente[-1][-1]]

        serpiente.append(nuevo_punto)
        serpiente.pop(0)
        return nuevo_punto

def jugar(tablero,velocidad):
    """Esta funcion recive un tablero y la velocidad, con ello 
    funciona como menu" para el funcionamiento del juego.
    """
    punto = 1
    alargar_alargarserpiente = 0
    serpiente = [[len(tablero)//2 , len(tablero[0])//2]]
    while True:
        if punto == 1:
            objetivo = generar_objetivo(serpiente,tablero)
            alargar_alargarserpiente = 1
            punto = 0
        if punto == 0:
            pantalla(serpiente,objetivo,tablero)
            valor = terminal.timed_input(velocidad)
            direccion = list(valor[0]) #Primer valor en ser introducido
            nuevo_punto = mod_serpiente(direccion,alargar_alargarserpiente,serpiente)
            if nuevo_punto == objetivo:
                punto = 1
            if chequear_si_choco(nuevo_punto,serpiente) == True:
                terminal.clear_terminal()
                print("La serpiente llego a medir:" + len(serpiente))
                return
    return

def menu():
    """Esta funcion funciona como menu principal del juego
    y organiza todo de forma que se pueda acceder de forma 
    comoda a la edicion de los parametros de la partida al
    igual que al juego y a un pequeño tutorial.
    """
    bienvenido()
    tablero = [["   ","   ","   ","   ","   "],["   ","   ","   ","   ","   "],["   ","   ","   ","   ","   "],["   ","   ","   ","   ","   "],["   ","   ","   ","   ","   "]]
    #Tablero generico, encaso de que no se configure ninguno especial. 5x5
    velocidad = 5 #Tiempo para mover por defecto.
    while True:
        print("""- Introdusca 1 para editar la configuracion.
- Introdusca 2 para ver el tutorial.
- Introdusca 3 para jugar.
- Introdusca 4 para salir del juego.
        """)
        valor = input("[Opciones: 1/2/3/4] ")
        if valor.isdigit() and int(valor) == 1:
            velocidad , tablero = configuracion(velocidad,tablero)
        if valor.isdigit() and int(valor) == 2:
            print ("tutorial Proximamente")
            tutorial() 
        if valor.isdigit() and int(valor) == 3:
            jugar(tablero,velocidad)
        if valor.isdigit() and int(valor) == 4:
            print("Apagando programa...")
            break
        else:
            terminal.clear_terminal()
    return

menu()
