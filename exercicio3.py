def soma_dos_aninhados(lista_de_listas):
    # Inicializa a variável soma com o valor 0.
    soma = 0
    for lista in lista_de_listas:
        # Usa a função sum() para calcular a soma de todos os elementos da lista interna.
        soma += sum(lista)
    return soma

# Exemplo de uso da função:
lista = [[11, 22], [33], [44, 55, 66]]
outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]

resultado_lista = soma_dos_aninhados(lista)
resultado_outra_lista = soma_dos_aninhados(outra_lista)

print("Resultado da lista:", resultado_lista)  
print("Resultado da outra lista:", resultado_outra_lista)  








