def participaFib(n):
    ult = 1
    pen = 1
    num = 0
    
    encontrou = 0
    
    if (n == 1) or (n == 2):
        encontrou = 1
    else:
        cont = 3
        while num <= n:
            num = ult + pen
            pen = ult
            ult = num
            cont += 1
            print(num)
            if(n == num):
                encontrou = 1
    
    if(encontrou):
        print("Valor pertence a sequencia de fibonacci")
    else:
        print("Valor nao pertence a sequencia de fibonacci")

n = int(input("Informe o número a ser verificado: "))
participaFib(n)