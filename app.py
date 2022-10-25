from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Integer)
    nome = db.Column(db.String(128))
    senha = db.Column(db.String(128))
    cpf = db.Column(db.Integer)
    email = db.Column(db.String(128))
    logradouro = db.Column(db.String(128))
    numero = db.Column(db.String(128))
    complemento = db.Column(db.String(128))
    bairro = db.Column(db.String(128))
    cep = db.Column(db.String(128))
    telefone = db.Column(db.String(128))
    estado = db.Column(db.String(128))
    cidade = db.Column(db.String(128))
    criado_em = db.Column(db.Date())

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    razaoSocial = db.Column(db.String(128))
    cnpj = db.Column(db.Integer)
    nomeFantasia = db.Column(db.String(128))
    telefone = db.Column(db.String(128))
    email = db.Column(db.String(128))
    cep = db.Column(db.String(128))
    logradouro = db.Column(db.String(128))
    bairro = db.Column(db.String(128))
    numero = db.Column(db.String(128))
    cidade = db.Column(db.String(128))
    estado = db.Column(db.String(128))
    criado_em = db.Column(db.Date())