from .adicionar import usuarios

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\nLista de usuários:")
        for i, usuario in enumerate(usuarios.values(), start=1):
            print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}")
