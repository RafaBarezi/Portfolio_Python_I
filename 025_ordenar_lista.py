print("Ordenamento de listas:\n")

lista_nomes = ["Rafaela", "Fernando", "Mel"]

# Para imprimir a lista completa iterando:
for a in lista_nomes:
    print(a)

# Reverse define que a lista deve ser lida de traz pra frente:
lista_nomes.reverse() 
print("\nlista de nomes ao contrário", lista_nomes,"\n")

# Para ordenar de forma ascendente se usa o short:
lista_nomes.sort() 
print("lista em ordem alfabética:", lista_nomes,"\n") 
lista_nomes.sort(reverse=True) 
print("lista de nomes em ordem alfabética reversa:", lista_nomes,"\n")  