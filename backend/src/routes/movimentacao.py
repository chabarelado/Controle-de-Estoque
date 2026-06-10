from datetime import datetime

class Movimentacao:
    def __init__(self, peca_id, destinatario_id, data, quantidade):
        self.id_movimento = None
        self.peca_id = peca_id
        self.destinatario_id = destinatario_id
        self.data = data or datetime.now()
        self.quantidade = quantidade
        self.movimentacao.ativo = False

    