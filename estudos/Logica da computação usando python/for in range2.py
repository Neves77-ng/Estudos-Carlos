numero = int(input("digite um número: "))

soma = 0
print("Numeros pares: ")
for i in range(1, numero + 1):
    if i % 2 == 0:
        print(i)
        soma += i

print("soma dos pares:", soma)