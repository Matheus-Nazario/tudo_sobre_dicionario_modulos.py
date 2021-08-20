from calcular_salario import calcular_salario

dicionario = {
    "marcilio": ["marcilio@email.com", 5000.00, "DESENVOLVEDOR"],
    "pedro": ["pedro@email.com", 2000.00, "DESENVOLVEDOR"],
    "carlos": ["carlos@email.com", 1000.00, "DESENVOLVEDOR"],
    "roberto": ["roberto@email.com", 5000.00, "ANALISTA"],
    "renata": ["renata@email.com", 3500.00, "ANALISTA"],
    "angelica": ["angelica@email.com", 1000.00, "ANALISTA"],
    "amanda": ["amanda@email.com", 8000.00, "GERENTE"],
    "ricardo": ["ricardo@email.com", 4000.00, "GERENTE"],
    "fernanda": ["fernanda@email.com", 3000.00, "GERENTE"],
    "marcos": ["marcos@email.com", 800.00, "ESTAGIARIO"],
}

try:
    resultado = calcular_salario(dicionario, "marcilio")
    assert resultado == 4250.0
    print("CORRETO")
except AssertionError:
    print("ERRO:")
    print(" Resultado esperado: 4250.0")
    print(" Resultado da Função:", resultado)

try:
    resultado = calcular_salario(dicionario, "pedro")
    assert resultado == 1700.0
    print("CORRETO")
except AssertionError:
    print("ERRO:")
    print(" Resultado esperado: 1700.0")
    print(" Resultado da Função:", resultado)

try:
    resultado = calcular_salario(dicionario, "carlos")
    assert resultado == 950.0
    print("CORRETO")
except AssertionError:
    print("ERRO:")
    print(" Resultado esperado: 950.0")
    print(" Resultado da Função:", resultado)

try:
    resultado = calcular_salario(dicionario, "roberto")
    assert resultado == 4000.0
    print("CORRETO")
except AssertionError:
    print("ERRO:")
    print(" Resultado esperado: 4000.0")
    print(" Resultado da Função:", resultado)

try:
    resultado = calcular_salario(dicionario, "renata")
    assert resultado == 2800.0
    print("CORRETO")
except AssertionError:
    print("ERRO:")
    print(" Resultado esperado: 2800.0")
    print(" Resultado da Função:", resultado)

try:
    resultado = calcular_salario(dicionario, "angelica")
    assert resultado == 900.0
    print("CORRETO")
except AssertionError:
    print("ERRO:")
    print(" Resultado esperado: 900.0")
    print(" Resultado da Função:", resultado)

try:
    resultado = calcular_salario(dicionario, "amanda")
    assert resultado == 6000.0
    print("CORRETO")
except AssertionError:
    print("ERRO:")
    print(" Resultado esperado: 6000.0")
    print(" Resultado da Função:", resultado)

try:
    resultado = calcular_salario(dicionario, "ricardo")
    assert resultado == 3000.0
    print("CORRETO")
except AssertionError:
    print("ERRO:")
    print(" Resultado esperado: 3000.0")
    print(" Resultado da Função:", resultado)

try:
    resultado = calcular_salario(dicionario, "fernanda")
    assert resultado == 2550.0
    print("CORRETO")
except AssertionError:
    print("ERRO:")
    print(" Resultado esperado: 2550.0")
    print(" Resultado da Função:", resultado)
