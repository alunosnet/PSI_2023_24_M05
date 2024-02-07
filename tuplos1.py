import numpy as np

meu_tuplo=(1,2,3)

print(meu_tuplo)

print(meu_tuplo[0])

arr=np.zeros(3)
print(arr)
print(type(arr))
arr=meu_tuplo
print(arr)
print(type(arr))

arr=np.array(meu_tuplo)
print(arr)
