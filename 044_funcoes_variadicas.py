print("Funções variádicas:\n") 

def lista_argumentos(*lista):
    print(lista,"\n")

lista_argumentos(0, 1, 2, 3, 4)
lista_argumentos("zero", "um", "dois", "três", "quatro")
lista_argumentos(2==2, 2!=2, 3!=2, 3==2)
lista_argumentos(3.14, 1988)

lista1 = ["a","b","c","d","e"]
lista_argumentos(lista1)

dict = {}
dict ["key01"] = "elemento1"
dict ["key02"] = "elemento2"
dict ["key03"] = "elemento3"
lista_argumentos(dict)

tupla = "abc", 7, "Rafaela", 3.14, True
lista_argumentos(tupla)

# exemplo 2

def lista_argumentos_associativos(**dicionario):
    print(dicionario)

lista_argumentos_associativos( a= 0, b= 1, c = 2, d= 3)
lista_argumentos_associativos( zero= 0, um = 1, dois = 2, tres = 3, quatro=4 )

# exemplo 3

def argumentos (*args, **kwargs):
    print("\nEsses são os args:", args,"\n")
    print("Esses são os kwargs:", kwargs,"\n")

argumentos(1, 2 ,3 ,4, 25 , um=1, dois=2, tres=3)