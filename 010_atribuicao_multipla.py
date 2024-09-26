print("Atribuição múltipla:\n")

print("Atribuição - Exemplo 1 :\n")
a = 10 
b = 5

print("a =", a)
print("b =", b, "\n")

a, b = b, a

print("Após a reatribuição:\n")
print("a =", a)
print("b =", b, "\n")


print("Atribuição - Exemplo 2:\n")
nome, sobrenome = "Rafaela", "Barezi"
print("nome =", nome)
print("sobrenome =", sobrenome,"\n")

nome, sobrenome = sobrenome, nome

print("Após a reatribuição:\n")
print("nome =", nome)
print("sobrenome =", sobrenome,"\n")

print("Atribuição - Exemplo 3:\n")

num1, num2, num3 = 2, 4, 8
print("num1 =", num1)
print("num2 =", num2)
print("num3 =", num3,"\n")

num1, num2, num3  = num1*2, num1+num2+num3, num1*num2*num3

print("Após a reatribuição:\n")
print("num1 =", num1)
print("num2 =", num2)
print("num3 =", num3, "\n")