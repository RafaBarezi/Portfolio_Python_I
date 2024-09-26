print("\nInstrução break:\n")

print("Antes de entrar no laço:\n")
x = 0
while (x<=100):
    x += 5
    print(x)
    if(x == 50):
        print("\nChegou no n° 50, então pedimos para a instrução parar\n")
        break
        
print("Depois de entrar no laço\n") 
