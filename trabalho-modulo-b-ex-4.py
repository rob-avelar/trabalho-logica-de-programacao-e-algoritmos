print("Bem vindos a empresa do Robson Aparecido Avelar dos Santos")  # Empresa com o meu nome

# Lista para armazenar os funcionários e o ID global inicial
lista_funcionarios = [] 
id_global = 1298790   

def cadastrar_funcionario(id):  # Função de cadastro de funcionário
    print(f'ID do novo funcionário: {id}')
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    lista_funcionarios.append(funcionario.copy())

def consultar_funcionarios():  # Função de consulta de funcionários
    while True:
        print("Consultar Funcionário")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            for func in lista_funcionarios:
                print(func)
        elif opcao == 2:
            id_consulta = int(input("Digite o ID do funcionário: "))
            encontrado = False
            for func in lista_funcionarios:
                if func['id'] == id_consulta:
                    print(func)
                    encontrado = True
                    break
            if not encontrado:
                print("Id inválido")
        elif opcao == 3:
            setor_consulta = input("Digite o setor dos funcionários: ")
            encontrados = [func for func in lista_funcionarios if func['setor'] == setor_consulta]
            if encontrados:
                for func in encontrados:
                    print(func)
            else:
                print("Nenhum funcionário encontrado nesse setor")
        elif opcao == 4:
            return
        else:
            print("Opção inválida")

def remover_funcionario():  # Função de remoção de funcionário da lista
    while True:
        id_remover = int(input("Digite o ID do funcionário a ser removido: "))
        encontrado = False
        for func in lista_funcionarios:
            if func['id'] == id_remover:
                lista_funcionarios.remove(func)
                print("Funcionário removido com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Id inválido")
        else:
            break

while True:  # Estrutura de menu no código principal
    print("Menu:")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == 2:
        consultar_funcionarios()
    elif opcao == 3:
        remover_funcionario()
    elif opcao == 4:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida")

