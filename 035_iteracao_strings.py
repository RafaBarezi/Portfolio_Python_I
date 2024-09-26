print("Iteração das strings:\n")

# Primeira forma:
string_1 = "Iterando"
for x in string_1:
    print(x)
print()

# Segunda forma:
string_2 = "Nova iteração"
index = 0 
while index < len(string_2):
    print(string_2[index])
    index +=1 
print()

# Terceira forma 
for chave, valor in enumerate("Iterando strings"): 
    print(chave, valor)
print("\n",enumerate("Iterando strings"),"\n") 
print(dict(enumerate("Iterando strings")),"\n")