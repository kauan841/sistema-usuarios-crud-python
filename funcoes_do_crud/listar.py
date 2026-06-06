from .adicionar import usuarios
from .arquivo import ler_json

def listar_usuarios():
    usuarios_cadastrados = ler_json()
    if not usuarios_cadastrados:
        print("Nenhum usuário cadastrado.")
    else:
        print("\nLista de usuários:")
        for i, usuario in enumerate(usuarios_cadastrados.values(), start=1):
            print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}")
