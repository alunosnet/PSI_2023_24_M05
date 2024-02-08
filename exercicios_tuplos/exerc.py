#1 
meses =("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")

#2
print(meses[2])

#3
verao=meses[5:8]
print(verao)

#4
if "Junho" in meses:
    print("Tem junho")
else:
    print("Não tem junho")

#5
cores_primarias=("Vermelho","Verde","Azul")
cores_secundarias=("Laranja","Violeta","Amarelo")
todas_cores=cores_primarias+cores_secundarias
print(todas_cores)

#6
print(todas_cores * 3)

#7
tuplo=("a",1,2,3,"a")

#8
print(todas_cores.index("Verde"))

#9
palavras=("ola","maria","adeus")
soma=0
for elemento in palavras:
    n = elemento.count('a')
    soma += n
print(soma)

#10
n = (33,21,10,-5)
n_ordenados=sorted(n)
print(n_ordenados)
