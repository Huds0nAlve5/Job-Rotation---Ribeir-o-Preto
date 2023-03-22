def reverterString(s):
    tam = len(s)
    listaNovaString = []
    x = 0
    
    for i in range(tam):
        listaNovaString.append(s[tam-1-x])
        x += 1
        
    stringInversa = ''.join(listaNovaString)
    print(stringInversa)
    
s = "Flamengo"
reverterString(s)