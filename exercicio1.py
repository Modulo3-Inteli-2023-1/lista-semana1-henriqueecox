def multiplas_operacoes(a, b):
    # Soma
    soma = a + b
    
    # Subtração
    subtracao = a - b
    
    # Multiplicação
    multiplicacao = a * b
    
    # Divisão com tratamento para divisão por zero
    if b != 0:
        divisao = a / b
    else:
        divisao = 0

    return soma, subtracao, multiplicacao, divisao

# Exemplo de uso da função
resultado = multiplas_operacoes(10, 2)
print("Soma:", resultado[0])
print("Subtração:", resultado[1])
print("Multiplicação:", resultado[2])
print("Divisão:", resultado[3])












