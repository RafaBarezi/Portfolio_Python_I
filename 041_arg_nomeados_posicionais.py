print("Argumentos nomeados vs argumentos posicionais:\n")

def dados_pessoais(nome, sobrenome, idade, país):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nPaís: {}\n".format(nome, sobrenome, idade, país))

dados_pessoais("Rafaela", sobrenome="Barezi", idade="36", país="Brasil")
dados_pessoais("Fernando", sobrenome="Barezi", idade="25", país="Brasil")
dados_pessoais("Mel", sobrenome="Barezi", idade="4", país="Brasil")