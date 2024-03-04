'''
PSI - Módulo 5
Estruturas de Dados Compostas
Listas
'''
import random

super_heroes = ["Spider-Man","Iron Man","Captain America","Thor", "Hulk","Black Panther","Doctor Strange","Vision"]

super_vilains=["Magneto","Doctor Doom","Thanos","Loki","Galactus","Kingpin","Green Goblin","Venon"]

#Simular o combate entre um vilão e um herói
#Não repetir

while len(super_vilains)>0:
    heroi = random.choice(super_heroes)
    vilao = random.choice(super_vilains)
    print(f"Combate de {heroi} com {vilao}")
    combate=[heroi,vilao]
    ganha=random.choice(combate)
    print(f"Ganhou {ganha}")
    super_heroes.remove(heroi)
    super_vilains.remove(vilao)
