print("Fatiando listas (Slicing):\n")

lista = ["p","y","t","h","o","n"]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5],"\n")

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])
print(lista[-6],"\n")

print("Imprimindo [0, 1, 2[:", lista[:2]) # ['p', 'y']
print("Imprimindo [2, 3, 4, 5]:", lista[2:]) # ['t', 'h', 'o', 'n']

print("\nDefinindo apenas o step, de pois em 2:", lista[::2]) 
print("\nDefinindo apenas o step, com passo invertido", lista[::-1])  
print("\nDefinindo inicio e step", lista[2::2],"\n") 