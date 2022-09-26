import json
from flask import Flask
from flask import request

import os
import sys

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./app/models/utils"))

from app.models.utils.utilitariosUsuarios import UtilitariosUsuarios
from app.models.login import Login
from app.models.empresa import Empresa

app = Flask(__name__)
app.debug = True

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
      login = Empresa(data['razaoSocial'],data['cnpj'],data['fantasia'],data['telefone'],data['e-mail'],data['cep'],
         data['logradouro'],data['bairro'],data['numero'],data['cidade'],data['tipo'],data['matriz'],)
      response = login.cadastrarEmpresa()
      return response

app.run()