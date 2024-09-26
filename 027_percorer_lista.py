print("Percorer lista (Mostrar quantidade de cada elemento):\n")

from collections import defaultdict

lista_mel = ["Mel", "Rafaela", "Mel","Fernando", "Mel", "Mel"]

index = defaultdict(list) 

for i, valor in enumerate(lista_mel):
 
	index[valor].append(i) 
       
for valor in index:
        if (len(index[valor])>0):
            print(valor,"aparece na posição", index[valor])  
print()