color1 = input("Ingrese el primer color: ")
color2 = input("Ingrese el segundo color: ")
if (color1 == "verde" and color2 == "azul") or (color1 == "azul" and color2 == "verde"):
        print ("Cian")
elif (color1 == "verde" and color2 == "rojo") or (color1 == "rojo" and color2 == "verde"):
        print ("Amarillo")
else:
        print ("Combinación no válida")