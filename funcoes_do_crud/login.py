from .adicionar import usuarios
from .arquivo import ler_arquivo_json

def login():
    print("Bem-vindo ao sistema de login!")
    nome = input("Digite seu nome: ")
    idade_input = input("Digite sua idade: ")


    try:
        nome = nome.strip()
        idade = int(idade_input)
    except ValueError:
        print("Nome ou idade inválidos. Tente novamente.")
        return False

    usuarios_cadastrados = ler_arquivo_json()
    for usuario in usuarios_cadastrados.values():
        if usuario['nome'] == nome and usuario['idade'] == idade:
            print(f"Login bem-sucedido! Bem-vindo, {nome}!")
            return True

    print("Nome ou idade incorretos. Tente novamente.")
    return False