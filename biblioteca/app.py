import numpy as np

# Função que permite ao utilizador adicionar um livro
# O livro novo estará sempre disponivel
# Verifique se ainda existe espaço no array antes de adicionar
# Tenha atenção para não repetir o id do livro
def adicionar_livro(livros,nr_livros):
    if nr_livros==len(livros):
        print("Não é possível adicionar mais livros.")
        return
    #ler os dados do livro
    titulo=input("Título:")
    disponivel=True
    nome_leitor=""
    id=livros[nr_livros-1]["id_livro"] + 1
    livros[nr_livros]={"id_livro":id,"titulo":titulo,"disponivel":disponivel,"nome_leitor":nome_leitor}
    nr_livros = nr_livros + 1
    return nr_livros

# Função para mostrar os livros
# deve permitir escolher se lista todos ou só os disponíveis ou só os indisponíveis
def listar_livros(livros,nr_livros):
    op = input("1. Listar todos\n2. Listar disponíveis\n3. Listar indisponíveis: ")
    if op=="1":
        for i in range(nr_livros):
            for chave, valor in livros[i].items():
                print(f"{chave} - {valor}")
            print("#"*20)
    if op=="2" or op=="3":
        escolha = True if op=="2" else False
        for i in range(nr_livros):
            if livros[i]['disponivel']==escolha:
                for chave, valor in livros[i].items():
                    print(f"{chave} - {valor}")
                print("#"*20)

# Função que muda o estado do livro e regista o nome do leitor
def emprestar_livro(livros,nr_livros):
    #pedir o id do livro
    id = int(input("Id do livro a emprestar: "))
    #verificar se o id existe e se o livro está disponível
    for i in range(nr_livros):
        if livros[i]["id_livro"]==id:
            if livros[i]["disponivel"]==False:
                print("Esse livro não está disponível")
            else:
                #pedir o nome do leitor
                nome=input("Nome do leitor:")
                #alterar o estado do livro
                livros[i]["disponivel"]=False
                #registar o nome do leitor
                livros[i]["nome_leitor"]=nome
            return
    print("Não existe um livro com o id indicado")

#Função que torna o livro disponível e apaga o nome do leitor
def devolver_livro(livros,nr_livros):
    #pedir o id do livro
    id = int(input("Id do livro a emprestar: "))
    #verificar se o id existe e se o livro está disponível
    for i in range(nr_livros):
        if livros[i]["id_livro"]==id:
            if livros[i]["disponivel"]==True:
                print("Esse livro não está emprestado")
            else:
                #alterar o estado do livro
                livros[i]["disponivel"]=not livros[i]['disponivel']
                #remover o nome do leitor
                livros[i]["nome_leitor"]=""
            return
    print("Não existe um livro com o id indicado")

#Função que apresenta as opções ao utilizador e devolve a sua escolha
def menu():
    while True:
        print("1. Adicionar\n2.Listar\n3.Emprestar\n4.Devolver\n5.Sair")
        op = int(input(":"))
        if op <1 or op >5:
            print("Essa opção não é válida")
        else:
            return op

#função para gerar (seed) dados iniciais
def inicializar(livros):
    livros[0]={"id_livro":1,"titulo": "Dom Quixote", "disponivel": True,"nome_leitor":""}
    livros[1]={"id_livro":2,"titulo": "A Arte da Guerra", "disponivel": True,"nome_leitor":""}
    livros[2]={"id_livro":3,"titulo": "1984", "disponivel": True,"nome_leitor":""}
    livros[3]={"id_livro":4,"titulo": "Os Lusíadas", "disponivel": True,"nome_leitor":""}
    livros[4]={"id_livro":5,"titulo": "A Metamorfose", "disponivel": True,"nome_leitor":""}
    return 5

def main():
    MAX_ITEMS=100
    livros =np.empty(MAX_ITEMS,dtype=object)
    nr_livros=inicializar(livros)
    op = 1
    while op!=5:
        op = menu()
        if op==1:
            nr_livros=adicionar_livro(livros,nr_livros)
        elif op==2:
            listar_livros(livros,nr_livros)
        elif op==3:
            emprestar_livro(livros,nr_livros)
        elif op==4:
            pass
    print("Obrigado por utilizar o meu programa")

# Ponto de entrada do programa (main loop)
if __name__ == "__main__":
    main()
