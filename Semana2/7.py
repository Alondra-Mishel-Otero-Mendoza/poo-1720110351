class Chevrolet():
    llantas = None
    color = None
    trasmision = None
    filtro = None
    quemacocos = None
    parabrisas = None
    limpiaparabrisas = None
    asientos = None
    volante = None
    modelo = None
    
    
    def __init__(self):
        print ("Audi")
    
    def pasear(self):
        print("Donde sea")
    
    def llevar(self):
        print("Lugares")
    
    def transportar(self):
        print("Persona 7")
    
    def arrancar(self):
        print("Electrico")
    
    def freno(self):
        print("de discos")

    
audi= Chevrolet()
audi.llantas=("4 Deportivas")
audi.color=("gris")
audi.trasmision=("Automatico")
audi.filtro=("Aceite y gasolina")
audi.quemacocos=("si")
audi.parabrisas=("si")
audi.limpiaparabrisas=("si")
audi.asientos=("2 individules, 1 para 4")
audi.volante=("deportivo")
audi.modelo=("2019 deportivo")

print(audi.llantas)
print(audi.color)
print(audi.trasmision)
print(audi.filtro)
print(audi.quemacocos)
print(audi.parabrisas)
print(audi.limpiaparabrisas)
print(audi.asientos)
print(audi.volante)
print(audi.modelo)