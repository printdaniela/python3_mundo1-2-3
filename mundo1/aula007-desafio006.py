#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número:'))
d = n*2
t = n*3
rq = n**(1/2)
print(f'O dobro do número digitado é {d}, seu triplo é {t} e o valor de sua raiz quadrada é {rq:.2f}.')