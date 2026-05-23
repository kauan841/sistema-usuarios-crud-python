from .adicionar import usuarios

def buscar_usuario(nome):
    if nome in usuarios:
        usuario = usuarios[nome]
        print(f"Usuário encontrado: Nome: {usuario['nome']}, Idade: {usuario['idade']}")
    else:
        print(f"Usuário '{nome}' não encontrado.")