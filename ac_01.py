""" 
        Atividade Contínua 01 


1. Suponha que a operação in não existia em Python. 
Escreva uma função com o nome pertence, 
que recebe como argumentos de entrada uma lista e um número inteiro e retorna True, 
se o número inteiro estiver armazenado na lista, e False,
caso contrário. Por exemplo: 
pertence([2, 3, 4], 3) # chamada da função True # retorno 
pertence([2, 3, 4], 1) # chamada da função False # retorno 
"""


def pertence(lista, num):
    qtd = lista.count(num)

    if qtd > 0:
        print(True)
    else:
        print(False)


pertence([2, 3, 4], 7)

"""
2. Escreva uma função chamada substitui que recebe como argumentos de entrada
uma lista (lst) e dois números (velho e novo) e retorna uma lista onde todas as
ocorrências de velho são substituídas por novo.
Por exemplo:
substitui([1, 2, 3, 2, 4], 2, 99) # chamada da função
[1, 99, 3, 99, 4] # retorno
"""


def substitui(lista, velho, novo):

    for i in lista:
        if velho in lista:
            ind = lista.index(velho)
            lista.insert(ind, novo)
            indExc = ind + 1
            lista.pop(indExc)
    print(lista)


substitui([1, 2, 3, 2, 4], 2, 99)

"""
3. Escreva uma função chamada posicoes_lista que recebe como argumentos de entrada uma lista 
e um elemento, e retorna uma lista contendo todas as 
posições em que o elemento ocorre na lista. 
Por exemplo: 
posicoes_lista(['a', 2, 'b', 'a'], 'a') # chamada da função [0, 3] # retorno 
"""


def posicoes_lista(lista, elemento):
    newLista = []

    qtdLista = len(lista)
    cont = 0
    while cont < qtdLista:
        valor = lista[cont]
        if elemento == valor:
            newLista.append(cont)

        cont = cont + 1
    print(newLista)


posicoes_lista(["a", 2, "b", "a"], "a")

"""
4. Suponha um dicionário D de estudantes, como definida no exemplo abaixo, onde a chave
é o nome do estudante e o valor uma lista de 3 notas. Escreva uma função chamada
aprovados que receba como argumentos de entrada o dicionário D e retorna uma lista
com o nome dos alunos aprovados (um aluno é aprovado quando a média das suas notas
é maior ou igual a 6).
Por exemplo:
D = {'Alano':[4.5, 7.0, 6.0],
'Denise':[9.0, 8.5, 9.5],
'Ana Paula':[3.5, 1.0, 6.5],
'Marcelo': [9.0, 10.0, 7.0]}
aprovados(D) # chamada da função
['Denise', 'Marcelo'] # retorno
"""


def aprovados(d):
    osaprovados = []
    for x in d:
        media = sum(d[x]) / len(d[x])
        if media >= 6:
            osaprovados.append(x)
    print(osaprovados)


D = {
    "Alano": [4.5, 7.0, 6.0],
    "Denise": [9.0, 8.5, 9.5],
    "Ana Paula": [3.5, 1.0, 6.5],
    "Marcelo": [9.0, 10.0, 7.0],
}
aprovados(D)  # chamada da função
["Denise", "Marcelo"]  # retorno
