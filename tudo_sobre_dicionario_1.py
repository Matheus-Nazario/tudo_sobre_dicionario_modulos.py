import unittest
from collections import Counter

"""
Um dicionário é muito semelhante a uma lista.

Tomemos a lista [10,20,30]. As posições dela são 0,1 e 2.
lista[0] vale 10, lista[1] vale 20 e lista[2] vale 30.

A diferença entre dicionários e listas é que um dicionário
pode ter as posições que a gente quiser.

Um dicionário pode ter as posições 3, 9 e 11
(sem ter as posições 0,1,2,4,5,6,7,8, nem 10)

Na verdade, como podemos ver no exemplo a seguir,
um dicionário pode ter as posições "marcos", "fabio" e "maria".

(oficialmente, um dicionário não tem "posições",
mas sim chaves)
"""
agenda_exemplo = {}
agenda_exemplo["marcos"] = 32112232
agenda_exemplo["fabio"] = 988887788
agenda_exemplo["maria"] = 44554455

"""
Rode o codigo no IDLE apertando F5

Se você digitar agenda_exemplo['maria'],
deverá ver o telefone da maria
"""

"""
Crie uma função consulta que recebe uma agenda (um dicionário)
e uma pessoa, e retorna o telefone dessa pessoa
"""


def consulta(agenda, pessoa):
    for i in agenda:
        if i == pessoa:
            return agenda[pessoa]


"""
Crie uma função adiciona que recebe uma agenda
(um dicionário)
uma pessoa e um telefone, e adiciona o
telefone dessa pessoa na agenda

Adicionar um item num dicionário é simples
dicionario['chave'] = valor
"""


def adiciona(agenda, pessoa, telefone):
    agenda[pessoa] = telefone


"""
Rode o codigo no IDLE apertando F5

Ai, você pode testar sua função adiciona manualmente e
também fazer o runTests
"""

"""
Uma terceira feature que precisamos para a nossa agenda é
a possibilidade de verificar se uma pessoa já está na base de dados.

Simplesmente verificar agenda['pessoa'] não funciona:
se você acessar uma pessoa que não existe,
o python dará um KeyError.

Precisamos, então usar o seguinte: 'chave' in dicionario
    isso é um teste que retorna True se a chave
    está no dicionário, e False caso contrário.

Temos, por exemplo, os prints seguintes,
que verificam se algumas pessoas estao na agenda
"""
# print('maria esta na agenda?')
# print('maria' in agenda_exemplo)

# print('damiao esta na agenda?')
# print('damiao' in agenda_exemplo)

# pessoa = 'marcos'
# print('a string da variavel pessoa é uma chave da agenda?')
# print(pessoa in agenda_exemplo)

"""
Crie uma função verifica, que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa
está na agenda (retorna True se
a pessoa está e False caso contrário)
"""


def verifica(agenda, pessoa):
    return pessoa in agenda


"""
Para definir um dicionário vazio, fazemos o seguinte:
"""
vazio = {}


"""
Usando seus conhecimentos de dicionário até agora,
crie uma função conta_letras que recebe uma palavra e retorna
um dicionário com o número de ocorrências de cada letra.

por exemplo, conta_letras('abacaxi') deve
retornar o dicionário {'a':3,'b':1,'c':1,'x':1}

NAO USE nenhuma função mágica do python. Escreva a lógica
usando dicionários.

O seguinte trecho de codigo pode ser util:
>>> palavra='ganancia'
>>> nro_a = 0
>>> for letra in palavra:
    print('estou olhando para',letra)
    if letra == 'a':
    nro_a = nro_a+1
estou olhando para g
estou olhando para a
estou olhando para n
estou olhando para a
estou olhando para n
estou olhando para c
estou olhando para i
estou olhando para a
>>> nro_a
3
"""


def conta_letras(palavra):
    conta = {}
    for letra in palavra:
        conta[letra] = 0
    for key, value in conta.items():
        for letra in palavra:
            if key == letra:
                value = value + 1
                conta[letra] = value
    return conta


"""
Agora, vamos usar listas e dicionários para criar uma agenda
um pouco mais completa. Veja o exemplo
"""

