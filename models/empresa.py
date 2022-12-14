import sqlite3
from datetime import datetime
from .utils.utils import Utils
from .utils.message import message

class Empresa():

    def __init__(self, *args):

        if(len(args) == 12):
            self.razaoSocial = args[0]
            self.cnpj = args[1]
            self.nomeFantasia = args[2]
            self.telefone = args[3]
            self.email = args[4]
            self.cep = args[5]
            self.logradouro = args[6]
            self.bairro = args[7]
            self.numero = args[8]
            self.cidade = args[9]
            self.estado = args[10]
            self.tipo = args[11]

    def cadastrarEmpresa(self):
        self.razaoSocial = self.razaoSocial.upper()


        if(not Utils.validarCnpj(self.cnpj)):
            return message("Cnpj inválido!", (220/255, 53/255, 69/255, 1))
            
        self.cnpj = self.converteCnpjNumero(self.cnpj)

        conn = sqlite3.connect('instance/app.db')
        cursor = conn.cursor()

        for dados in cursor.execute(""" SELECT * FROM empresas WHERE cnpj=?; """, (self.cnpj,)):
            if(dados):
               return message("O cnpj já está cadastrado !", (220/255, 53/255, 69/255, 1))
        
        self.nomeFantasia = self.nomeFantasia.upper()

        if(len(self.telefone) > 11):
            return message("Telefone inválido", (220/255, 53/255, 69/255, 1))
        
        if(not Utils.validarEmail(self.email)):
            return message("Email invalido", (220/255, 53/255, 69/255, 1))
        
        if(not Utils.validarCep(self.cep)):
            return message("Cep inválido", (220/255, 53/255, 69/255, 1))
        
        self.logradouro = self.logradouro.capitalize()

        self.bairro = self.bairro.capitalize()
        
        if(len(self.numero) > 4):
            return message("Numero da casa inválido", (220/255, 53/255, 69/255, 1))
        
        self.cidade = self.cidade.capitalize()

        self.estado = self.estado.capitalize()

        self.tipo = self.tipo.upper()

        cursor.execute("""INSERT INTO empresas (razaoSocial, cnpj, nomeFantasia, telefone, email, cep, logradouro, 
        bairro, numero, cidade, estado, tipo, criado_em)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);
        """, (self.razaoSocial, self.cnpj, self.nomeFantasia, self.telefone, self.email, self.cep, self.logradouro, self.bairro, self.numero, self.cidade, self.estado, self.tipo, datetime.today().strftime('%d-%m-%Y')))

        conn.commit()
        conn.close()
        return message("Dados inseridos com sucesso!", (40/255, 167/255, 67/255, 1))
    
    def excluirEmpresa(self, razaoSocial):
        conn = sqlite3.connect('instance/app.db')
        
        cursor = conn.cursor()

        for dados in cursor.execute(""" SELECT * FROM empresas WHERE razaoSocial=?; """, (razaoSocial,)):
            if(dados):
                cursor.execute("DELETE FROM empresas WHERE razaoSocial=?;", (razaoSocial,))

                conn.commit()
                
                conn.close()
            
                return "Dados EXCLUIDOS com sucesso."

        return "Não existe empresa para a exclusão !"
    
    def atualizarEmpresa(self, updateEmpresa):
        conn = sqlite3.connect('instance/app.db')
        cursor = conn.cursor()

        for dados in cursor.execute(""" SELECT * FROM empresas WHERE razaoSocial=?; """, (updateEmpresa['alvo'],)):
            if(dados):
                empresa = {
                    "razaoSocial" : dados[1],
                    "cnpj" : dados[2],
                    "nomeFantasia" : dados[3],
                    "telefone" : dados[4],
                    "email" : dados[5],
                    "cep" : dados[6],
                    "logradouro" : dados[7],
                    "bairro" : dados[8],
                    "numero" : dados[9],
                    "cidade" : dados[10],
                    "estado" : dados[11],
                    "tipo" : dados[12]
                }

                for chave, valor in updateEmpresa.items():
                    if valor != "":
                        if chave == "razaoSocial" or chave == "nomeFantasia" or chave == "tipo":
                            empresa[chave] = valor.upper()
                        if chave == "cnpj":
                            if(not Utils.validarCnpj(valor)):
                                return "Cnpj invalido"
                            empresa[chave] = valor
                        if chave == "telefone":
                            if(len(valor) > 11):
                                return "Telefone inválido"
                            empresa[chave] = valor
                        if chave == "email":
                            if(not Utils.validarEmail(valor)):
                                return "Email invalido"
                            empresa[chave] = valor
                        if chave == "cep":
                            if(not Utils.validarCep(valor)):
                                return "Cep inválido"
                            empresa[chave] = valor
                        if chave == "logradouro" or chave == "bairro" or chave == "cidade" or chave == "estado":
                            empresa[chave] = valor.capitalize()
                        if chave == "numero":
                            if(len(valor) > 4):
                                return "Numero da casa inválido"
                            empresa[chave] = valor

                cursor.execute(""" UPDATE empresas SET 
                                razaoSocial = ?,
                                cnpj = ?,
                                nomeFantasia = ?,
                                telefone = ?,
                                email = ?,
                                cep = ?,
                                logradouro = ?,
                                bairro = ?,
                                numero = ?,
                                cidade = ?,
                                estado = ?,
                                tipo = ?
                                WHERE razaoSocial=?
                                ;""",
                    (empresa["razaoSocial"], empresa["cnpj"], empresa["nomeFantasia"],
                        empresa["telefone"], empresa["email"], empresa["cep"], empresa["logradouro"],
                        empresa["bairro"], empresa["numero"], empresa["cidade"], empresa["estado"],
                        empresa["tipo"], updateEmpresa['alvo']))

                conn.commit()
                
                conn.close()
            
                return "Atualizado com sucesso."

        return "Não existe empresa para a atualização !"
    
    def lerTabelaEmpresa(self):
        conn = sqlite3.connect('instance/app.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM empresas; """)

        lista = []

        for linha in cursor.fetchall():
            lista.append(linha)

        conn.close()

        return ['Leitura de Empresa.', lista]
    
    def converteCnpjNumero(self, cnpj):
        numbers = ""
        for digit in cnpj:
            if digit.isdigit():
                numbers = numbers + digit
        return int(numbers)
