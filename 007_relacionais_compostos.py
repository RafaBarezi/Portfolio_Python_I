print("Relacionais compostos:\n")

num1 = eval(input("Digite um número >>> "))
num2 = eval(input("Digite outro número >>> "))  

if(num1 == num2):
    print("\nOs números digitados são iguais\n")
elif(num1 > num2):
    print("\nO %d é maior que %d"%(num1, num2),"\n")
else:
    print("\nO %d é maior que %d"%(num2, num1),"\n")