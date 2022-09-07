from crypt import methods
import json
from urllib import response
from flask import Flask
from flask import request

import os
import sys

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./app/models/utils"))

from app.models.utils.utilitariosUsuarios import UtilitariosUsuarios
from app.models.login import Login

app = Flask(__name__)

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
app.run("192.168.0.11", "8000")