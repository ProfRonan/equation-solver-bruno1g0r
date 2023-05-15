grau = int(input("Digite o grau da função"))
if(grau <1 or grau >2):
    print("Grau inválido.")
elif(grau == 1):
    print("A equação é do primeiro grau.")
    a = float(input("digite o valor de a"))
    if(a == 0):
        print("Valor inválido.")
    elif(a != 0):
        b = float(input("digite o valor de b"))
        raiz= (-1*b)/a
        print(round(raiz,2))
elif(grau == 2):
    print("A equação é do segundo grau.")
    a = float(input("digite o valor de a"))
    if(a == 0):
        print("Valor de a inválido")
    elif(a != 0):
        b = float(input("digite o valor de b"))
        c = float(input("digite o valor de c"))
        delta = (b*b)+(-4*a*c)
        if(delta < 0):
            print("A equação não possui raizes reais")
        elif(delta == 0):
            print("A equação possui uma raiz real")
            raiz = (-1*b)/(2*a)
            print(round(raiz,2))
        elif(delta > 0):
            print("A equação possui duas raízes reais")
            raiz1 = ((-1*b)+(delta**(1/2)))/(2*a)
            raiz2 = ((-1*b)-(delta**(1/2)))/(2*a)
            if(raiz1>raiz2):
                print(round(raiz1,2))
                print(round(raiz2,2))
            elif(raiz1<raiz2):
                print(round(raiz2,2))
                print(round(raiz1,2))
            
