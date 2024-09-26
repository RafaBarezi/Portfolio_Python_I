print("Comparando strings:\n")

print("a" > "X")
print("a" < "1")
print("r" > "M","\n")

print("O caractere de código 114 na tabela ASCII é:", (chr(114)),"\n")

print("A letra R está na",(ord("R")),"° posição da tabela ASCII\n")

for x in range(127): # Intervalo de 0 a 127
    print("O caractere", chr(x), "está na ", (ord(chr(x))), "° posição da tabela ASCII")
print()