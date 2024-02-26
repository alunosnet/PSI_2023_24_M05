#converter dicionário numa lista
dicionario={'a':1,'b':2,'c':3}
lista=list(dicionario)
print(lista)
lista2=list(dicionario.items())
print(lista2)
#primeiro elemento da lista e o segundo elemento do tuplo
print(lista2[0][1])
lista3=list(dicionario.values())
print(lista3)

#converter string numa lista
nomes="nome1, nome2, mais um nome, ainda mais outro"
lista_nomes=nomes.split(",")
print(lista_nomes)