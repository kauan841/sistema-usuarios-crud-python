import json

def ler_arquivo_json():
    caminho = "C:\\Users\\kaike\\Desktop\\CRUD\dados\\login.json"
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    

def ler_json():
    caminho = "C:\\Users\\kaike\\Desktop\\CRUD\dados\\adicionar.json"
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}