
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from sqlalchemy import text



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
            Data = data.get('Data')  # Certifique-se de que a chave 'Data' está no JSON
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
           

            # Consulta para obter o último pet inserido
            consulta_query = text("""
                                    select * from Pets order by Id desc limit 1
                                  """)
            query = conn.execute(consulta_query )
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)  
       
        except:
           conn.rollback()
        finally:
           conn.close()
class PetsById(Resource):
    def delete(self, Id):
        conn = db_connect.connect()
        try:
           
            delete_query = text("""
                DELETE FROM Pets WHERE Id = :Id
            """)
            result = conn.execute(delete_query, {'Id': Id})
            conn.commit()

            if result.rowcount == 0:
                return {"Mensagem": "Pet não Encontrado"}, 404

            return {"Status": "Pet Deletado com Sucesso"}

        except SQLAlchemyError as e:
            conn.rollback()
            return {"Mensagem": str(e)}, 500
        finally:
            conn.close()

    def get(self, Id):
        conn = db_connect.connect()
        try:
    
            select_query = text("""
                SELECT * FROM Pets WHERE Id = :Id
            """)
            query = conn.execute(select_query, {'Id': Id})
            result = [dict(zip(query.keys(), row)) for row in query.fetchall()]

            if not result:
                return {"Mensagem": "Pet não Encontrado!"}, 404

            return jsonify(result)

        except SQLAlchemyError as e:
            return {"Mensagem": str(e)}, 500
        finally:
            conn.close()
            
api.add_resource(Pets, '/pets')
api.add_resource(PetsById, '/pets/<int:id>')                 



if __name__ == '__main__':
    app.run(debug=True)