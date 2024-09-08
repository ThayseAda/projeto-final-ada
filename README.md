# Projeto Final ADA

Este é o repositório para o projeto final do curso ADA. O objetivo deste projeto é desenvolver uma aplicação de coleta de informações sobre pets, adicionar melhorias ao código, escrever testes unitários e de integração, e configurar uma pipeline de CI/CD usando GitHub Actions para deploy na EC2.

## Sumário

1. [Descrição do Projeto](#descrição-do-projeto)
2. [Como Usar](#como-usar)
3. [Instalação](#instalação)
4. [Documentação](#documentação)
5. [Como Contribuir](#como-contribuir)
6. [Licença](#licença)
7. [Histórico de Commits](#histórico-de-commits)
8. [Testes](#testes)
9. [GitHub Actions](#github-actions)

## Descrição do Projeto

Este projeto é uma aplicação para coletar informações sobre pets. As principais funcionalidades incluem a coleta e validação de dados como nome, idade e peso do pet. Melhorias foram implementadas para validar a entrada dos dados e foram adicionados testes para garantir o funcionamento correto da aplicação.

## Como Usar

Para utilizar a aplicação:

1. Clone o repositório:
   ```bash
   git clone https://github.com/akillez01/projeto-final-ada-achilles.git
   cd projeto-final-ada-achilles
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # No Windows
   source venv/bin/activate   # No Unix/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   python run.py
   ```

## Instalação

Para configurar o ambiente de desenvolvimento e instalar as dependências:

1. Instale o Flask e Waitress:
   ```bash
   pip install Flask Waitress
   ```

2. Se necessário, atualize o pip:
   ```bash
   python -m pip install --upgrade pip
   ```

3. Para configurar o GitHub Actions e outras ferramentas de CI/CD, adicione a configuração específica no diretório `.github/workflows`.

## Documentação

- **app.py**: Contém o código principal da aplicação Flask.
- **run.py**: Script para executar a aplicação com Waitress.
- **info_pet.py**: Código para coleta e processamento de informações dos pets.
- **test_coletar_informacoes_pet.py**: Testes unitários para o código de coleta de informações dos pets.
- **requirements.txt**: Lista de dependências do projeto.

## Como Contribuir

Para contribuir com o projeto:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça suas alterações e adicione commits:
   ```bash
   git add .
   git commit -m "descrição das mudanças"
   ```
4. Envie suas alterações para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request para revisão.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Histórico de Commits

- **feat**: Adiciona suporte ao Waitress para execução do servidor.
- **fix**: Corrige problemas de importação e dependências.
- **docs**: Atualiza README.md com informações sobre instalação e execução.
- **test**: Adiciona testes unitários para validação de dados de entrada.

## Testes

Para executar os testes unitários:

1. Certifique-se de que o ambiente virtual está ativado.
2. Execute os testes:
   ```bash
   pytest
   ```

## GitHub Actions

A configuração de CI/CD para deploy na EC2 está disponível no diretório `.github/workflows`. A pipeline executa os seguintes passos:

1. Testes.
2. Build.
3. Deploy na instância EC2 da AWS.
```