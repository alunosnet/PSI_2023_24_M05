"""3.	Jogo de dados em Python. Crie um programa onde 4 jogadores joguem um jogo de dados. Cada jogador lança o dado 6 vezes e o programa deve guardar os resultados num dicionário em que o nome do jogador é a chave. No final o programa deve indicar quem ganhou o jogo que corresponde ao jogador com o total de valores mais elevado. O valor do lançamento do dado deve ser simulado com a library random.
"""
import random

def LancarDados():
    n = random.randint(1,6)
    return n

def JogadorLancarDados():
    jogador={}
    #nome
    nome=input("Introduza o nome do jogador:")
    jogador['nome']=nome
    #lançamentos
    lista_lancamentos=[]
    for _ in range(6):
        lista_lancamentos.append(LancarDados())
    jogador['lancamentos']=lista_lancamentos
    return jogador

jogadores=[]

for _ in range(4):
    jogadores.append(JogadorLancarDados())

#TODO: terminar aqui
maior=sum(jogadores[0]['lancamentos'])
for jogador in jogadores:
    if sum(jogador['lancamentos'])>maior:
        maior=sum(jogador['lancamentos'])
        

print(jogadores)