nota1 = float(input("Informe a primeira nota:"))
nota2 = float(input("Informe a segunda nota:"))
nota3 = float(input("Informe a terceira nota:"))
media = (nota1 + nota2 + nota3) / 3

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3  < 0 or nota3 > 10:
    print("Notas invalidas!!")

elif media >= 7:
    print("Aprovado! A sua média é {media}!")

elif media >= 5:
    print("Recuperacão! A sua média é {media}!")

else:
    print("Reprovado! A sua média é {media}!")