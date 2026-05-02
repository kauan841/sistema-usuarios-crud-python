usuarios = []


def adicionar_usuario(nome, idade):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f"Usuário '{nome}' já existe.")
            return
        return

    usuarios.append({
        'nome': nome,
        'idade': idade
    })

    print(f"Usuário '{nome}' adicionado com sucesso!")


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\nLista de usuários:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}")


def buscar_usuario(nome):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f"Usuário encontrado: Nome: {usuario['nome']}, Idade: {usuario['idade']}")
            return
    print(f"Usuário '{nome}' não encontrado.")


def atualizar_usuario(nome):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            try:
                nova_idade = int(input(f"Digite a nova idade para '{nome}': "))
            except ValueError:
                print("Digite um número válido.")
            return

        usuario['idade'] = nova_idade
        print(f"Usuário '{nome}' atualizado com sucesso!")
    else:
        print(f"Usuário '{nome}' não encontrado.")


def remover_usuario(nome):
    for i, usuario in enumerate(usuarios):
        if usuario['nome'] == nome:
            del usuarios[i]
            print(f"Usuário '{nome}' removido com sucesso!")
            return
    print(f"Usuário '{nome}' não encontrado.")


# MENU PRINCIPAL
while True:
    print("\nMenu de opções:")
    print("1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário")
    print("4. Atualizar usuário")
    print("5. Remover usuário")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome do usuário: ")

        try:
            idade = int(input("Digite a idade do usuário: "))
        except ValueError:
            print("Digite uma idade válida.")
            continue

        adicionar_usuario(nome, idade)

    elif escolha == '2':
        listar_usuarios()

    elif escolha == '3':
        nome = input("Digite o nome do usuário: ")
        buscar_usuario(nome)

    elif escolha == '4':
        nome = input("Digite o nome do usuário: ")
        atualizar_usuario(nome)

    elif escolha == '5':
        nome = input("Digite o nome do usuário: ")
        remover_usuario(nome)

    elif escolha == '6':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
