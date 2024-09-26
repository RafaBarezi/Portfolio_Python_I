print("Variáveis:\n")

inteiro = 5
decimal = 1.5
palavra = "Qualquer texto ou palavra (string)"

print(inteiro)
print("inteiro")
print(palavra,"\n")


print("Concatenando inteiro: %i" % inteiro)
print("Concatenando inteiro:", inteiro)
print("Concatenando inteiro: " + str(inteiro) + "\n")

print("Concatenando decimal:", decimal)
print("Concatenando decimal: %f" % decimal)
print("Concatenando decimal: %.7f" % decimal + "\n")

print("Concatenando strings:", palavra)
print("Concatenando strings: %s" % palavra)
print("Concatenando strings: " + palavra + "\n")