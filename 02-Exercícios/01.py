# Pergunta o nome de um produto
# Pergunta o preço dele
# Pergunta a quantidade em estoque
# Faz isso se repetir até o usuário digitar "n" pra parar
# No final, mostra todos os produtos cadastrados

estoque = []

while True:
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    estoque.append({
        "produto": produto,
        "preço": preco,
        "quantidade": quantidade
    })

    resposta = input("Deseja adicionar outro produto? (s/n): ").lower()
    if resposta == "n":
        break                 

print(f"\nProdutos cadastrados: {len(estoque)}\n")
for item in estoque:
    print(f"Produto: {item['produto']}, Preço: R${item['preço']}, Quantidade: {item['quantidade']}")