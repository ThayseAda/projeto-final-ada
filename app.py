from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obter dados do formulário
    nome = request.form.get('nome')
    raca = request.form.get('raca')
    idade = request.form.get('idade')
    peso = request.form.get('peso')
    vacinado = request.form.get('vacinado', 'não')  # Valor padrão 'não' se não estiver definido

    # Validar e processar os dados
    try:
        idade = int(idade)
        if idade < 0:
            return "A idade não pode ser negativa. Tente novamente.", 400
    except ValueError:
        return "Por favor, insira um número válido para a idade.", 400

    try:
        peso = float(peso)
        if peso < 0:
            return "O peso não pode ser negativo. Tente novamente.", 400
    except ValueError:
        return "Por favor, insira um número válido para o peso.", 400

    # Renderizar a página de resultados
    return render_template('result.html', nome=nome, raca=raca, idade=idade, peso=peso, vacinado=vacinado)

if __name__ == '__main__':
    app.run(debug=True)
