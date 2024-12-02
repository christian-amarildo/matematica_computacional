def exponencial(valor, expoente):
    for i in range(1,expoente):
        valor *= valor
    return valor 

def somatorio(n,x):
    soma = 0
    for x in range(1,n+1):
        soma += x
    return soma

n= int(input("insira o valor de n: "))
x= int(input("insira o valor de x: "))

