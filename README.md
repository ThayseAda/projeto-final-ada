# Aplicação de Cadastro e Consulta de Pets

Esta é uma aplicação web simples para cadastrar e consultar informações sobre pets. Desenvolvida usando Flask e SQLite, a aplicação permite aos usuários registrar novos pets, bem como buscar informações sobre eles com base em critérios como nome, idade ou peso.

## Funcionalidades

- **Tela Inicial:** Permite ao usuário escolher entre as opções de cadastro ou consulta.
- **Cadastro de Pets:** Permite inserir informações sobre um pet, como nome, idade e peso. Após o cadastro, o usuário recebe uma notificação de sucesso.
- **Consulta de Pets:** Permite buscar pets cadastrados com base em nome, idade ou peso. Se o campo de busca estiver vazio, todos os pets cadastrados serão exibidos. A lista é atualizada somente quando o botão "Buscar" é clicado.
- **Edição de Pets:** Permite editar as informações de um pet cadastrado.

## Tecnologias Utilizadas

- **Flask:** Framework web para Python.
- **SQLite:** Banco de dados leve e integrado.
- **HTML/CSS:** Para a construção das páginas e estilização.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask. Define rotas e lógica de backend.
- `templates/`: Diretório contendo os templates HTML para as páginas da aplicação.
  - `index.html`: Tela inicial para seleção de cadastro ou consulta.
  - `cadastro.html`: Página para o cadastro de novos pets.
  - `consulta.html`: Página para a consulta e visualização dos pets cadastrados.
- `static/`: Diretório contendo arquivos estáticos como CSS e imagens.
  - `style.css`: Arquivo de estilização para as páginas HTML.

## Instruções de Instalação

1. **Clone o Repositório:**
```bash
   git https://github.com/viniciuscaol/projeto-final-ada.git
   cd projeto-final-ada
```

2. **Instale as Dependências:** Certifique-se de ter o Python instalado e crie um ambiente virtual:
```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
```
Em seguida, instale as dependências:
```bash
    pip install -r requirements.txt
```

3. **Inicialize o Banco de Dados:** Certifique-se de que o arquivo **pet.db**  esteja criado e configure o esquema do banco de dados. O arquivo **app.py** deve criar automaticamente o banco de dados e a tabela pets se não existirem.
</br>

4. **Execute a Aplicação:**
```bash
  python app.py
```
A aplicação estará disponível em http://localhost:5000.