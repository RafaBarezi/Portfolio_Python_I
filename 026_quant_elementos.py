print("Quantidade de elementos:\n")

lista_nomes = ["Rafaela","Fernando", "Mel"]
print(lista_nomes,"\n")
len(lista_nomes)
print("Para mostrar quantidade de ítens:",len(lista_nomes),"\n")

# Para acessar o penúltimo objeto da lista:
print("O penúltimo ítem da lista é:",lista_nomes[len(lista_nomes)-2],"\n")

# Para inserir elementos na lista:
lista_nomes.insert(1, "Mel") 

print("Inserindo Mel na lista",(lista_nomes),"\n")
lista_nomes.insert(0, "Mel") 

print("Inserindo Mel na lista outra vez",(lista_nomes),"\n")

# Para saber quantas vezes o elemento está na lista:

lista_nomes.count("Mel")
print("Quantidade de vezes que Mel aparece na lista:", lista_nomes.count("Mel"),"\n")  

lista_nomes.count("Rafaela")
print("Quantidade de vezes que Rafaela aparece na lista:", lista_nomes.count("Rafaela"),"\n")

# Quando se deseja saber qual o índice (posição) de um deteminado ítem na lista:

lista_nomes.index("Mel") 
print("Mel está na posição:", lista_nomes.index("Mel"),"\n") # Só mostra a posição da primeira vez que o ítem repetido aparece

lista_nomes.index("Rafaela") 
print("Rafaela está na posição:", lista_nomes.index("Rafaela"),"\n")  

lista_nomes.index("Fernando") 
print("Fernando está na posição:", lista_nomes.index("Fernando"),"\n")