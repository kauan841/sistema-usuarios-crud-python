from .adicionar import usuarios

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

    for usuario in usuarios.values():
        if usuario['nome'] == nome and usuario['idade'] == idade:
            print(f"Login bem-sucedido! Bem-vindo, {nome}!")
            return True

    print("Nome ou idade incorretos. Tente novamente.")
    return False