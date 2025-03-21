from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para criar a tabela LIVROS no banco de dados SQLite
def criar_tabela():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS LIVROS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            autor TEXT NOT NULL,
            imagem_url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Rota inicial (/)
@app.route('/')
def home():
    return 'Bem-vindo à API de Doação de Livros! Use /doar para cadastrar e /livros para listar.'

# Rota para cadastrar um livro (POST /doar)
@app.route('/doar', methods=['POST'])
def doar_livro():
    data = request.get_json()
    titulo = data.get('titulo')
    categoria = data.get('categoria')
    autor = data.get('autor')
    imagem_url = data.get('imagem_url')

    if not titulo or not categoria or not autor or not imagem_url:
        return jsonify({'mensagem': 'Dados incompletos!'}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO LIVROS (titulo, categoria, autor, imagem_url) VALUES (?, ?, ?, ?)',
                   (titulo, categoria, autor, imagem_url))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Livro cadastrado com sucesso!'}), 201

# Rota para listar todos os livros (GET /livros)
@app.route('/livros', methods=['GET'])
def listar_livros():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM LIVROS')
    livros = cursor.fetchall()
    conn.close()

    resultado = []
    for livro in livros:
        resultado.append({
            'id': livro[0],
            'titulo': livro[1],
            'categoria': livro[2],
            'autor': livro[3],
            'imagem_url': livro[4]
        })

    return jsonify(resultado)

if __name__ == '__main__':
    criar_tabela()  # Cria a tabela se ela não existir
    app.run(debug=True)
