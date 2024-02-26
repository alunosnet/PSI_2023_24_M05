#Fazer um programa que lê do utilizador os nomes dos sócios de dois clubes de futebol e REMOVE os nomes repetidos das duas listas

#Ler os sócios (função)
#Perguntar o nº de sócios ou terminar quando inserir um nome em branco
def LerNomes(lista):
    n=int(input("Indique o nº de sócios:"))
    for _ in range(n):
        nome=input("Indique um nome:")
        lista.append(nome)

#Comparar as duas listas
#percorrer um lista e verificar se o nome existe na outra
#se existir remover
def RemoveRepetidos(lista1,lista2):
    #remove os elementos que existem nas duas listas
    #for nomes in lista1[:]:
    for posicao in range(len(lista1)-1,-1,-1):
        if lista1[posicao] in lista2:
            lista2.remove(lista1[posicao])
            nome=lista1.pop(posicao)
            print(f"O nome {nome} foi removido das duas listas")

def main():
    #criar duas listas vazias
    clube1=[]
    clube2=[]
    #ler os dados para uma lista
    LerNomes(clube1)
    #ler os dados para outra lista
    LerNomes(clube2)
    print(clube1)
    print(clube2)
    RemoveRepetidos(clube1,clube2)
    print(clube1)
    print(clube2)

if __name__=="__main__":
    main()