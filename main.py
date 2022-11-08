from flask import request

import os
import sys

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./models/utils"))

from models.utils.utilitariosUsuarios import UtilitariosUsuarios
from models.login import Login
from models.empresa import Empresa
from app import app

@app.route("/lerDadosUsuario", methods=['POST'])

def lerDadosUsuario():
   if request.method == "POST":
      utilsUsuario = UtilitariosUsuarios()
      data = request.form.to_dict()
      response = utilsUsuario.lerDadosUsuario(data)

      return response

@app.route("/lerTabelaUsuarios", methods=['GET'])

def lerTabelaUsuarios():
   if request.method == "GET":
      utilsUsuario = UtilitariosUsuarios()
      response = utilsUsuario.lerTabelaUsuarios()

      return response

@app.route("/cadastroUsuario", methods=['POST'])

def cadastroUsuario():
   if request.method == "POST":
      utilsUsuario = UtilitariosUsuarios()
      data = request.form.to_dict()
      response = utilsUsuario.cadastrarUsuario(data)
      
      return response

@app.route("/login", methods=["POST"])

def login():
   if request.method == "POST":
      login = Login()
      data = request.form.to_dict()
      response = login.login(data)
      return response

@app.route("/cadastrarEmpresa", methods=["POST"])

def cadastrarEmpresa():
   if request.method == "POST":
      data = request.form.to_dict()
      login = Empresa(data['razaoSocial'],data['cnpj'],data['fantasia'],data['telefone'],data['email'],data['cep'],
         data['logradouro'],data['bairro'],data['numero'],data['cidade'],data['tipo'],data['matriz'],)
      response = login.cadastrarEmpresa()
      return response

app.run()