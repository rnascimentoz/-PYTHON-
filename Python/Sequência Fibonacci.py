print("-"*15)
print("Fibonacci")
print("-"*15)
n = int(input("Digite o número de casas a serem exibidas: "))
a = 1
b = 1
print("-"*40)
print()
print("Fibonacci: 0,", end="")
for x in range(n):
    print(a, end="")
    c = a + b
    a = b
    b = c
print()
print()
print("-"*40)