from flask import Flask, render_template, request
from pessoa import Pessoa
from gbd import GBD

servidor = '127.0.0.1'
usuario = 'root'
senha_gbd = 'root'
bd = 'html'
gbd = GBD(servidor, usuario, senha_gbd, bd)

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
    senha = request.args.get('senha')
    lista_pessoas=gbd.listar_pessoas()
    for cod in range(len(lista_pessoas)+1):
        unico = True
        for pessoa in lista_pessoas:
            if cod==pessoa.cod:
                unico = False
                break
        if unico:
            codigo = cod
    pessoa = Pessoa(codigo ,nome, idade, senha)
    gbd.inserir_pessoa(pessoa)
    return render_template('exibir_mensagem.html', pessoa=pessoa)

@app.route('/listar_pessoas')
def listar_pessoas():
    lista_pessoas = gbd.listar_pessoas()
    return render_template("listar_pessoas.html", lista_pessoas=lista_pessoas, lista_index=range(len(lista_pessoas)))

@app.route('/deletar_pessoa')
def deletar_pessoa():
    cod = request.args.get('cod')
    gbd.deletar_pessoa(cod)
    lista_pessoas = gbd.listar_pessoas()
    return render_template("listar_pessoas.html", lista_pessoas=lista_pessoas, lista_index=range(len(lista_pessoas)))

@app.route('/form_editar')
def form_editar_pessoa():
    cod = request.args.get('cod')
    pessoa = gbd.buscar_pessoa(cod)
    return render_template('form_editar.html', pessoa=pessoa)

@app.route('/editar_pessoa')
def editar_pessoa():
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    cod = request.args.get('cod')
    senha = request.args.get('senha')
    print(cod)
    pessoa = gbd.buscar_pessoa(cod)
    if nome=='':
        nome = pessoa.nome
    if idade=='':
        idade=pessoa.idade
    if senha=='':
        senha = pessoa.senha
    pessoa = Pessoa(cod,nome,idade, senha)
    gbd.deletar_pessoa(cod)
    gbd.inserir_pessoa(pessoa)
    return render_template('exibir_mensagem.html', pessoa=pessoa)

@app.route('/form_login')
def form_login():
    return render_template('form_login.html')

@app.route('/login')
def login():
    user = request.args.get('user')
    senha = request.args.get('senha')
    pessoa = gbd.buscar_pessoa(user, 'nome')
    if senha==pessoa.senha:
        .


app.run(host='0.0.0.0')