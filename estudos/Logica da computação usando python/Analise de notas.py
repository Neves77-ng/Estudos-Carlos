nota1 = float(input("Informe a primeira nota:"))
nota2 = float(input("Informe a segunda nota:"))
nota3 = float(input("Informe a terceira nota:"))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado!")

elif media >= 5:
    print("Recuperacão!")

else:
    print("Reprovado!")

print(f"sua média é: {media}")