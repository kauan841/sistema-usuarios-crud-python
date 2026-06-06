from .adicionar import usuarios
from .arquivo import ler_json

def buscar_usuario(nome):
    usuarios_cadastrados = ler_json()
    if nome in usuarios_cadastrados:
        usuario = usuarios_cadastrados[nome]
        print(f"Usuário encontrado: Nome: {usuario['nome']}, Idade: {usuario['idade']}")
    else:
        print(f"Usuário '{nome}' não encontrado.")