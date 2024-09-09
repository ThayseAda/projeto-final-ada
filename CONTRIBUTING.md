# Contribuindo com o Projeto

Obrigado por considerar contribuir com o **projeto-final-ada**! Este documento orienta como você pode contribuir de forma eficiente e de acordo com as práticas estabelecidas.

## Requisitos

Certifique-se de ter as seguintes ferramentas instaladas antes de começar:

- **Python 3.9+**
- **Pipenv** (para gerenciar dependências)
- **Docker** (opcional, para testes locais)
- **Git** (para controle de versão)

## Boas Práticas de Commit
Use as convenções de commit para manter um histórico limpo e claro. Seguem algumas diretrizes:

-   Use verbos no imperativo para descrever as mudanças.
-   Estruture suas mensagens da seguinte forma:
    - **Tipo**: tipo de mudança (ex: feat, fix, docs, refactor, test).
    - **Escopo**: o módulo ou parte do código afetado pela mudança.
    - **Mensagem**: uma breve descrição do que foi alterado.

### Exemplo:
```scss
feat(users): add user registration functionality
```

## Tipos de Commits
- ``feat``: Adiciona uma nova funcionalidade.
- ``fix``: Corrige um bug.
- ``docs``: Altera a documentação.
- ``style``: Ajusta formatação, espaçamento, etc. (não afeta lógica de código).
- ``refactor``: Refatoração do código sem mudança de funcionalidade.
- ``test``: Adiciona ou corrige testes.
- ``chore``: Outras mudanças menores.

## Criando Pull Requests
Ao enviar uma pull request (PR):

1. Certifique-se de que sua branch está atualizada com a ``main``.
2. Verifique se todos os testes estão passando localmente:
```bash
pytest
```
3. Descreva claramente as mudanças e o propósito da PR.
4. Aguarde a revisão e faça ajustes se necessário.

### Executando Testes
1. Configure o ambiente de testes:

```bash
flask db upgrade
```
2. Execute os testes com o Pytest:

```bash
pytest
```

### Código de Conduta
Por favor, siga nosso [Código de Conduta](./CODE_OF_CONDUCT.md) para garantir um ambiente colaborativo e respeitoso.

---