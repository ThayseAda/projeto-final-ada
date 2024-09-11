
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from sqlalchemy import text

# Obs:O SQLAlchemy é um ORM (Object-Relational Mapper) poderoso que facilita a 
# interação entre o Python e os bancos de dados, permitindo que se trabalhe com tabelas
# de banco de dados como se fossem classes Python. Isso abstrai muitas das complexidades
# associadas ao gerenciamento de bancos de dados.
# Utilizar o SQLAlchemy no Flask é simples, graças à extensão Flask-SQLAlchemy, que 
# integra as funcionalidades do ORM diretamente na aplicação Flask.

# Resource: É uma classe base fornecida pelo Flask-RESTful.
#  Quando você herda de Resource, podemos
#  definir os métodos HTTP que seu recurso deve manipular.

#Frameworks de API RESTful: Flask-RESTful é uma extensão para o 
# framework Flask que facilita a criação de APIs RESTful. 
# Em Flask-RESTful, recursos são representados como classes.



db_connect = create_engine('sqlite:///PetData.db')
app = Flask(__name__)
api = Api(app)

class Pets(Resource):
   
    def post(self):
        try:
            conn = db_connect.connect()
            # Extração e validação dos dados do JSON
            data = request.get_json()
            Nome = data.get("Nome")
            Especie = data.get('Especie')
            Idade = data.get('Idade')
            Peso = data.get('Peso')
            Data = data.get('Data') 
            Historico = data.get('Historico')

            if not all([Nome,Especie, Idade, Peso, Data, Historico]):
                return {'message': 'Missing data'}, 400

            # Inserção com parâmetros para evitar SQL Injection
            insert_query = text("""
                INSERT INTO Pets (Nome,Especie,Idade,Peso,Data,Historico)
                VALUES (:Nome,:Especie,:Idade,:Peso,:Data,:Historico)
            """)
            conn.execute(insert_query, {
                'Nome': Nome,
                'Especie': Especie,
                'Idade': Idade,
                'Peso': Peso,
                'Data': Data,
                'Historico': Historico
            })
            conn.commit()
           

            # Obtem o último pet inserido

            consulta_query = text("""
                                    SELECT * FROM Pets ORDER BY Id DESC LIMIT 1
                                  """)
            query = conn.execute(consulta_query )
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)  
       
        except:
           conn.rollback()
        finally:
           conn.close()

    def get(self):
        try:
         conn = db_connect.connect()
         query_lista_todos_pets = text("""
                 SELECT * FROM Pets
                 """)
         query = conn.execute(query_lista_todos_pets )
         result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
         return jsonify(result)   
        except:
           conn.close()

    def put(self):
        conn = db_connect.connect()
        try:
            data = request.get_json()
            Id = data.get('Id')
            Nome = data.get('Nome')
            Especie = data.get('Especie')
            Idade = data.get('Idade')
            Peso = data.get('Peso')
            Data = data.get('Data')
            Historico = data.get('Historico')

            if not Id:
                return {'message': 'ID is required'}, 400

            update_query = text("""
                UPDATE Pets
                SET Nome = :Nome,
                    Especie = :Especie,
                    Idade = :Idade,
                    Peso = :Peso,
                    Data = :Data,
                    Historico = :Historico
                WHERE Id = :Id
            """)
            conn.execute(update_query, {
                'Nome': Nome,
                'Especie': Especie,
                'Idade': Idade,
                'Peso': Peso,
                'Data': Data,
                'Historico': Historico,
                'Id': Id
            })
            conn.commit()

            query_pet_alterado = text("""
                SELECT * FROM Pets WHERE Id = :Id
            """)
            query = conn.execute(query_pet_alterado, {'Id': Id})
            result = [dict(zip(query.keys(), row)) for row in query.fetchall()]
            return jsonify(result)

        except SQLAlchemyError as e:
            conn.rollback()
            return {'Mensagem': str(e)}, 500
        finally:
            conn.close()   


api.add_resource(Pets, '/pets')
         

if __name__ == '__main__':
    app.run(debug=True)