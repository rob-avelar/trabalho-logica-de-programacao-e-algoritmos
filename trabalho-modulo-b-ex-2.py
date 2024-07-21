print('Bem-Vindo ao restaurante de Robson Aparecido Avelar dos Santos')
print('--'*13, 'Cardápio', '--'*13)
print('---| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) | ---')
print('---|    P    |     R$ 16,00        |     R$ 15,00        | ---')
print('---|    M    |     R$ 18,00        |     R$ 17,00        | ---')
print('---|    G    |     R$ 22,00        |     R$ 21,00        | ---')
print('--'*31)

total = 0
continuar = True

while continuar:
    # Escolhendo o sabor do prato
    sabor = input('Digite o sabor do prato (BA ou FF): ')
    while sabor not in ['BA', 'FF']:
        print('Sabor inválido. Tente novamente.')
        # Caso de sabor inválido, refazendo a pergunta
        sabor = input('Digite o sabor do prato (BA ou FF): ')

    # Escolhendo o tamanho do prato
    tamanho = input('Escolha o tamanho do prato desejado (P, M ou G): ')
    while tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente.')
        # Caso de tamanho inválido, refazendo a pergunta
        tamanho = input('Escolha o tamanho do prato desejado (P, M ou G): ')

    # Calculando o preço do prato dependendo do tamanho e sabor
    if sabor == 'BA':
        if tamanho == 'P':
            preco = 16.00
        elif tamanho == 'M':
            preco = 18.00
        elif tamanho == 'G':
            preco = 22.00

    elif sabor == 'FF':
        if tamanho == 'P':
            preco = 15.00
        elif tamanho == 'M':
            preco = 17.00
        elif tamanho == 'G':
            preco = 21.00

    total += preco
    print(f'Você pediu um {sabor} no tamanho {tamanho}. O preço é R$ {preco:.2f}.')

    # Perguntando ao cliente se deseja mais alguma coisa
    mais_alguma_coisa = input('Deseja pedir mais alguma coisa? (S/N): ')
    while mais_alguma_coisa not in ['S', 'N']:
        print('Opção inválida. Deseja pedir mais alguma coisa? (S/N): ')

    if mais_alguma_coisa == 'N':
        continuar = False

# Exibindo o valor total da conta ao cliente
print(f'O total da sua conta é R$ {total:.2f}. Obrigado pela preferência!')

