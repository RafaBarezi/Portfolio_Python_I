print("Fatiando Strings:\n")

S = "Para o python, toda string é imutável!"
print(S)

print("Imprimindo apenas um ítem:", S[22],"\n")

print(type(S))
print(type(S[22]))
print((S[-1]),"\n") 

# Para cortes nas strings:

print(S[0:14])
print(S[15:26])
print(S[27:37],"\n")

# Para inversão
print(S[::-1],"\n")

# Para saltar caracteres:
print(S[::3],"\n")