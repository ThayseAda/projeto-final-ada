from flask import Flask, jsonify, request
from sql import pyodbc



app = Flask(__name__)

pets = [
    {
        'id': 1,
        'pet': "cachorro",
        'idade': "12"
    },
    {
        'id': 2,
        'pet': "gato",
        'idade': "12"
    }
]

# Consultar todos
@app.route('/peths')
def obter_peths():
    return jsonify(pets)

app.run(port=5500,host='localhost',debug=True)