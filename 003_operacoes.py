print("Operações matemáticas:\n")

print(10+7)
print(10+(50+50))
print(10-7)
print(10*7)
print(10/2)
print("\n")

valor= (10/7)
print("%.2f" %valor)
print(10%7)
print(10%2)
print("\n")

num1 = eval(input("\nPor favor, digite um número >>> "))
num2 = eval(input("Favor digitar outro número >>>"))
divisao = num1 / num2
resto = num1 % num2
print("\n")
print(f"{num1} dividido por {num2} é igual a {divisao}\n")
print(f"O resto de {num1} e {num2} é {resto}")