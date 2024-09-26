print("Class List III:\n")

lista = [1, 2, 3, 4]
# Adicionar um novo ítem a lista:
lista = lista + [5, 6, 7, 8, 9]+[12]
print(lista,"\n")
# Adicionar elementos no inicio da lista:
lista =  [0]+lista
print(lista,"\n")
# Adicionar elementos no fim da lista:
lista.append(15)
print(lista,"\n")
lista.append(22)
print(lista,"\n")

# Adicionar elementos iguais usando multiplicação na lista:
print(5*["Rafaela"],"\n")

# Adicionar elementos diferentes usando multiplicação:
lista += (3*["oi"])
print(lista,"\n")

# Excluir índices da lista (Deletando o n° 0 da lista):
del(lista[0])
print(lista,"\n")

# (Deletando o 10 da lista):
del(lista[9])
print(lista,"\n")

# (Deletando a sublista [10] da lista):
del(lista[9])
print(lista,"\n")