# Aplicação de Cadastro e Consulta de Pets 🐾

Este projeto é uma aplicação web simples para gerenciar registros de pets. Desenvolvido com **Flask** e **SQLite**, oferece funcionalidades de cadastro, consulta e edição de informações dos pets.

## Funcionalidades ✨

- **Tela Inicial:** Permite ao usuário escolher entre as opções de cadastro ou consulta.
- **Cadastro de Pets:** Permite inserir informações sobre um pet, como nome, idade e peso. Após o cadastro, o usuário recebe uma notificação de sucesso.
- **Consulta de Pets:** Permite buscar pets cadastrados com base em nome, idade ou peso. Se o campo de busca estiver vazio, todos os pets cadastrados serão exibidos. A lista é atualizada somente quando o botão "Buscar" é clicado.
- **Edição de Pets:** Permite editar as informações de um pet cadastrado.

## Tecnologias Usadas 🛠️

- **Flask:** Framework web para Python.
- **SQLite:** Banco de dados leve e integrado.
- **HTML/CSS:** Para a construção das páginas e estilização.

## Estrutura do Projeto 📁

- `app.py`: Arquivo principal da aplicação Flask. Define rotas e lógica de backend.
- `templates/`: Diretório contendo os templates HTML para as páginas da aplicação.
  - `index.html`: Tela inicial para seleção de cadastro ou consulta.
  - `cadastro.html`: Página para o cadastro de novos pets.
  - `consulta.html`: Página para a consulta e visualização dos pets cadastrados.
  - `editar.html`: Página para editar os pets cadastrados
- `static/`: Diretório contendo arquivos estáticos como CSS e imagens.
  - `style.css`: Arquivo de estilização para as páginas HTML.

## Instruções de Instalação 🚀

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

## Contribuindo 🤝

Por favor, leia o [CONTRIBUTING.md](./CONTRIBUTING.md) para detalhes sobre o processo de contribuição.

## Diretrizes para Pull Requests 🚀
1. Faça um fork do repositório.
2. Crie uma branch para sua feature (``git checkout -b minha-feature``).
3. Faça o commit das suas mudanças (``git commit -m 'Adiciona minha feature'``).
4. Envie para a branch (``git push origin minha-feature``).
5. Abra um Pull Request seguindo a [documentação](./pull_request_template.md).

## Código de Conduta 📜

Ao contribuir para este projeto, você concorda em seguir o nosso [Código de Conduta](./CODE_OF_CONDUCT.md), que ajuda a garantir um ambiente colaborativo e inclusivo.

## Licença 📄

Este projeto está licenciado sob a [MIT License](./LICENSE).

---

Agradecemos por contribuir para o projeto!