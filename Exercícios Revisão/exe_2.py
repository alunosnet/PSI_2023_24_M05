notas=[10,15,15,10]

#Média
media=sum(notas)/len(notas)

#média v2
soma=0
for x in notas:
    soma = soma + x
    #mostrar nota
    print(f"{x=}")
media=soma/len(notas)

#mostrar a média
print(f"{media=}")

#percentagem de negativas
negativas=0
for x in notas:
    if x<10:
        negativas += 1

perc_negativas=negativas/len(notas)*100
perc_positivas=100-perc_negativas
print(f"{perc_negativas=} {perc_positivas=}")

#melhor nota
melhor=notas[0]
for x in notas:
    if x>melhor:
        melhor=x
print(f"{melhor=}")