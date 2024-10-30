datos = []
import terminal
import random
#terminal.timed_input(timeout)
#terminal.clear_terminal() #Limpiar terminal
#random.randint(a, b) #numero random entre a y b
tablero = [["  .","  .","  .","  .","  ."],["  .","  .","  .","  .","  ."],["  .","  .","  .","  ."," . "],["  .","  .","  .","  .","  ."],["  .","  .","  .","  .","  ."]]
#Tablero generico, encaso de que no se configure ninguno especial. 5x5
serpiente = [] #Reiniciar serpiente, Formato:[[Fila,Columna],[...],...]
velocidad = 5 #Tiempo para mover por defecto.
objetivo = [0,0] # Punto
nuevo_punto = [-1,-1]
punto = 0
# "  ." Vacio
# " #." Serpiente
# " @." Punto

def generar_objetivo():
    while True:
        objetivo = [random.randint(0, len(tablero[0])),random.randint(0, len(tablero))]
        for h in range(len(serpiente)):
            if objetivo[0] != serpiente[h][0] and objetivo[-1] != serpiente[h][-1]: #evitar que el objetivo se genere sobre la serpiente
                break
            else:
                continue
    return 

def chequear_si_choco(nuevo_punto): #0 no perdio, 1 perdio
    x , y = nuevo_punto
    for z in range(len(serpiente)):
        a , b = serpiente[z][0] , serpiente[z][-1]
        if a == x:
          if b == y:
            return 1
    return 0

def generar_tablero(): #Lista
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
            for i in range(n_filas):
                fila.append("  .")
            for j in range(n_columnas):
                tablero.append(fila)
            break
    return

def bienvenido(): #Lista
    terminal.clear_terminal()
    print("")
    print("Bienvenid@, usted esta apunto de empezar a jugar al Snake")
    print("")
    print("Echo por Sebastian Roca")
    print("")
    return

def modificar_v():
    while True:
        print("""Puedes introducir "atras" para volver sin modificar nada """)
        valor2 = input("Introduce la nueva velocidad en segundos(Numero positivo): ")
        if valor2.isdigit():
            terminal.clear_terminal()
            velocidad = valor2
            print("la velocidad fue cambiada a" + velocidad)
            break
        elif valor2 == "atras":
            terminal.clear_terminal()
            break
        else:
            terminal.clear_terminal()
            print("No as introducido un valor valido")
    return

def configuracion():
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
            generar_tablero()
        if valor.isdigit() and int(valor) == 2:
            terminal.clear_terminal()
            modificar_v()
        if valor.isdigit() and int(valor) == 3:
            terminal.clear_terminal()
            print("Volviendo al menu...")
            break
        if not valor.isdigit() and int(valor) > 3:
            terminal.clear_terminal()
            print("""
            ¡No ha introducido un valor valido!
            """)
    return

def pantalla():
    mostrar = []
    mostrar = tablero
    for j in range(len(serpiente)):
        mostrar[serpiente[j][0]][serpiente[j][1]] = " #."
    mostrar[objetivo[0]][objetivo[1]] = " @."

    for f in range(len(tablero)):
        print(mostrar[f])
    print("")
    print("Muevete con A/S/D/W")
    return

def mod_serpiente(direccion,punto):
    if direccion[0] == "a": # izquierda
        if punto == 0:
            nuevo_punto = [serpiente[-1][0]-1 , serpiente[-1][-1]]  #Generar futura posicion   
            serpiente.pop(0)                                        #quitar posicion vieja
            serpiente.append(nuevo_punto)                           #Agregar el nuevo punto
        elif punto == 1:
            nuevo_punto = [serpiente[-1][0]-1 , serpiente[-1][-1]]
            serpiente.append(nuevo_punto)
            punto = 0

    elif direccion[0] == "s": # abajo
        if punto == 0:
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1]-1]
            serpiente.pop(0)
            serpiente.append(nuevo_punto)
        elif punto == 1:
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1]-1]
            serpiente.append(nuevo_punto)
            punto = 0

    elif direccion[0] == "d": # derecha
        if punto == 0:
            nuevo_punto = [serpiente[-1][0]+1 , serpiente[-1][-1]]
            serpiente.pop(0)
            serpiente.append(nuevo_punto)
        elif punto == 1:
            nuevo_punto = [serpiente[-1][0]+1 , serpiente[-1][-1]]
            serpiente.append(nuevo_punto)
            punto = 0

    elif direccion[0] == "w": # arriba
        if punto == 0:
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1]+1]
            serpiente.pop(0)
            serpiente.append(nuevo_punto)
        elif punto == 1:
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1]+1]
            serpiente.append(nuevo_punto)
            punto = 0
    return nuevo_punto

def jugar():
    perdio = 0
    direccion = "w"
    centro = [len(tablero)//2 , len(tablero[0])//2] #Formato:[fila, columna]
    serpiente = [] #Reiniciar serpiente, Formato:[[Fila,Columna],[...],...]
    serpiente.append(centro) #Posicion inicial de la serpiente, 
    generar_objetivo()
    while True:
        if perdio == 0:
            terminal.clear_terminal()
            generar_objetivo()
            pantalla()
            direccion = terminal.timed_input(velocidad)
            perdio = chequear_si_choco(mod_serpiente(direccion,punto)) #Si choca la funcion devuelve 1 si no devuelve 0

        elif perdio == 1:
            terminal.clear_terminal()
            print("La serpiente llego a medir " + len(serpiente))
            esperar = terminal.timed_input(30)
            break
    return

def menu():
    bienvenido()
    while True:
        print("""- Introdusca 1 para editar la configuracion.
- Introdusca 2 para ver el tutorial.
- Introdusca 3 para jugar.
- Introdusca 4 para salir del juego.
        """)
        valor = input("[Opciones: 1/2/3/4] ")
        if valor.isdigit() and int(valor) == 1:
            configuracion()
        if valor.isdigit() and int(valor) == 2:
            print ("tutorial Proximamente")
            #tutorial() 
        if valor.isdigit() and int(valor) == 3:
            jugar()
        if valor.isdigit() and int(valor) == 4:
            print("Apagando programa...")
            break
        if not valor.isdigit() and int(valor) > 4:
            terminal.clear_terminal()
            print("""
            ¡No ha introducido un valor valido!
            """)
    return

menu()
