import numpy as np

# Função que permite ao utilizador adicionar um livro
# O livro novo estará sempre disponivel
# Verifique se ainda existe espaço no array antes de adicionar
# Tenha atenção para não repetir o id do livro
def adicionar_livro():
    pass

# Função para mostrar os livros
# deve permitir escolher se lista todos ou só os disponíveis ou só os indisponíveis
def listar_livros():
    pass

# Função que muda o estado do livro e regista o nome do leitor
def emprestar_livro():
    pass

#Função que torna o livro disponível e apaga o nome do leitor
def devolver_livro():
    pass

#Função que apresenta as opções ao utilizador e devolve a sua escolha
def menu():
    pass

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
    #continuar aqui

# Ponto de entrada do programa (main loop)
if __name__ == "__main__":
    main()
