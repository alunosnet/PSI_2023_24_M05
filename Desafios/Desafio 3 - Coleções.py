'''
PSI - Módulo 5
Estruturas de Dados Compostas
Coleções
'''

# Estrutura de dados
Disciplina_PSI={
                  'Modulos': ('Algoritmia','Estruturas de Controlo','Funções','Estruturas de Dados Estáticas'),
                  'WebGrafia':{'3wschool.com','github.com/alunosnet','udacity.com'} ,
                  'Aulas':['M1','M1','M1','M2','M2','M3','M3','M4','M4','M4','M4'],
                  'Avaliação':['Teste Escrito','Teste prático','Teste prático','Teste prático']
               }

# Mostrar os sites recomendados para a disciplina (webgrafia)
print(Disciplina_PSI["WebGrafia"])
#ou
for elemento in Disciplina_PSI['WebGrafia']:
    print(elemento)
# Mostrar o nome de um módulo pela posição (pedir ao utilizador)
posicao=int(input("Qual o módulo (1-4)? "))
print(Disciplina_PSI['Modulos'][posicao-1])

# Mostrar as aulas que são dadas num módulo (pedir ao utilizador o nº do módulo)
modulo=int(input("Qual o nº módulo (1-4)?"))
modulo = f"M{modulo}"
aulas = Disciplina_PSI['Aulas']
for aula in aulas:
    if modulo==aula:
        print(aula)

# Mostrar os módulos que tenham determinado conteudo (pedir ao utilizador)
conteudo=input("Qual o conteúdo? ")
modulos=Disciplina_PSI['Modulos']
for modulo in modulos:
    if conteudo.lower() in modulo.lower():
        print(modulo)

# Mostrar os módulo cuja avaliação não é 'Teste Escrito'
avaliacoes=Disciplina_PSI['Avaliação']
for avaliacao in avaliacoes:
    if avaliacao!="Teste Escrito":
        print(avaliacao)
#ou
testes=[avaliacao for avaliacao in avaliacoes if avaliacao!="Teste Escrito"]
print(testes)
# Mostrar o nº de módulos da disciplina
print(len(Disciplina_PSI['Modulos']))

# Adicionar mais 5 aulas do módulo M2
for _ in range(5):
   Disciplina_PSI['Aulas'].append("M2")
#ou
aulas_novas=["M2","M2","M2","M2","M2"]
Disciplina_PSI['Aulas'].extend(aulas_novas)
print(Disciplina_PSI['Aulas'])
#ou Gustavo Cruz
Disciplina_PSI['Aulas'].extend(["M2"]*5)
print(Disciplina_PSI['Aulas'])
# Adicionar uma chave nova para classificacoes que deve corresponder a uma lista de 4 notas indicadas pelo utilizador
Disciplina_PSI['classificacoes']=[]
for _ in range(4):
    nota=int(input("Nota: "))
    Disciplina_PSI['classificacoes'].append(nota)
print(Disciplina_PSI['classificacoes'])
print(Disciplina_PSI)