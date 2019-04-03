import MySQLdb
from pessoa import Pessoa

class GBD():
    '''meu gerenciador de bd para python'''

    def __init__(self, servidor='', usuario='', senha='', bd=''):
        self.login(servidor, usuario, senha, bd)
        self.con = MySQLdb.connect(self.servidor, self.usuario, self.senha)
        self.cursor = self.con.cursor()
        self.cursor.execute('CREATE SCHEMA IF NOT EXISTS {} COLLATE latin1_general_cs'.format(bd))
        self.con.select_db(bd)
        self.criar_tabela()

    def login(self, servidor, usuario, senha, bd):
        if servidor=='':
            servidor = input('Servidor: ')
        if usuario=='':
            usuario = input('Usuario: ')
        if senha=='':
            senha = input('Senha: ')
        if bd=='':
            bd = input('Banco de dados: ')
        self.servidor = servidor
        self.usuario = usuario
        self.senha = senha
        self.bd = bd
  
    def criar_tabela(self):
        nome_tabela = 'pessoa'
        atributos = '''
        cod INT,
        nome VARCHAR(60) not null,
        idade INT(3) not null
        '''
        self.cursor.execute('CREATE TABLE IF NOT EXISTS {}({})'.format(nome_tabela, atributos))
    
    def inserir_pessoa(self, pessoa):
        self.cursor.execute("INSERT INTO pessoa (cod, nome, idade) VALUES ('{}','{}','{}')".format(pessoa.cod, pessoa.nome,pessoa.idade))
        self.con.commit()

    def listar_pessoas(self):
        qtd_resultados = self.cursor.execute('SELECT * FROM pessoa')
        lista_pessoas = []
        for cont in range(qtd_resultados):
            dados = self.cursor.fetchone()
            pessoa = Pessoa(dados[0], dados[1], dados[2])
            lista_pessoas.append(pessoa)
        return lista_pessoas

    def deletar_pessoa(self, cod):
        self.cursor.execute("delete from pessoa where cod='{}'".format(cod))
        self.con.commit()        