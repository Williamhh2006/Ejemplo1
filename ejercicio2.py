n = int(input("Ingrese el total de la factura \n"))
if n < 9999:
    print("Gracias por la compra")
else:
    comi= n*0.05
    print("Usted tiene que paga la comision, en total sera",comi)
    