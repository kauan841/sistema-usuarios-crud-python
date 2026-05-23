from .adicionar import usuarios

def atualizar_usuario(nome):
    if nome in usuarios:
        usuario = usuarios[nome]

        try:
            nova_idade = int(input(f"Digite a nova idade para '{nome}': "))
        except ValueError:
            print("Digite um número válido.")
            return

        usuario['idade'] = nova_idade
        print(f"Usuário '{nome}' atualizado com sucesso!")
    else:
        print(f"Usuário '{nome}' não encontrado.")