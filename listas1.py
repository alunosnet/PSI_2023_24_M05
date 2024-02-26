lista_numeros=list(range(5))
print(lista_numeros)

print(type(lista_numeros))

lista_numeros_2=lista_numeros
print(id(lista_numeros))
print(id(lista_numeros_2))

lista_numeros_2[1]=-10
print(lista_numeros[1])

#copia os elementos
lista_numeros_2=lista_numeros[:]
lista_numeros_2[0]=100
print(lista_numeros)
print(lista_numeros_2)

#listar todos elementos
for x in lista_numeros:
    print(x)

#listar pelas posições
for i in range(len(lista_numeros)):
    print(lista_numeros[i])

#adicionar elementos
lista_numeros.append(1366)
print(lista_numeros)

#inserir um elemento no inicio da lista
lista_numeros.insert(0,"Viseu")
print(lista_numeros)

#juntar duas listas
lista_numeros.extend(["joaquim","maria",127])
print(lista_numeros)

#juntar duas listas com +
frutas=["maçã","laranja"]
arvores=["macieira","larangeira"]
juntar=frutas+arvores
print(juntar)
frutas[0]="banana"
print(juntar)

arvore=arvores.pop(1)
print(arvore)

print(lista_numeros)
del lista_numeros[1:4] #remove os elementos das posições 1,2,3
print(lista_numeros)

#remove todos elementos
lista_numeros=[]
arvores.clear()