agenda_melhor1 = {
    "lucas": {
        "email": "lucas.goncalves@faculdadeimpacta.com.br",
        "telefones": [11999888999, 1177788899],
    },  # meu email está correto, meus telefones nao :P
    "maria": {
        "email": "maria.aparecida@exemplo.com",
        "telefones": [84999777444],
    },
    "marta": {"telefones": [1177788899]},
}

"""
Crie uma função email, que recebe uma agenda (dessas melhoradas)
e uma pessoa.

Ela retorna o email da pessoa.

Não precisa se preocupar com
o caso do registro da pessoa nao ter email (faremos isso
mais pra frente)
"""


def email(agenda, pessoa):

    for i in agenda:
        if i == pessoa:
            a = agenda[i]
            return a["email"]


"""
Crie uma função telefone_principal, que recebe uma agenda
(nessa versão mais nova) e uma pessoa.

Ela retorna o primeiro telefone da lista de telefones da
pessoa
"""


def telefone_principal(agenda, pessoa):
    for i in agenda:
        if i == pessoa:
            a = agenda[pessoa]
            telefones = a["telefones"]
            return telefones[0]


"""
Se você quiser verificar todas as chaves de um dicionário,
pode fazer como a seguir
>>> for chave in agenda_melhor1:
    print(chave)
lucas
maria
marta

Lembrando de qual a cara da agenda_melhor1:

{'marta': {'telefones': [1177788899]},
 'lucas': {'email': 'lucas.goncalves@faculdadeimpacta.com.br',
                       'telefones': [11999888999, 1177788899]},
 'maria': {'email': 'maria.aparecida@exemplo.com', 'telefones': [84999777444]}}

(ela realmente só tem essas 3 chaves)
"""
"""
Crie uma função sem_email, que recebe uma agenda (nessa versão
mais nova) e retorna uma lista de todos os contatos sem email.

Por exemplo, sem_email(agenda_melhor1) deve retornar uma
lista com um único contato: ['marta']
"""


def sem_email(agenda):
    lista = []
    for key, value in agenda.items():
        if "email" not in value:
            lista.append(key)

    return lista


"""
Crie uma função conta telefones, que recebe uma agenda (nessa versão
mais nova) e retorna a quantidade de números de telefone registrados.

Se houver telefones repetidos (o exemplo agenda_melhor1 tem!),
conte as repetições (então, para agenda_melhor1 a resposta deve
ser 4, por mais que o mesmo número apareça no item marta
e no item lucas
"""


def conta_telefones(agenda):
    lista = []
    valor = 0
    for value in agenda.values():
        for i in value["telefones"]:
            lista.append(i)
    valor = len(lista)
    return valor


"""
Por ultimo, vamos criar uma funcao conta_ocorrencias
que dirá quantas vezes um telefone ocorre na agenda.

Ela recebe uma agenda melhorada (um dicionário nesse formato
que estamos usando) e devolve um dicionário. As chaves são
os números de telefone, e os valores, as vezes que cada
número apareceu na agenda
"""


def conta_ocorrencias(agenda):
    lista = []
    for valor in agenda.values():
        valores_telefone = valor["telefones"]
        for i in valores_telefone:
            lista.append(i)
    valores = Counter(lista)
    return valores


# segunda Opção sem a impotação
"""
def conta_ocorrencias(agenda):
    dicionario_ocorrencias = {}
    lista = []
    for key, value in agenda.items():
        for i in value["telefones"]:
            lista.append(i)
            dicionario_ocorrencias[i] = 0

    for i in dicionario_ocorrencias:
        valor = lista.count(i)
        dicionario_ocorrencias[i] = valor

    return dicionario_ocorrencias
"""

# -----------------------------teste------------------
agenda_testes1 = {
    "joao": 22222222,
    "jose": 33333333,
}

# agendas melhoradas
agenda1 = {}
alfabeto = "abcde"
for c in alfabeto:
    agenda1[c] = {
        "telefones": [1122233344]
    }  # uma agenda cujas pessoas sao as primeiras 5 letras
