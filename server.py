from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def init():
    return render_template('inicio.html')

@app.route('/form_cadastrar')
def cadastrar():
    return render_template('form_cadastrar.html')


app.run()
