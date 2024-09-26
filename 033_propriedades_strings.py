print("Propriedades das String\n")

s = "lista de caracteres, trabalhando com strings"
print(s,"\n")
print("Quantidade de caracteres da frase lista de caracteres:", len(s),"\n")
print("A 16° letra é:", s[16],"\n")

# Uma forma de alterar algo na string seria cortando ela e remonantando novamente: 
s.split(" ")
print(s.split(" "),"\n")

lista = s.split(" ")
print(lista[0],lista[1], lista[2],"\n")

l = "lista de caracteres, trabalhando com strings"
print(l,"\n")
l.replace("com", "")
print(l.replace("com", ""),"\n")

# Para saber qual é a string manuseada podemos verificar o id da string:

print(id(s))
print(id(l.replace("com", "")))
print()