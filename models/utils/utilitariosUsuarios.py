import sqlite3
from datetime import datetime
import bcrypt
import re

import utils
from .message import message

class UtilitariosUsuarios():

    def cadastrarUsuario(self, usuario):

        usuario["nome"] = usuario["nome"].capitalize()

        usuario["senha"] = bcrypt.hashpw(bytes(usuario["senha"], 'utf-8'), bcrypt.gensalt())

        if not self.validarCpf(usuario["cpf"]):
            return message("Cpf inválido", (220/255, 53/255, 69/255, 1))
        
        usuario["cpf"] = self.converteCpfNumero(usuario["cpf"])
        
        conn = sqlite3.connect('instance/app.db')
        cursor = conn.cursor()
        
        for dados in cursor.execute(""" SELECT * FROM usuarios WHERE cpf=?; """, (usuario["cpf"],)):
            if(dados):
               return message("O cpf já está cadastrado !", (220/255, 53/255, 69/255, 1))

        if not utils.Utils.validarEmail(usuario["email"]):
            return message("Email invalido", (220/255, 53/255, 69/255, 1))
        
        usuario["logradouro"] = usuario["logradouro"].capitalize()

        if(len(usuario["numero"]) > 4):
            return message("Numero da casa inválido", (220/255, 53/255, 69/255, 1))
        
        usuario["complemento"] = usuario["complemento"].capitalize()

        usuario["bairro"]  = usuario["bairro"].capitalize()

        if not utils.Utils.validarCep(usuario["cep"]):
            return message("Cep inválido", (220/255, 53/255, 69/255, 1))
        
        if len(usuario["telefone"]) > 11:
            return message("Telefone inválido", (220/255, 53/255, 69/255, 1))
        
        usuario["cidade"] = usuario["cidade"].capitalize()

        usuario["estado"] = usuario["estado"].capitalize()

        cursor.execute("""INSERT INTO usuarios (nome, tipo, senha, cpf, email, logradouro, numero, 
        complemento, bairro, cep, telefone, cidade, estado, criado_em)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (usuario["nome"], usuario["tipo"], usuario["senha"], usuario["cpf"], usuario["email"], usuario["logradouro"], usuario["numero"], usuario["complemento"], usuario["bairro"], usuario["cep"], usuario["telefone"], usuario["cidade"], usuario["estado"], datetime.today().strftime('%d-%m-%Y')))

        conn.commit()
        conn.close()
        return message("Usuário cadastrado com sucesso!", (40/255, 167/255, 67/255, 1))

    def validarCpf(self, cpf):
        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True
    
    def converteCpfNumero(self, cpf):
        numbers = ""
        for digit in cpf:
            if digit.isdigit():
                numbers = numbers + digit
        return int(numbers)