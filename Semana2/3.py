class Avion():
    alas = None
    pasajeros = None
    piloto = None
    azafata = None
    equipaje = None
    horario = None
    oxigeno = None
    combustible = None
    altura = None
    ventanas = None
    
    
    def __init__(self):
        print ("Avion Militar")
    
    def Arrancar(self):
        print("Realiza")
    
    def Despejar(self):
        print("Libros")
    
    def lugar(self):
        print("Donde?")
    
    def Volar(self):
        print("En maniobras")
    
    def Aterrisar(self):
        print("En clase")

 

combate= Avion()
combate.alas=("2")
combate.pasajeros=("1")
combate.piloto=("1")
combate.azafata=("0")
combate.equipaje=("0")
combate.horario=("30/03/2021")
combate.oxigeno=("Artificial")
combate.combustible=("Jet fuel")
combate.altura=("5000-6000 metros")
combate.ventanas=("1")



print(combate.alas)
print(combate.pasajeros)
print(combate.piloto)
print(combate.azafata)
print(combate.equipaje)
print(combate.horario)
print(combate.oxigeno)
print(combate.combustible)
print(combate.altura)
print(combate.ventanas)