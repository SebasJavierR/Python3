class Charla:
    def __init__(self,edad,nombre):
        self.edad = edad #self.edad ES DISTINTO A edad
        self.nombre = nombre
        print("Se a agregado un miembro a la clase")

    def hablar(self, mensaje):
        print("")
        print(mensaje)
    def informar_edad(self):
        print("y tengo ", self.edad, " años de edad")
    
    def creecer(self):
        self.edad += 1
        print(self.nombre)

class pokemon:
    def __init__(self,edad,nombre):
        self.vida = 50
        self.hambre = 50
        self.energia = 50
        self.poder = 10
        self.edad = edad
        self.nombre = nombre
    def dormir(self):
        self.vida += 5
        self.hambre -= 5
        self.energia += 40
        print(self.nombre, "se fue a dormir")
    def curar(self):
        self.vida += 50
        self.hambre -= 5
        self.energia -= 5
        print(self.nombre, "fue curado")
    def pasar(self):
        self.vida += 5
        self.hambre -= 5
        self.energia -= 5
        print("pasar turno")
    def evolucionar(self):
        self.vida -= 50
        self.hambre -= 50
        self.energia -= 50
        self.poder += 10
        print(self.nombre, "fue evolucionado")
    def alimentar(self):
        self.vida += 10
        self.hambre += 50
        print(self.nombre, "fue alimentado")
    def llamar(self, mensaje):
        print(mensaje, self.nombre)
    def estado(self):
        print("vida ",self.vida)
        print("hambre ",self.hambre)
        print("poder ",self.poder)
        print("energia ",self.energia)
        

pikachu = pokemon(10, "Pikachu")
pikachu.estado()
pikachu.pasar()
pikachu.estado()
pokemon.__init__(self.hambre)
print(type(__hambre__))
print(isinstance(__hambre__, pokemon))


