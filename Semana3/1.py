class Dias_a_segundos():
    
    #Nombre:Mishel Otero Mendoza
    #Grupo: tic's "21" fecha: 31/03/2021
    #Descripción:definimos cuantos dias a conertir después el bucle for para la formula.
        
   def dias(self):
       self.total_de_dias = int(input(":"))
       for formula in range(self.total_de_dias):
           ingresar = int(input("¿Cuantos dias a convertir: ".format(formula+1)<))
           convertir = ingresar*86400
           print("Esto equivale a segundos{}". format(convertir))
objeto = Dias_a_segundos()
objeto.dias()