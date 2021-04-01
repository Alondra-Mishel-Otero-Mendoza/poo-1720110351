class Cajero():
    botones = None
    pantalla = None
    dinero = None
    cifras = None
    codigo = None
    usuario = None
    cuenta = None
    ticket = None
    retiros = None
    seguridad = None
    
    
    def __init__(self):
        print ("Cajero Banncomer")
    
    def Sacar(self):
        print("Dinero")
    
    def ingresar(self):
        print("Tarjeta")
    
    def retirar(self):
        print("Efectivo")
    
    def acciones(self):
        print("todo")
    
    def ingreso(self):
        print("efectivo")


banncomer= Cajero()
banncomer.botones=("si")
banncomer.pantalla=("tactil")
banncomer.dinero=("hasta $10 000")
banncomer.cifras=("$10 000")
banncomer.codigo=("si")
banncomer.usuario=("mishel")
banncomer.cuenta=("1720110351")
banncomer.ticket=("si")
banncomer.retiros=("si")
banncomer.seguridad=("si")

print(banncomer.botones)
print(banncomer.pantalla)
print(banncomer.dinero)
print(banncomer.cifras)
print(banncomer.codigo)
print(banncomer.usuario)
print(banncomer.cuenta)
print(banncomer.ticket)
print(banncomer.retiros)
print(banncomer.seguridad)