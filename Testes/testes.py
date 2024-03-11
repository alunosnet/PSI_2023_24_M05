import funcoes

try:
    #testar se a média de 10 e 20 é igual a 15
    r = funcoes.Media(10,20)
    assert r==15, "Média está errada"
    print("Passou no primeiro teste")
    r = funcoes.Media(-1,-1)
    assert r is None, "Média está errada com valores negativos"
    print("Passou no segundo teste")
except AssertionError as e:
    print(f"Erro na execução do teste - {e}")
else:
    print("A função passou no teste")
finally:
    print("Teste terminado")