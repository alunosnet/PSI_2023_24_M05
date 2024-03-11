
animais = {
    ("cão","pitbull"):{"idade":5,"dono":"joaquim"},
    ("gato","siames"):{"idade":2,"dono":"carla"},
    ("cão","cão de água"):{"idade":3,"dono":"joaquim"},
    ("cobra","não sei"):{"idade":1,"dono":"joao"},
    ("cão","bulldog"):{"idade":3,"dono":"maria"},
}

#print dos animais do joaquim
print("Os animais do joaquim:")
for chave,valor in animais.items():
    if valor["dono"]=="joaquim":
        print(f"Especie: {chave[0]} Raça: {chave[1]} Idade: {valor['idade']}")

#listar quantos animais há por cada especies
contagem={}
for chave in animais.keys():
    especie=chave[0]
    #verificar se a especie existe no dicionário
    if especie in contagem:
        contagem[especie] += 1
    else:
        contagem[especie] = 1
print(contagem)

#mostrar o animal mais velho
mais_velho=0
o_mais_velho=None
for chave,valor in animais.items():
    if valor["idade"]>mais_velho:
        mais_velho=valor["idade"]
        o_mais_velho=chave
print(f"O animal mais velho encontrado foi {o_mais_velho} com a idade de {mais_velho}")

#média de idades dos animais
soma=0
for valor in animais.values():
    soma = soma + valor['idade']
media = soma / len(animais)
print(f"A média das idades dos animais é de {media}")

#mostrar os animais com idade superior à média
for chave, valor in animais.items():
    if valor['idade']>media:
        print(f"Animal com idade superior à média: {chave}")

#percentagem de animais por espécie
for chave, valor in contagem.items():
    percentagem = valor/len(animais) * 100
    print(f"A espécie {chave} representa {percentagem}% de animais")