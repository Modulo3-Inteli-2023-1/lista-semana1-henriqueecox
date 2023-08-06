def tem_duplicados(lista):
    # Cria um conjunto vazio para armazenar os elementos únicos da lista
    elementos_unicos = set()

    # Percorre a lista
    for elemento in lista:
        # Se o elemento já estiver no conjunto, significa que ele é duplicado
        if elemento in elementos_unicos:
            return True
        # Adiciona o elemento ao conjunto de elementos únicos
        elementos_unicos.add(elemento)

    # Se percorreu toda a lista sem encontrar duplicados, retorna False
    return False

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 2, 3, 4, 5]

print(tem_duplicados(lista1))  
print(tem_duplicados(lista2))  










