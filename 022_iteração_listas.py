print("Iteração de listas:\n")

lista_num= [000, 100, 200, 300, 400]
print(lista_num)
print("\nlista iterada:\n")

for x in lista_num:   
    print(x)

lista_num2 = [000, 100, 200, 300, 400,500]
lista_index = [0, 1, 2, 3, 4, 5] # Cada um desses é uma posição
for x in lista_index:
    lista_num2[x] += 50
print("\nIterando com o índice:", lista_num2,"\n")

for x in range(3):  
    lista_num2[x] += 10
print("Iterando com range, adicionando 10 apenas em 3 ítens:", lista_num2,"\n")

for x in range(len(lista_num)):  
    lista_num2[x] += 50
print("Iterando com range, adicionando 50 em todos os ítens anteriores:",lista_num2,"\n")

# Iterando com enumerate

list_A = ["aaa", "eee", "iii", "ooo", "uuu"]
enumerate(list_A)
print(list_A,"\n")
list(enumerate(list_A))
print(list(enumerate(list_A)))
print("\n")

list_B = [0, 1, 2, 3, 4]
for lista_indexada, y in enumerate(list_B):   
    list_B[lista_indexada] += 100
print("Adicionando 100 em todos os ítens através do enumerate:",list_B,"\n")