#generar codigo para interactuar
incio = input("ingrese el numero del piso al que desea subir: ")
 
#funcion int para relacionar cadenas y enteros.
if int(incio) <=10:
    print("Se encuentra en el piso ")

else: print("El número del piso ingresado es inválido") 
            
print( " " + incio + " ")

#variables para Subir o bajar en el ascensor
parte2 = input("Ingrese el numero del piso que quiere subir o bajar: ")
numero = 0

#funcion while para generar un bucle que funcione como ascensor
while numero <10:
    numero +=2
    print("numero")
    if int(parte2) < 5:
        print("Baja al piso")
    elif int(parte2) >5:
        print("Sube al piso")
    else: print("Usted encuentra en el piso 5")
    break

print("Se abre la puerta del Ascensor.")




