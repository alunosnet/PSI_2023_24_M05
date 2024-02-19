#programa para gerir alunos
#-um array com 100 posições para os alunos
#-adicionar alunos
#-listar todos
#-pesquisar alunos
#-editar alunos
#-um array com 100 posições para notas
import numpy as np

#função para adicionar um aluno novo
def AdicionarAluno():
    nome=input("Nome:")
    idade=int(input("Idade:"))
    morada=input("Morada:")
    email=input("Email:")
    novo={'nome':nome,'idade':idade,'morada':morada,'email':email}
    return novo

#função para listar todos os alunos
def ListarTodos(alunos,nr_alunos):
    for i in range(nr_alunos):
        #print(f"Nome:{alunos[i]['nome']}")
        aluno = alunos[i]
        for chave,valor in aluno.items():
            print(f"{chave} : {valor}")

#função para pesquisar um aluno com base nome
def Pesquisar(alunos,nr_alunos):
    #pedir o nome a pesquisar
    nome = input("Nome do aluno:")
    for i in range(nr_alunos):
        if alunos[i]['nome']==nome:
            #print(alunos[i])
            #break
            return alunos[i]
    return None

#função para pesquisar o aluno e devolve a posição no array
def PesquisarPosicao(alunos,nr_alunos):
    #pedir o nome a pesquisar
    nome = input("Nome do aluno:")
    for i in range(nr_alunos):
        if alunos[i]['nome']==nome:
            return i
    return None


#função para alterar os dados de um aluno
#função para adicionar notas

#função para ler uma opção do utilizador
def menu():
    print("1. Adicionar aluno\n2.Listar todos\n3. Editar\n4.Pesquisar\n5.Adicionar Nota\n6. Sair")
    op=input(":")
    return op

def ListarNotas(notas,alunos,nr_notas):
    for i in range(nr_notas):
        print(f"Nota: {notas[i][0]}")
        print(f"Aluno: {alunos[notas[i][1]]['nome']}")

def main():
    MAX_ITEMS=100
    #array para os dados dos alunos
    alunos=np.empty(MAX_ITEMS,dtype=object)
    nr_alunos=0
    FORMA=(MAX_ITEMS,2)
    #array 2D para os dados das notas
    notas=np.zeros(FORMA,'i')
    nr_notas=0
    #menu
    while True:
        op = menu()
        if op=='1':
            if nr_alunos==MAX_ITEMS:
                print("Não tem mais espaço disponível")
                continue
            aluno=AdicionarAluno()
            alunos[nr_alunos]=aluno
            nr_alunos = nr_alunos + 1
        elif op=='2':
            ListarTodos(alunos,nr_alunos)
        elif op=='4':
            aluno=Pesquisar(alunos,nr_alunos)
            if aluno is not None:
                print(aluno)
            else:
                print("Não existe nenhum aluno com esse nome")
        elif op=='3':
            aluno=Pesquisar(alunos,nr_alunos)
            if aluno is not None:
                #nome
                aluno['nome']=input(f"Nome atual ({aluno['nome']}):")
                #morada
                aluno['morada']=input(f"Morada atual ({aluno['morada']}):")
                #email
                aluno['email']=input(f"Email atual ({aluno['email']}):")
                #idade
                aluno['idade']=int(input(f"Idade atual ({aluno['idade']}):"))
            else:
                print("Não existe nenhum aluno com esse nome")
        elif op=='5':
            #Adicionar notas dos alunos
            posicao_aluno=PesquisarPosicao(alunos,nr_alunos)
            if posicao_aluno is None:
                print("O nome indicado não existe")
            else:
                nota=int(input("Qual a nota do aluno:"))
                #guardar
                notas[nr_notas][0]=nota
                notas[nr_notas][1]=posicao_aluno
                nr_notas = nr_notas + 1
                ListarNotas(notas,alunos,nr_notas)
        elif op=='6':
            break

if __name__=='__main__':
    main()