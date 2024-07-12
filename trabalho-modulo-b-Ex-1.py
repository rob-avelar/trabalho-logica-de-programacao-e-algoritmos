# Exigência de código (1 de 6) - Print com nome completo
print('Bem-vindos a loja de Robson Aparecido Avelar dos Santos! \n')

# Exigência de código (2 de 6) - Implementar input do valor do pedido e número de parcelas
valorDoPedido = float(input('Digite o valor do pedido: '))
quantidadedeParcelas = int(input('Digite o número de parcelas: '))

# Exigência de código (3 de 6) e (5 de 6) - Implementar juros e estruturas condicionais
if quantidadedeParcelas < 4:
    juros = 0.0
elif quantidadedeParcelas >=4 and quantidadedeParcelas <6:
    juros = 0.04
elif quantidadedeParcelas >=6 and quantidadedeParcelas <9:
    juros = 0.08
elif quantidadedeParcelas >=9 and quantidadedeParcelas <13:
    juros = 0.16
else:
    juros = 0.32

# Exigência de código (4 de 6) - Implementar valor da parcela e valor total parcelado
valordeParcela = (valorDoPedido * (1 + juros)) / quantidadedeParcelas
valorTotalParcelado = valordeParcela * quantidadedeParcelas

# Exigência de código (6 de 6) - Fazer comentários relevantes no código

# Exigência de console (1 de 2) - Apresentar mensagem com o nome completo
print('Atendimento realizado por Robson Aparecido Avelar dos Santos \n')

# Exigência de console (2 de 2) - Apresentar parcelamento com juros se quantidade de parcelas for maior ou igual a 4.

if quantidadedeParcelas >= 4:
    print(f'Parcelamento em {quantidadedeParcelas} vezes com juros de {juros * 100}%')
    print(f'Valor da parcela: R$ {valordeParcela:.2f}')
    print(f'Valor total parcelado: R$ {valorTotalParcelado:.2f}')
else:
    print(f'Parcelamento em {quantidadedeParcelas} vezes sem juros')
    print(f'Valor da parcela: R$ {valordeParcela:.2f}')
    print(f'Valor total parcelado: R$ {valorTotalParcelado:.2f}')





