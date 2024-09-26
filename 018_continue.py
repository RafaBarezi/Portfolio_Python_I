print("Instrução continue:\n")

x = 0
while(x<50):
    x += 1
    if(x%3==0): 
        continue
    if(x>25):
        break
    print(x)
else: 
    print("\nelse\n")
print("\nfim\n")