# CRUDCore 👥

Sistema CRUD de usuários desenvolvido em Python com autenticação, persistência de dados em JSON e arquitetura modular.

---

## 🚀 Visão Geral

O CRUDCore é um projeto desenvolvido para praticar conceitos fundamentais e intermediários de programação com Python.

O sistema permite o gerenciamento completo de usuários através do terminal, incluindo autenticação, cadastro, atualização de dados e persistência das informações utilizando arquivos JSON.

Além das operações CRUD tradicionais, o projeto foi estruturado em múltiplos módulos para simular a organização utilizada em aplicações reais.

---

## ✨ Funcionalidades

### 🔐 Sistema de Autenticação

* Cadastro de usuários
* Login utilizando nome e idade
* Validação de credenciais
* Persistência dos dados de acesso

### 👥 Gerenciamento de Usuários

* Adicionar usuários
* Listar usuários cadastrados
* Buscar usuários específicos
* Atualizar informações
* Remover usuários

### 🛡️ Validações

* Campos obrigatórios
* Verificação de dados inválidos
* Tratamento de exceções
* Prevenção de usuários duplicados

### 💾 Persistência de Dados

* Armazenamento em arquivos JSON
* Carregamento automático dos dados ao iniciar o sistema
* Atualização automática após alterações

---

## 🧰 Tecnologias Utilizadas

* Python 3.14
* JSON
* Dicionários (`dict`)
* Estruturas condicionais (`if`, `elif`, `else`)
* Estruturas de repetição (`while`, `for`)
* Funções
* Modularização
* Tratamento de exceções (`try/except`)
* Git
* GitHub
* Ambiente Virtual (`venv`)

---

## 📂 Estrutura do Projeto

```bash
CRUDCore/
│
├── dados/
│   ├── login.json
│   └── adicionar.json
│
├── funcoes_do_crud/
│   ├── adicionar.py
│   ├── atualizar.py
│   ├── buscar.py
│   ├── arquivo.py
│   ├── listar.py
│   ├── login.py
│   └── remover.py
│
├── sistema_CRUD/
│   └── sistema_crud.py
│
├── venv/
│
└── README.md
```

---

## 💻 Exemplo de Execução

```text
Você deseja entrar no sistema? (s/n): s

Bem-vindo ao sistema CRUD de usuários!

1. Fazer cadastro
2. Fazer login

Escolha uma opção: 2

Digite seu nome:
Digite sua idade:

Login bem-sucedido!
```

---

## 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido para praticar:

* Lógica de programação
* Estruturas de dados
* Modularização de código
* Manipulação de arquivos JSON
* Persistência de dados
* Tratamento de erros
* Organização de projetos Python
* Versionamento com Git e GitHub

---

## 📈 Melhorias Futuras

* Implementação de senhas criptografadas
* Integração com SQLite
* Sistema de permissões
* Interface gráfica
* API REST com Flask
* Interface Web
* Testes automatizados
* Deploy em nuvem

---

## 👨‍💻 Autor

**Kauan Moraes**

Projeto desenvolvido com foco em aprendizado, prática de programação e evolução contínua como desenvolvedor Python.
