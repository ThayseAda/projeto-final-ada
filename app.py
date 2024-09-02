from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

# Conectar ao banco de dados SQLite
def init_db():
    conn = sqlite3.connect('pet.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            peso REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Tela de seleção de cadastro ou consulta
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir o formulário de cadastro de pet
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para processar o cadastro do pet
@app.route('/add', methods=['POST'])
def add_pet():
    nome = request.form['nome']
    idade = request.form['idade']
    peso = request.form['peso']

    conn = sqlite3.connect('pet.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pets (nome, idade, peso) VALUES (?, ?, ?)", (nome, idade, peso))
    conn.commit()
    conn.close()

    return jsonify({'success': True})

# Rota para consulta de pets com filtro
@app.route('/consulta', methods=['GET'])
def consulta():
    criterio = request.args.get('criterio')
    valor = request.args.get('valor', '').strip()

    conn = sqlite3.connect('pet.db')
    cursor = conn.cursor()

    if valor:
        # Determinar o critério de busca e executar a query apropriada
        if criterio == 'nome':
            cursor.execute("SELECT * FROM pets WHERE nome LIKE ?", ('%' + valor + '%',))
        elif criterio == 'idade':
            try:
                idade = int(valor)
                cursor.execute("SELECT * FROM pets WHERE idade = ?", (idade,))
            except ValueError:
                return render_template('consulta.html', pets=[], erro="Idade inválida.")
        elif criterio == 'peso':
            try:
                peso = float(valor)
                cursor.execute("SELECT * FROM pets WHERE peso = ?", (peso,))
            except ValueError:
                return render_template('consulta.html', pets=[], erro="Peso inválido.")
    else:
        # Se não houver valor, listar todos os pets
        cursor.execute("SELECT * FROM pets")

    pets = cursor.fetchall()
    conn.close()

    return render_template('consulta.html', pets=pets, criterio=criterio, valor=valor)

# Rota para exibir o formulário de edição de pet
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_pet(id):
    conn = sqlite3.connect('pet.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        peso = request.form['peso']
        
        cursor.execute("UPDATE pets SET nome = ?, idade = ?, peso = ? WHERE id = ?", (nome, idade, peso, id))
        conn.commit()
        conn.close()
        
        return redirect('/consulta')
    
    cursor.execute("SELECT * FROM pets WHERE id = ?", (id,))
    pet = cursor.fetchone()
    conn.close()

    return render_template('editar.html', pet=pet)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