agenda2 = {}
vogais = "aeiouy"
for c in vogais:
    agenda2[c] = {
        "telefones": [11321321321]
    }  # uma agenda cujas pessoas sao todas as vogais
agenda2["fulano"] = {"email": "fulano@exemplo.com", "telefones": [1144440000]}
agenda3 = {}
pessoas = ["marcia", "ana", "marcos", "heitor"]
for p in pessoas:
    agenda3[p] = {"telefones": [1123232323]}
agenda3["fulano"] = {
    "email": "fulano@exemplo.com",
    "telefones": [11777888999, 1122222222],
}


class TestPartOne(unittest.TestCase):
    def test_01_consulta(self):
        self.assertEqual(consulta(agenda_testes1, "joao"), 22222222)
        self.assertEqual(consulta(agenda_testes1, "jose"), 33333333)

    def test_02_adiciona(self):
        agenda_testes1 = {
            "joao": 2,
            "jose": 3,
        }
        adiciona(agenda_testes1, "marcia", 55555555)
        self.assertEqual(consulta(agenda_testes1, "marcia"), 55555555)
        adiciona(agenda_testes1, "antonio", 88888888)
        self.assertEqual(consulta(agenda_testes1, "antonio"), 88888888)

    def test_03_verifica(self):
        self.assertFalse(verifica(agenda_testes1, "marcia"))
        self.assertFalse(verifica(agenda_testes1, "antonio"))
        self.assertTrue(verifica(agenda_testes1, "joao"))
        self.assertTrue(verifica(agenda_testes1, "jose"))

    def test_04_conta_letras(self):
        self.assertEqual(conta_letras("banana"), {"b": 1, "n": 2, "a": 3})
        self.assertEqual(conta_letras(""), {})
        self.assertEqual(
            conta_letras("a" * 5 + "b" * 3 + "c" * 10 + "a"),
            {"a": 6, "b": 3, "c": 10},
        )

    def test_05_email(self):
        self.assertEqual(
            email(agenda_melhor1, "lucas"),
            "lucas.goncalves@faculdadeimpacta.com.br",
        )
        self.assertEqual(
            email(agenda_melhor1, "maria"), "maria.aparecida@exemplo.com"
        )
        self.assertEqual(email(agenda2, "fulano"), "fulano@exemplo.com")
        self.assertEqual(email(agenda3, "fulano"), "fulano@exemplo.com")

    def test_06_telefone_principal(self):
        self.assertEqual(
            telefone_principal(agenda_melhor1, "lucas"), 11999888999
        )
        self.assertEqual(
            telefone_principal(agenda_melhor1, "maria"), 84999777444
        )
        self.assertEqual(
            telefone_principal(agenda_melhor1, "marta"), 1177788899
        )
        self.assertEqual(telefone_principal(agenda1, "a"), 1122233344)
        self.assertEqual(telefone_principal(agenda2, "a"), 11321321321)
        self.assertEqual(telefone_principal(agenda3, "ana"), 1123232323)
        self.assertEqual(telefone_principal(agenda3, "fulano"), 11777888999)

    def test_07_sem_email(self):
        self.assertEqual(set(sem_email(agenda1)), set(list(alfabeto)))
        self.assertEqual(set(sem_email(agenda2)), set(list(vogais)))
        self.assertEqual(set(sem_email(agenda3)), set(pessoas))

    def test_08_conta_telefones(self):
        self.assertEqual(conta_telefones(agenda1), 5)
        self.assertEqual(conta_telefones(agenda2), 7)
        self.assertEqual(conta_telefones(agenda3), 6)

    def test_09_conta_ocorrencias(self):
        self.assertEqual(conta_ocorrencias(agenda1), {1122233344: 5})
        self.assertEqual(
            conta_ocorrencias(agenda2), {11321321321: 6, 1144440000: 1}
        )
        self.assertEqual(
            conta_ocorrencias(agenda3),
            {1123232323: 4, 11777888999: 1, 1122222222: 1},
        )


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartOne)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


try:
    from dicionarios_gabarito import *
except:
    pass


runTests()
