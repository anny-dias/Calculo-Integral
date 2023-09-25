def funcao(x):
    return x**2/2 + x**4/3 - x/6
delta = 0.0001
inicio = -1
fim = 7
areazona = 0
while inicio < fim:
    altura = funcao(inicio)
    base = delta
    areazinha = base*altura
    areazona += areazinha
    inicio += delta
print(areazona)
print(7**3/6 - (-1)**3/6 + 7**5/15 - (-1)**5/15 - 7**2/12 + (-1)**2/12)