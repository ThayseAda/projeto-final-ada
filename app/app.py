
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
            Especie = data.get('Especie')
            Idade = data.get('Idade')
            Peso = data.get('Peso')
            Data = data.get('Data')  # Certifique-se de que a chave 'Data' está no JSON
            Historico = data.get('Historico')

            if not all([Especie, Idade, Peso, Data, Historico]):
                return {'message': 'Missing data'}, 400

            # Inserção com parâmetros para evitar SQL Injection
            insert_query = text("""
                INSERT INTO Pets (Especie, Idade, Peso, Data, Historico)
                VALUES (:Especie, :Idade, :Peso, :Data, :Historico)
            """)
            conn.execute(insert_query, {
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
         

api.add_resource(Pets, '/pets')

if __name__ == '__main__':
    app.run(debug=True)