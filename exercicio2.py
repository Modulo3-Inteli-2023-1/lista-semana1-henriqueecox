def cumulativo(lista):
    # Cria uma lista vazia para guardar os resultados da soma cumulativa.
    cumulativa = []
    soma = 0
    # Percorre cada número na lista original.
    for num in lista:
        # A cada número, adiciona-o à soma acumulada.
        soma += num

        # Depois de adicionar o número à soma, coloca a soma acumulada na lista cumulativa.
        cumulativa.append(soma)

    # Devolve a lista com os resultados da soma cumulativa.
    return cumulativa

lista = [2, 3, 4, 5]
resultado = cumulativo(lista)
print(resultado)  # Resultado esperado: [2, 5, 9, 14]








