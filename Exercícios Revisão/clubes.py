def ler_nomes(lista):
    while True:
        nome=input("Nome:")
        if nome:
            lista.append(nome)
        else:
            break

clube1=[]
clube2=[]
print("Nomes do clube 1")
ler_nomes(clube1)
print("Nomes do clube 2")
ler_nomes(clube2)

#lista com nomes repetidos
repetidos=[]
for nome in clube1:
    if nome in clube2:
        repetidos.append(nome)

#remover os repetidos do clube pretendido
for nome in repetidos:
    op = input(f"{nome} pretende ficar no clube 1 ou 2?")
    if op=="1":
        clube2.remove(nome)
    else:
        clube1.remove(nome)

#ordernar as listas
clube1.sort()
clube2.sort()
repetidos.sort()
print(f"Clube 1:{clube1}, Clube 2: {clube2} e repetidos: {repetidos}")