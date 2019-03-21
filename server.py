from flask import Flask, render_template, request
from pessoa import Pessoa

app = Flask(__name__)


@app.route('/')
def init():
    return render_template('inicio.html')

@app.route('/form_cadastrar')
def form_cadastrar():
    return render_template('form_cadastrar.html')

@app.route('/cadastrar_pessoa')
def cadastrar():
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    pessoa = Pessoa(nome, idade)
    arq = open('valores.txt', 'a')
    arq.write("{},{};".format(nome,idade))
    arq.close()
    return render_template('exibir_mensagem.html', pessoa=pessoa)

@app.route('/listar_pessoas')
def listar_pessoas():
    arq = open("valores.txt", "r")
    txt = arq.read()
    lista_pessoas = []
    cont_arq = txt.split(';')
    for i in cont_arq:
        i.split(',')
    for dados_pessoa in cont_arq:
        lista_pessoas.append(Pessoa(dados_pessoa[0], dados_pessoa[1]))
    return render_template("listar_pessoas.html", lista_pessoas=lista_pessoas)



app.run()
