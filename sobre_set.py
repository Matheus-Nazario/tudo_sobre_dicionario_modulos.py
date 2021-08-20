#
# Exsite tipos de conjutos list, dicionário e SET

# O Set ordena do menor para o maior de A a z e usa {}
#
lista_set = {"um_set", "dois_set"}

print(lista_set)


usuarios1 = [1, 2, 3, 3, 4, 2, 8]

usuarios2 = [7, 10, 5, 6]

lsita_vazia = []
lsita_vazia.extend(usuarios1)

outra_lista = usuarios1.copy()
outra_lista.extend(usuarios2)
print(outra_lista)
valor = set(outra_lista)
print(valor)
