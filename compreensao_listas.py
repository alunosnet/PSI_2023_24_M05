lista = [1,2,3,4,5]

lista_dobro=[n*2 for n in lista]
print(lista_dobro)

dobro=[]
for n in lista:
    dobro.append(n*2)
print(dobro)

dobro_pares=[n*2 for n in lista if n%2==0]
print(dobro_pares)
