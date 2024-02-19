dicionario = {'frança':'paris','espanha':'madrid','portugal':'lisboa'}

for pais,capital in dicionario.items():
    print(f"A capital de {pais} é {capital}")

#adicionar novo
pais=input("Novo país:")
capital=input("Capital: ")
dicionario[pais]=capital
print(dicionario)

#procurar a capital de um país
pais=input("País a pesquisar:")
if pais not in dicionario:
    print("Esse país não existe")
else:
    print(f"A capital do {pais} é {dicionario[pais]}")

#versão 2
capital = dicionario.get(pais,"Esse país não existe")
print(capital)

#procurar o país de uma capital
capital=input("Qual a capital do pais a pesquisar:")
if capital not in dicionario.values():
    print("Essa capital não existe")
else:
    for pais, cap in dicionario.items():
        if cap == capital:
            print(pais)