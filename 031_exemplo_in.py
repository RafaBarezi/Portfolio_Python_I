print("Exemplo com o operador in:\n")

a,b,c = 10, 20, 30
x = eval(input("Por favor, digite um n° >>>"))

if(x in [a, b, c]):
    print("\nO número digitado está contido\n")
else:
    print("\nO número digitado não está contido\n")

#Exemplo 2 

cores = ["azul", "vermelho", "verde", "amarelo"]

while True:
    cor = input("Por favor, digite o nome de uma cor básica ou digite sair para encerrar o programa >>> ")
    
    if(cor=="sair"):
        break 
    elif(cor in cores):
        print("A cor está contida\n")
    else:
        print("A cor não está contida\n")