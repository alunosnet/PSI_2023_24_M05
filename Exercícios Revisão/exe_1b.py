numeros=[]

#ler as 10 notas
for _ in range(10):
    nota=float(input("Nota: "))
    numeros.append(nota)

#mostrar as notas por ordem inversa
for pos in range(len(numeros)-1,-1,-1):
    print(numeros[pos])

contar_negativos=0
for x in numeros:
    if x<0:
        contar_negativos += 1

perc_negativos=contar_negativos/len(numeros)*100
print(f"% de negativos: {perc_negativos:.2f}")
print(f"% de positivos: {100-perc_negativos:.2f}")