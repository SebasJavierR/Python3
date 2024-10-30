def mod_serpiente(direccion,punto,serpiente):
    """Esta funcion recive la direccion, si el jugador a echo punto y la serpiente
    para modificarla de acuerdo a las normas del juego, si capturo un punto
    se agranda y se mueve, de lo contrario solo se desplaza, devuelve la ultima 
    posicion a la que se desplazo la serpiente.
    """
    #punto == 1 #Serpiente NO pierde el punto mas viejo
    #punto == 0 #Serpiente SI pierde el punto mas viejo
    #direccion == "a" #columna disminulle en 1
    #direccion == "d" #columna aumenta en 1
    #direccion == "s" #fila disminulle en 1
    #direccion == "w" #fila aumenta en 1

    if punto == 1:
        if direccion == "a":
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] -1]
        if direccion == "d":
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] +1]
        if direccion == "s":
            nuevo_punto = [serpiente[-1][0] -1 , serpiente[-1][-1]]
        if direccion == "w":
            nuevo_punto = [serpiente[-1][0] +1 , serpiente[-1][-1]]

        serpiente.append(nuevo_punto)
        return nuevo_punto

    else:
        if direccion == "a":
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] -1]
        if direccion == "d":
            nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] +1]
        if direccion == "s":
            nuevo_punto = [serpiente[-1][0] -1 , serpiente[-1][-1]]
        if direccion == "w":
            nuevo_punto = [serpiente[-1][0] +1 , serpiente[-1][-1]]

        serpiente.append(nuevo_punto)
        serpiente.pop(0)
        return nuevo_punto