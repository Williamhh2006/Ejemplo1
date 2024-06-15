not1 = int(input("Ingrese el primer nota \n"))
not2 = int(input("Ingrese el segundo nota \n"))
not3 = int(input("Ingrese el tercer nota \n"))
not4 = int(input("Ingrese el cuarto nota \n"))
prome=((not1+not2+not3+not4)/4)
if (prome<11):
        print ("F")
elif (prome<21):
        print ("E")
elif (prome<31):
        print ("D")
elif (prome<41):
        print ("C")
elif (prome<51):
        print ("B")
else:
        print ("A")
