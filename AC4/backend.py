from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'lpissuto',
    'password': '123456',
    'database': 'AC4_database'
}

@app.route('/buscar', methods=['GET'])
def get_dados():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tabela")
    rows = cursor.fetchall()

    results = []
    for row in rows:
        result = {
            'id': row[0],
            'campo1': row[1],
            'campo2': row[2]
        }
        results.append(result)

    conn.close()

    return jsonify(results)

@app.route('/inserir', methods=['POST'])
def post_dados():
    data = request.json
    campo1 = data['campo1']
    campo2 = data['campo2']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "INSERT INTO tabela (campo1, campo2) VALUES (%s, %s)"
    values = (campo1, campo2)
    cursor.execute(query, values)

    conn.commit()
    conn.close()
    return 'Dados inseridos com sucesso!'

if __name__ == '__main__':
    app.run()
