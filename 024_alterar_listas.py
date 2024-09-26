print("Incluindo, alterando e excluindo elementos:\n")

lista_letras = ["aaa", "bbb", "ccc", "ddd"]
print(lista_letras)
print("\nIterando lista_letras:\n")
print(lista_letras[0])
print(lista_letras[1])
print(lista_letras[2])
print(lista_letras[3],"\n")

# Adicionando / substituindo ítens:
lista_letras.append("eee")
print("Adicionando eee com append:", lista_letras,"\n")

lista_letras[2] = "xxx"
print("Substituindo ccc por xxx:", lista_letras,"\n")

# Para excluir ítens se usa .clear():
lista_letras.clear()
print("Todos os ítens excluídos:",lista_letras,"\n")

# Para exclusão do último elemento:

lista_letras = ["aaa", "bbb", "ccc", "ddd", "eee"]
lista_letras.pop()
print("Exclusão do útimo elemento da lista:", lista_letras,"\n") 

# Para exclusão outros elementos da lista precisamos escolher o índice:

lista_letras.pop(0) 
print(lista_letras) 
lista_letras.pop(0) 
print(lista_letras)
lista_letras.pop(0) 
print(lista_letras) 
lista_letras.pop(0) 
print(lista_letras) 


# Usando a função del para deletar elementos:

lista_letras = ["aaa", "bbb", "ccc", "ddd", "eee"]
del(lista_letras[0:2]) 
print("\nRemover da posição a posição 2 (antes da letra b):", lista_letras,"\n")  

# Para remover posições aleatórias

lista_letras_2 = ["aaa", "bbb", "ccc", "ddd", "eee"]
del(lista_letras_2[::2]) 
print(lista_letras_2,"\n")  