nome = input("Digite seu nome?  ")
profissao = input("Digite sua profissão?  ")
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade não pode ser negativa.")
            continue
        break
    except ValueError:
        print("Por favor, digite um número válido.")

mensagem_base = f"Bem-vindo(a) ao meu exercício, {nome}! Atualmente você é {profissao}."

if idade < 12:
    falta = 18 - idade
    print(f"{mensagem_base} Você é uma criança! Faltam {falta} anos pra atingir a maioridade.")
elif idade < 18:
    falta = 18 - idade
    print(f"{mensagem_base} Você é um adolescente! Ainda faltam {falta} anos para a maioridade.")
else:
    print(f"{mensagem_base} Você é um adulto.")