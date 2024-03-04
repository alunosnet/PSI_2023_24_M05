"""
Faça um programa que tenha uma função notas() que recebe várias notas de um aluno e retorna um dicionário com as seguintes informações:
Número de notas;
A melhor nota;
A pior nota;
A média das notas;
A situação: APROVADO se média maior ou igual a 10 e REPROVADO nos restantes casos.
"""

def notas(notas_aluno):
    aluno={}
    aluno['numero_notas']=len(notas_aluno)
    aluno['melhor_nota']=max(notas_aluno)
    #v2
    """melhor_nota=notas_aluno[0]
    for n in notas_aluno:
        if n>melhor_nota:
            melhor_nota=n
    aluno['melhor_nota']=melhor_nota
    """
    aluno['pior_nota']=min(notas_aluno)
    media=sum(notas_aluno)/len(notas_aluno)
    aluno['media_notas']=media
    aluno['situacao'] = "Aprovado" if media>=10 else "Reprovado"
    return aluno

def main():
    notas_aluno=[10,13,7,14]
    aluno=notas(notas_aluno)
    print(aluno)

if __name__=='__main__':
    main()