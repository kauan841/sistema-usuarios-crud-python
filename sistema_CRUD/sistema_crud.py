import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from funcoes_do_crud.adicionar import adicionar_usuario_no_sistema
from funcoes_do_crud.listar import listar_usuarios
from funcoes_do_crud.buscar import buscar_usuario
from funcoes_do_crud.atualizar import atualizar_usuario
from funcoes_do_crud.remover import remover_usuario
from funcoes_do_crud.login import login


while True:

    escolha = input("Você deseja entrar no sistema? (s/n): ").strip().lower()

    if escolha == 's':
        break

    elif escolha == 'n':
        print("Saindo do sistema...")
        sys.exit()

    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")


# LOGIN / CADASTRO

while True:

    print("\nBem-vindo ao sistema CRUD de usuários!")
    print("Faça cadastro para acessar o sistema.")
    print("1. Fazer cadastro")
    print("2. Fazer login")

    escolha = input("Escolha uma opção: ").strip()

    # impede espaço vazio
    if escolha == "":
        print("Não digite apenas espaços.")
        continue

    if escolha == '1':

        nome = input("Digite o nome do usuário: ").strip()

        if nome == "":
            print("Nome não pode ser vazio.")
            continue

        idade_input = input("Digite a idade do usuário: ").strip()

        if idade_input == "":
            print("Idade não pode ser vazia.")
            continue

        try:
            idade = int(idade_input)

        except ValueError:
            print("Digite uma idade válida.")
            continue

        adicionar_usuario_no_sistema(nome, idade)

        print("Cadastro realizado com sucesso!")

        if login():
            break

    elif escolha == '2':

        if login():
            break

    else:
        print("Opção inválida. Tente novamente.")


# MENU PRINCIPAL

while True:

    print("\nMenu de opções:")
    print("1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário")
    print("4. Atualizar usuário")
    print("5. Remover usuário")
    print("6. Sair")

    escolha = input("Escolha uma opção: ").strip()

    if escolha == "":

        print("Não digite apenas espaços.")
        continue

    if escolha == '1':

        nome = input("Digite o nome do usuário: ").strip()

        if nome == "":
            print("Nome inválido.")
            continue

        idade_input = input("Digite a idade do usuário: ").strip()

        if idade_input == "":
            print("Idade inválida.")
            continue

        try:
            idade = int(idade_input)

        except ValueError:
            print("Digite uma idade válida.")
            continue

        adicionar_usuario_no_sistema(nome, idade)

    elif escolha == '2':
        listar_usuarios()

    elif escolha == '3':

        nome = input("Digite o nome do usuário: ").strip()

        if nome == "":
            print("Nome inválido.")
            continue

        buscar_usuario(nome)

    elif escolha == '4':

        nome = input("Digite o nome do usuário: ").strip()

        if nome == "":
            print("Nome inválido.")
            continue

        atualizar_usuario(nome)

    elif escolha == '5':

        nome = input("Digite o nome do usuário: ").strip()

        if nome == "":
            print("Nome inválido.")
            continue

        remover_usuario(nome)

    elif escolha == '6':

        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")