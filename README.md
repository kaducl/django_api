## 🇬🇧 English Version

# CodeLeap Network API

A simple and robust RESTful API built with Python, Django, and Django REST Framework. This project serves as the backend for the CodeLeap Network, enabling full CRUD (Create, Read, Update, Delete) functionality for posts.

This project was developed as a technical challenge for a Backend Developer position at CodeLeap.

► Key Features

The API implements the four fundamental CRUD (Create, Read, Update, Delete) operations, allowing for complete management of posts.

    List all posts: Returns a list of all posts, sorted from newest to oldest.

    Create a new post: Allows the creation of a new post with a username, title, and content.

    View a single post's details: Returns data for a specific post via its id.

    Update a post: Allows updating the title and content of an existing post.

    Delete a post: Removes a post from the database.

    Pagination: List results are paginated (10 items per page) to ensure high performance and scalability.

► Core Technologies

    Python

    Django & Django REST Framework (DRF)

    SQLite3 (for development)

► Getting Started

To run this project on your local machine, follow these steps.

1. Clone & Setup Environment
```bash
git clone https://github.com/kaducl/django_api
cd django_api
python -m venv venv

# Activate the environment on Windows
venv\Scripts\activate

# Or on Mac/Linux
source venv/bin/activate
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Prepare Database
```bash
python manage.py migrate
```
4. Run Server
```bash
python manage.py runserver
```
The API will be available at http://127.0.0.1:8000/.

### ► API Endpoints

All endpoints are available under the `/careers/` prefix.

| Method | Endpoint          | Description                                             |
| :----- | :---------------- | :------------------------------------------------------ |
| `GET`  | `/careers/`       | Retrieves the list of all posts, sorted by most recent. |
| `POST` | `/careers/`       | Creates a new post.                                     |
| `GET`  | `/careers/{id}/`  | Retrieves a single post by its ID.                      |
| `PATCH`| `/careers/{id}/`  | Partially updates an existing post.                     |
| `DELETE`| `/careers/{id}/` | Deletes a specific post.                                |

The easiest way to test all endpoints is through the Browsable API provided by DRF at http://127.0.0.1:8000/careers/.

Developed by: Carlos Eduardo Lobato

## 🇧🇷 Versão em Português (Brasil)

# API da Rede CodeLeap 

Este projeto é uma API RESTful, construída com o poder do Python e do ecossistema Django, para gerenciar os posts de uma rede social. 

Este projeto foi desenvolvido como parte do desafio técnico para a vaga de Desenvolvedor Backend na CodeLeap.

► Funcionalidades Principais

A API implementa as quatro operações fundamentais de um CRUD (Create, Read, Update, Delete), permitindo o gerenciamento completo dos posts.

    Listar todos os posts: Retorna uma lista de todos os posts, ordenados dos mais recentes para os mais antigos.

    Criar um novo post: Permite a criação de um novo post com username, title e content.

    Ver detalhes de um post: Retorna os dados de um post específico através do seu id.

    Atualizar um post: Permite a atualização do title e content de um post existente.

    Deletar um post: Remove um post do banco de dados.

    Paginação: Os resultados das listas são paginados (10 itens por página) para garantir performance e escalabilidade.

► Ferramentas Utilizadas

    Linguagem: Python

    Framework Principal: Django

    Criação da API: Django REST Framework (DRF)

    Banco de Dados (Desenvolvimento): SQLite3

► Como Colocar para Rodar

Para ter a API funcionando na sua máquina, o caminho é simples:
```bash
1. Clone e Prepare o Ambiente
git clone https://github.com/kaducl/django_api
cd django_api
python -m venv venv

# Ative o ambiente no Windows:
venv\Scripts\activate

# Ou no Mac/Linux:
source venv/bin/activate
```
2. Instale os Pacotes Necessários
```bash
pip install -r requirements.txt
```
3. Construa o Banco de Dados
```bash
python manage.py migrate
```
4. Inicie o Servidor
```bash
python manage.py runserver
```
Pronto! A API já está no ar em http://127.0.0.1:8000/.

### ► Mapa dos Endpoints

O coração da nossa API bate no endpoint `/careers/`.

| Ação              | Verbo HTTP | Rota              | O que faz?                                                     |
| :---------------- | :--------- | :---------------- | :------------------------------------------------------------- |
| **Listar Posts** | `GET`      | `/careers/`       | Traz a lista completa de posts, ordenada pela data de criação. |
| **Criar um Post** | `POST`     | `/careers/`       | Publica um novo post na rede.                                  |
| **Ver um Post** | `GET`      | `/careers/{id}/`  | Mostra os detalhes de um único post.                           |
| **Editar um Post**| `PATCH`    | `/careers/{id}/`  | Atualiza as informações de um post.                            |
| **Deletar um Post**| `DELETE`   | `/careers/{id}/`  | Remove um post da plataforma.                                  |

A forma mais fácil de testar é pela API Navegável que o DRF nos dá de presente. É só acessar http://127.0.0.1:8000/careers/ e explorar!

Feito por: Carlos Eduardo Lobato

