class Usuario:

    def __init__(self,nome,cpf,email,senha,confirmar_senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.confirmar_senha = confirmar_senha

class Usuario_ativo:

    def __init__(self,id,nome,cpf,email):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def apagar_usuario(self):

        self.id = None
        self.nome = None
        self.cpf = None
        self.email = None