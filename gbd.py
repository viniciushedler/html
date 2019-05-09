import MySQLdb
from pessoa import Pessoa
from tabela import Tabela

class GBD():
    '''meu gerenciador de bd para python'''

    def __init__(self, servidor='', usuario='', senha='', bd=''):
        self.login(servidor, usuario, senha, bd)
        self.con = MySQLdb.connect(self.servidor, self.usuario, self.senha)
        self.cursor = self.con.cursor()
        self.cursor.execute('CREATE SCHEMA IF NOT EXISTS {} COLLATE latin1_general_cs'.format(bd))
        self.con.select_db(bd)
        self.criar_texto_tabelas()
        self.criar_tabelas_bd()
        self.conectar_usuario_init()
    
    def conectar_usuario_init(self):
        self.cursor.execute('select count(*) from usuario')
        n = self.cursor.fetchone()
        if n[0]==0:
            self.cursor.execute('insert into usuario values (-1)')
            self.con.commit()


    def criar_texto_tabelas(self):
        self.tabelas = []
        tabela = Tabela('pessoa',
        '''
        cod INT,
        nome VARCHAR(60) not null,
        idade INT(3) not null,
        senha VARCHAR(60) not null
        ''')
        self.tabelas.append(tabela)
        tabela = Tabela('usuario',
        '''
        cod INT
        ''')
        self.tabelas.append(tabela)

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
  
    def criar_tabelas_bd(self):
        for tabela in self.tabelas:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS {}({})'.format(tabela.nome, tabela.atributos))
    
    def inserir_pessoa(self, pessoa):
        self.cursor.execute("INSERT INTO pessoa (cod, nome, idade, senha) VALUES ('{}','{}','{}','{}')".format(pessoa.cod, pessoa.nome,pessoa.idade, pessoa.senha))
        self.con.commit()

    def listar_pessoas(self):
        qtd_resultados = self.cursor.execute('SELECT * FROM pessoa')
        lista_pessoas = []
        for cont in range(qtd_resultados):
            dados = self.cursor.fetchone()
            pessoa = Pessoa(dados[0], dados[1], dados[2], dados[3])
            lista_pessoas.append(pessoa)
        return lista_pessoas

    def deletar_pessoa(self, cod):
        self.cursor.execute("delete from pessoa where cod='{}'".format(cod))
        self.con.commit()        

    def querry(self, tabela, valor, atributo='cod'):
        '''
        querry(tabela, valor, atributo='cod')
        select from TABELA where VALOR=ATRIBUTO
        '''
        self.cursor.execute("select * from {} where {}='{}'".format(tabela,atributo,valor))
        dados = self.cursor.fetchone()
        pessoa = Pessoa(dados[0], dados[1], dados[2], dados[3])
        return pessoa
        
    def login_usuario(self, pessoa):
        self.cursor.execute("update usuario set cod={}".format(pessoa.cod))
        self.con.commit()

    def logout_usuario(self):
        self.cursor.execute("update usuario set cod=-1")
        self.con.commit()

    def get_cod_usuario(self):
        self.cursor.execute('select * from usuario')
        cod_usuario = self.cursor.fetchone()
        return cod_usuario[0]
