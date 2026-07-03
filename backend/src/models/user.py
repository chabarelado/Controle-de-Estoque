class User:
    def __init__(self, id, nome, login, senha, admin=False):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha
        self.admin = admin

    def dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "login": self.login,
            "senha": self.senha_hash,
            "admin": self.admin
        }