print("Operadores in - not in:\n")

print("2 está contido em (1, 2, 3, 4)?",2 in (1, 2, 3, 4, 5))
print("2 está NÃO contido em (1, 2, 3, 4)?",2 not in (1, 2, 3, 4, 5))

lista = ["a", "b", "c", "d", "e"]
print("lista:",lista)
print("c está contido em lista?", "c" in lista)

lista = ["a", "b", "c", "d", "e"]
print("lista:",lista)
print("r está NÃO contido em lista?", "r" not in lista,"\n")

7 in range(1, 10 ,1)
print("12 está NÃO contido no range [1, 2, 3, 4, 5, 6, 7, 8, 9]?", 12 not in range (1, 10 ,1),"\n")

1 in range(1, 7 ,3)
print("1 está contido no range [1, 7]?", 1 in range (1, 7 ,3))

X = range(1, 9, 1)
if(5 in X):
    print("X = range(1, 9, 1): 5 está contido em X\n")
else:
    print("X = range(1, 9, 1): 5 NÃO está contido em X\n")