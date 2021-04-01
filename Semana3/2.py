class grados_farenheit():
   #Nombre:Mishel Otero Mendoza
    #Grupo: tic's "21" fecha: 31/03/2021
    #Descripción:primero definimos la entrada cuantas temperaturas se van a convertir despues de eso se insertan, el comando append es pasa un listado y poderlo suman
    def ingresar (self):
        self.inicio = int(input("¿Cuantas temperaturas se tiene que calcular?: "))
        las_tres_tempreaturas = []
        base = 0
        for formula in range(self.inicio):
            C = int(input("Temperatura en Grados Celsius: ".format(formula + 1)))
            las_tres_tempreaturas.append(C)
            base += C
        convertir = (base/self.inicio) * 1.8 + 32
        print("Resultado Farenheit {}".format(convertir))


objeto = grados_farenheit()
objeto.ingresar()