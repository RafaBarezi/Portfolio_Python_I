print("Funções em dicionários:\n")

tel = {
    10101010 : "Rafaela",
    30303030 : "Fernando",
    50505050 : "Mel"
}
print(tel)

# Função len:
print("\nA lista tem",len(tel),"elementos")

# Função del, para excluir ítens:
del(tel[30303030])
print("\n",tel)

# Para exibir apenas as chaves ou somente as listas: 

print("\nAs chaves do dicionário são:",(tel.keys()))

print("\nOs valores do dicionário são:",(tel.values()))

# Exibir ítens isolados:
print("\nPara localizar chave isoladamente:",(tel[10101010]))
print("\nPara localizar chave isoladamente:",(tel[50505050]))

#Retornando com o get:
print("Usando a função get:",tel.get(50505050))

tel2 = {
    10101010 : "Rafaela",
    30303030 : "Fernando",
    50505050 : "Mel "
}

print(tel2.popitem(),"\n")
print(tel2.popitem(),"\n")
print(tel2.popitem(),"\n")

print("Após excluir todos os ítens da lista:", tel2,"\n")

tel3 = {
    10101010 : "Rafaela",
    30303030 : "Fernando",
    50505050 : "Mel "
}

print("50505050 está contido na lista?:",50505050 in tel3)
print("80808080 está contido na lista?:",80808080 not in tel3,"\n")

# Usamos o update para adicionar elementos de um dicionário em um outro:
nova_lista = {11111: "teste01", 22222: "teste02", 33333: "teste03"}

tel3.update(nova_lista)
print("lista tel3 somada com a lista nova_lista", tel3,"\n")

# Adicionando elemento a uma trupla 
tipo_tupla = (10,10,10,10)
tel3[tipo_tupla] = "teste"
print(tel3)