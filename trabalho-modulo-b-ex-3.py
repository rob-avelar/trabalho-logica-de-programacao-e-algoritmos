# Mensagem de boa-vinda
print("Bem vindos a Fábrica de Camisetas do Robson Aparecido Avelar dos Santos")

# Função para escolher o modelo de camiseta
def escolha_modelo():
    while True:
        print("Escolha o modelo desejado")
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Com Estampa")
        print("MLE - Manga Longa Com Estampa")
        modelo = input(">>").upper()
        if modelo == 'MCS':
            return 1.80
        elif modelo == 'MLS':
            return 2.10
        elif modelo == 'MCE':
            return 2.90
        elif modelo == 'MLE':
            return 3.20
        else:
            print('Escolha inválida, entre com o modelo novamente') # Mensagem informando que a escolha é inválida

# Função para obter o número de camisetas e calcular o desconto
def num_camisetas():
    while True:
        try:
            numero = int(input('Escolha o número de camisetas: '))
            if numero > 20000:
                print('Não aceitamos tantas camisetas de uma vez. Por favor, entre com o número de camisetas novamente.') # Mensagem informando que a quantidade de camisetas é inválida
            else:
                if numero < 20:
                    desconto = 0
                elif 20 <= numero < 200:
                    desconto = 0.05
                elif 200 <= numero < 2000:
                    desconto = 0.07
                elif 2000 <= numero <= 20000:
                    desconto = 0.12
                return numero * (1 - desconto)
        except ValueError:
            print('Valor não numérico. Tente novamente.')

# Função para escolher o tipo de frete
def escolha_frete():
    while True:
        print("Escolha o tipo de frete:")
        print("1 - Frete por transportadora - R$ 100.00")
        print("2 - Frete por Sedex - R$ 200.00")
        print("0 - Retirar pedido na fábrica - R$ 0.00")
        frete = input(">>")
        if frete == '1':
            return 100
        elif frete == '2':
            return 200
        elif frete == '0':
            return 0
        else:
            print('Opção inválida, tente novamente')

# Cálculo do total a pagar
modelo = escolha_modelo()
quantidade = num_camisetas()
frete = escolha_frete()

total = (modelo * quantidade) + frete

# Resultado do total da compra
print(f"Total: R$ {total:.2f} (Modelo: {modelo:.2f} * Quantidade(com desconto): {quantidade} + frete: {frete:.2f})")

# Comentários relevantes
# O código acima implementa um sistema de cobrança para uma fábrica de camisetas
# Os preços das camisetas variam conforme o modelo escolhido
# A quantidade de camisetas compradas pode proporcionar descontos
# O tipo de frete pode adicionar um custo extra ao total
# O programa valida as entradas do usuário e calcula o total a pagar com base nas escolhas feitas






