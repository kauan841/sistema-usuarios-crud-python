from .adicionar import usuarios

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("Usuários cadastrados:")
    for nome, info in usuarios.items():
        print(f"Nome: {info['nome']}, Idade: {info['idade']}")