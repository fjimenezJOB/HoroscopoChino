# Horoscopo chino
from flask import Flask, render_template, url_for, request, redirect
from metodos import Metodos

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def ligica():
    global animal
    anyo = int(request.form['anyo'])
    pregunta = Metodos()
    animal = pregunta.calculo(anyo)

    # Logica para texto
    global texto
    texto = pregunta.consultar(animal)
    print(texto + '*'*50)

    return redirect(url_for('signo'))


@app.route('/signo')
def signo():
    return render_template('signo.html', animal=animal, texto=texto)


@app.errorhandler(404)
def error(error):
    return '<h1> Pagina no encontrada...(404)<h1>'


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
