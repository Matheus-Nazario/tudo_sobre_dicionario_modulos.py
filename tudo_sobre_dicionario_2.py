# EXEMPLO 1:
# Criar dicionario para armazenar um cadastro de pessoas (CPF e NOME)
cadastro = {12345678: "Paulo", 88888888: "Maria", 4565456: "Joรฃo"}

print(cadastro)
print(cadastro[12345678])               # Paulo

# Adicionar os dados de uma pessoa no dicionario
cadastro[99999999] = "Ana"
cadastro[77777777] = "Pedro"
print(cadastro)

# Alterar o Nome de uma pessoa
cadastro[99999999] = "Ana Maria"
print(cadastro)

# Excluir os dados de uma pessoa
cadastro.pop(12345678)
print(cadastro)

# Verificar se chave existe no dicionรกrio
if 99999999 in cadastro:
    cadastro.pop(99999999)
else:
    print('CPF nao esta cadastrado')
print(cadastro)

# Percorrer o dicionario
for x in cadastro:
    print(x, cadastro[x])

# preencher dicionรกrio com dados informados pelo usuรกrio
for a in range(3):
    cpf = int(input('CPF: '))
    nome = input('Nome: ')
    cadastro[cpf] = nome
print(cadastro)

# EXEMPLO 2:
# Dicionario para armazenar o nome de um aluno e uma lista com 5 notas
alunos = {"Paulo": [9, 8, 7, 4, 10],
          "Maria": [8, 3, 8, 9, 10],
          "Pedro": [10, 7, 6, 4, 8]}

# Exibir lista de notas de um aluno
print(alunos["Pedro"])

# Inserir uma nova nota para um aluno
alunos["Pedro"].append(10)

# Alterar a nota de um aluno
alunos["Pedro"][5] = 9.5

cadastroDois = {99999999: "MAtheuzão", 100000: "hahahaha"}

cadastro.update(cadastroDois)
print(cadastro)
