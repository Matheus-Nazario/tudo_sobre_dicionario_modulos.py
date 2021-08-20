"""
A função recebe como entrada dois parâmetros:
Um dicionário contendo como chave o nome de um funcionário e como valor uma lista contendo email, salário-base e cargo desse funcionário.
O nome de um funcionário.
Observe abaixo um exemplo do formato do dicionário de entrada para a função:
{'marcilio': ['marcilio@email.com', 5000.00, 'DESENVOLVEDOR'],
 'angelica': ['angelica@email.com', 1000.00, 'ANALISTA'],
 'fernanda': ['fernanda@email.com', 3000.00, 'GERENTE']}

A função deve retornar como resultado o salário líquido do funcionário. O salário líquido é calculado de acordo com as regras abaixo:
Se o cargo for DESENVOLVEDOR, o funcionário terá desconto de 15% caso o salário seja maior ou igual que 2.000,00, ou apenas 5% caso o salário seja menor que isso.
Se o cargo for ANALISTA, o funcionário terá desconto de 20% caso o salário seja maior ou igual que 3.500,00, ou apenas 10% caso o salário seja menor que isso.
Se o cargo for GERENTE, o funcionário terá desconto de 25% caso o salário seja maior ou  igual que 4.000,00, ou apenas 15% caso o salário seja menor que isso.  
"""


def calcular_salario(dicionario, nome):
    email, salario, cargo = dicionario[nome]
    if cargo == "DESENVOLVEDOR":
        if salario >= 2000:
            return salario * 0.85
        else:
            return salario * 0.95

    if cargo == "ANALISTA":
        if salario >= 3500:
            return salario * 0.8
        else:
            return salario * 0.9

    if cargo == "GERENTE":
        if salario >= 4000:
            return salario * 0.75
        else:
            return salario * 0.85
