import sqlite3
import bcrypt

class Login():

    def login(self, usuario):

        response = {
            "msg" : "",
            "color_msg" : ()
        }

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        for dados in cursor.execute(""" SELECT senha FROM usuarios WHERE email=?; """, (usuario["email"],)):
            if(dados):
                if bcrypt.checkpw(usuario["senha"].encode('utf8'), dados[0]):
                    response["msg"] = "Login realizado com sucesso!"
                    response["color_msg"] = (40/255, 167/255, 67/255, 1)
                    return response
                else:
                    response["msg"] = "Senha inválida !"
                    response["color_msg"] = (220/255, 53/255, 69/255, 1)
                    return response
        response["msg"] = "Email/Usuario não existe!"
        response["color_msg"] = (220/255, 53/255, 69/255, 1)
        return response