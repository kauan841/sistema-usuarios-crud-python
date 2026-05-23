usuarios = {}


def adicionar_usuario_no_sistema(nome, idade):
    if nome in usuarios:
        print(f"Usuário '{nome}' já existe.")
        return

    usuarios[nome] = {
        'nome': nome,
        'idade': idade
    }

    print(f"Usuário '{nome}' adicionado com sucesso!")