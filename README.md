# Projeto(Ada) Santander Coder 2024 
## Api - Gerenciamento de Pets

> [!NOTE]
> Objetivo do projeto
<br>
> Desenvolver uma API que disponibiliza algumas operações para o Cadastramento e Gerenciamento de Pets.

* Funcionalidades da API:
   - [X] Cadastrar Pet.
   - [X] Deletar Pet.
   - [X] Atulizar Pet.
   - [X] Listar Pets

### 🛠 Tecnologias<a id="tecnologias"></a>
 As seguintes ferramentas e tecnologias foram usadas na construção do projeto:
- Git
- [Vs Code](https://code.visualstudio.com/)<br>
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
<br>
- [Jsonify](https://jsonify.com/)
 <br>
- [Flask-restful](https://flask-restful.readthedocs.io/en/latest/)
 <br>
- [SQLite](https://www.sqlite.org/)
 <br>
- [SQLAlchemy](https://www.sqlalchemy.org/)
 <br>

 ###  Pré-requisitos<a id="pre-requisitos"></a>

Antes de começar, será preciso ter instalado em sua máquina as seguintes ferramentas:<br>
 [Git](https://git-scm.com/)
 <br>
 [Python3](https://www.python.org/downloads/)
 <br>
 [Postman](https://www.postman.com/downloads/)
 <br>
  Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

<br>

# :hammer: Preparando o o ambiente.

Supondo que o Python já esteje instalado.Siga os passos abaixo descrito:
<br>

> [!NOTE] Outra coisa importante deixe para instalar ele dentro do env flask!
<br>
Caso não tenha o pip instalado:
```terminal
 sudo apt install python3-pip
 ```
- Instalar o Flask
```
pip install flask

```
- Se quiser confirmar que seu ambiente virtual agora tem o Flask instalado, você pode iniciar o interpretador Python e importar o Flask para ele:
<br>
  " >> import flask" (sem Apas).


- Instale pelo terminal do VsCode:
```terminal
 sudo apt install python3-virtualenv 
 ```
- Criar:
``` terminal 
 virtualenv flask
 ```
 - Entrar no virtualenv:
 ```terminal
   cd flask
  ```
- Ativar o virtualenv:
```terminal
source bin/activate
```
***Agora você deve ver (flask)à esquerda da linha de comando.***

- Já com o env devidamente configurado, vamos instalar as libs do Flask que vamos utlizar. Nesse caso vamos utlizar:
 [X] **Flask** <br>
 [X] **FlaskFlask-Restful** <br>
 [X] **Flask-SQLAlchemy** <br>
 [X] **Jsonify** <br>
Para baixar essas libs basta executar no terminal o seguinte comando:
```terminal
 pip install flask flask-jsonpify flask-sqlalchemy flask-restful
```
<br>

# SQLite
Vou utilizar o SQLite como banco de dados.O Script para Gerar as Tabelas se encontran em:
[ScriptBD](database)
Outra coisa importante a se destacar é que  arquivo de banco de dados é PetData.db deverá ficar na raiz do projeto.

**Endpoints**


| Verbo  | Endpoint        | Parâmetro | Body          |
|--------|-----------------|-----------|---------------|
| GET    | /pets/          | Id        | N/A           |
| POST   | /pets           | N/A       | Schema Pet    |
| DELETE | /pets/          | Id        | N/A           |
| GET    | /pets           | N/A       | N/A           |
| PUT    | /pets           | N/A       | Schema Pet    |           
<br>
- Esse é o Schema Pet, utilizado para passar para os métodos que exigirem Body.
<br>
```json
{  
    "Nome": "Arara",
    "Especie":"Arara",
    "Idade":2,
    "Peso":20,
    "Data":"10-10-2024",
    "Historico":"Problema"
}
```

- Para testar os Endpoind utilizei o Postman como cliente REST API(Existem outros).O arquivo dos testes se encontram em postman_end-points, para usá-lo basta realizar a importação pelo postman.

# Licença
Projeto sob a licença do MIT. Se quiser saber leia lin<LICENSE>.

# Contribuição
Siga as diretivas do CONTRIBUTING.md nele estão instruções de contribuir para este projeto.



