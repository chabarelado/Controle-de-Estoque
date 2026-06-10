
class Destinatario:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "endereço": self.endereco
        }