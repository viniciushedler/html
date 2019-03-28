from flask import Flask, render_template, request
from pessoa import Pessoa
from gbd import GBD

servidor = '127.0.0.1'
usuario = 'root'
senha = 'root'
bd = 'html'
gbd = GBD(servidor, usuario, senha, bd)

app = Flask(__name__)


@app.route('/')
def init():
    return render_template('inicio.html')

@app.route('/form_cadastrar')
def  abre_form_cadastrar():
    return render_template('form_cadastrar.html')

@app.route('/cadastrar_pessoa')
def cadastrar():
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    pessoa = Pessoa(nome, idade)
    gbd.inserir_pessoa(pessoa)
    return render_template('exibir_mensagem.html', pessoa=pessoa)

@app.route('/listar_pessoas')
def listar_pessoas():
    lista_pessoas = gbd.listar_pessoas()
    # arq = open("valores.txt", "r")
    # txt = arq.read()
    # lista_pessoas = []
    # cont_arq = txt.split(';')
    # dados = []
    # for i in cont_arq:
    #     if i=='':
    #         cont_arq.remove(i)
    #     else:
    #         dados.append(i.split(','))
    # for dados_pessoa in dados:
    #     lista_pessoas.append(Pessoa(dados_pessoa[0], dados_pessoa[1]))
    return render_template("listar_pessoas.html", lista_pessoas=lista_pessoas, lista_index=range(len(lista_pessoas)))

@app.route('/deletar_pessoa')
def deletar_pessoa():
    nome = request.args.get('nome')
    gbd.deletar_pessoa(nome)
    lista_pessoas = gbd.listar_pessoas()
    return render_template("listar_pessoas.html", lista_pessoas=lista_pessoas, lista_index=range(len(lista_pessoas)))


app.run()
