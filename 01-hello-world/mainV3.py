print("Olá amigo(a)! 🚀")

nome = input("Qual é o seu nome?  ")
idade = int(input("Qual é a sua idade?  "))

if idade < 12:
        print("Você é uma criança!")
elif idade < 18:
        print("Você é menor de idade!")
else:
        print("Você é maior de idade!")

if idade < 18:
        falta = 18 - idade
        print(f"Faltam {falta} anos para você se tornar maior de idade. Seja muito bem-vindo(a) ao meu repositório do GitHub! 🌟")
else :
        print("Seja muito bem-vindo(a) ao meu repositório do GitHub! 🌟")