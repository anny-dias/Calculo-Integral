import math
def funcao(x):
    return math.exp(-x**2)
inicio = -3
fim = 3
delta = 0.0001
areazona = 0
while inicio < fim:
    altura = funcao(inicio)
    base = delta
    areazinha = base*altura
    areazona += areazinha
    inicio += delta
print(areazona)
print((math.pi**0.5))