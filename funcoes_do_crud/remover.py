from .adicionar import usuarios

def remover_usuario(nome):
    if nome in usuarios:
        del usuarios[nome]
        print(f"Usuário '{nome}' removido com sucesso!")
    else:
        print(f"Usuário '{nome}' não encontrado.")