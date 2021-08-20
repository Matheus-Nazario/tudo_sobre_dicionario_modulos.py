"""
Preencha um dicionário com as informações de 5 produtos.
Utilize o nome do produto como chave e o preço como valor.
Solicite os dados ao usuário
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00

Exemplo:
Veja um exemplo da estrutura do dicionário.
{'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0, 'Lápis': 1.50}
"""

produto = {}

for x in range(5):
    nome_do_produto = input("Digite o nome do produto? ")
    preco = float(input("Digite o nome do produto? "))
    produto[nome_do_produto] = preco

print(produto)

for key, value in produto.items():
    if value > 50:
        print(key)
