"""
Escreva uma função que conta a quantidade de vogais em um texto
e armazena tal quantidade em um dicionário, onde a chave é a vogal
considerada e o valor é a quantidade de vezes que essa vogal aparece no texto.
A função deve receber o texto como entrada, e retornar o dicionário.
"""


def qtd_vogais(texto):
    dicvogal = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for i in texto:
        for key, value in dicvogal.items():
            if key == i:
                dicvogal[key] = value + 1

    print(dicvogal)


texto = input("Digite o texto e descubras as vogais: ")

qtd_vogais(texto)
