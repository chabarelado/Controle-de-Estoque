from datetime import datetime


class Movimentacao:
    def __init__(self, peca_id, destinatario_id, data, quantidade):
        self.peca_id = peca_id
        self.destinatario_id = destinatario_id
        self.data = data or datetime.now()
        self.quantidade = quantidade

    