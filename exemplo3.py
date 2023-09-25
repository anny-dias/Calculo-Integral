#Calculo do pi

def funcao(x):
    return (1-x**2)**0.5

inicio = -1 
fim = 1
delta = 0.0001
areazona = 0 

while inicio < fim:
    altura = funcao(inicio)
    base = delta 
    areazinha = base * altura
    areazona += areazinha
    inicio += delta
print(2 * areazona) 