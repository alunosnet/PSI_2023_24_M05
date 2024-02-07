
carros=("ford","ferrari","bmw","vw","ford")
print(carros.count("ford"))

def ler_Carros():
    carro1=input("Carro:")
    carro2=input("Carro:")
    carro3=input("Carro:")
    meu_tuplo=(carro1,carro2,carro3)
    return meu_tuplo

carros=ler_Carros()
c1,c2,c3=carros
print(c1)