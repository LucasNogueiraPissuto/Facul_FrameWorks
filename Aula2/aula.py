from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello Word Flask!"

@app.route('/dados')
def dados():
    
    nota1 = request.args.get('nota1', type=float)
    nota2 = request.args.get('nota2', type=float)
    
    media = (nota1 + nota2) / 2

    if media >= 7:
        return f"Aprovado! :D Notas: {nota1}, {nota2}"
    elif media > 5 and media < 7:
        return f"Ficou de DP :/ Notas: {nota1}, {nota2}"

    return f"Reprovado :( Notas {nota1}, {nota2}"

@app.route('/status')
def status():
    nota1 = request.args.get('nota1', type=float)
    nota2 = request.args.get('nota2', type=float)
    
    media = (nota1 + nota2) / 2

    if media >= 7:
        resultado = "Aprovado"
    elif media > 5 and media < 7:
        resultado = "DP"
    else:
        resultado = "Reprovado"

    return render_template('index.html', resultado = resultado, media = media, nota1 = nota1, nota2 = nota2)
    
if __name__ == '__main__':
    app.run(debug=True)