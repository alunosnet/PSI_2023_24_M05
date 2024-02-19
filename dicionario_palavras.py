"""Dado uma frase, crie um dicionário que mapeia cada palavra à sua contagem de ocorrências na frase."""
#ler a frase
frase=input("Frase:")
#retirar os espaços em branco no inicio e no fim
frase=frase.strip()
#adicionar um espaço em branco no final
frase += " "
#criar um dicionário vazio
dicionario = {}
palavra=""
for letra in frase.lower():
    if letra!=" ":
        palavra = palavra + letra
    else:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
        palavra=""

print(dicionario)