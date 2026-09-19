idade = int(input("Informe sua idade por gentileza: "))
empre_fixo = str(input("Possui emprego fixo? (Sim/Nao) ")).lower()
renda_mensal = float(input("Renda mensal: "))
nome_sujo = str(input("Possui o nome sujo?" )).lower()

if idade < 0 or renda_mensal < 0:
    print("Dados inválidos!")

elif idade >= 23 and empre_fixo == "sim" and renda_mensal >= 5000 and nome_sujo == "nao":
    print("Um emprestimo de R$ 20.000,00 Foi aprovado para você!")

