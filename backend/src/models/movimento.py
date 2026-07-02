from datetime import datetime
class Movimentacao: 
    def __init__(self, peca_id, destinatario_id, quantidade, ativo=False): 
        self.id_movimento = None 
        self.peca_id = peca_id 
        self.destinatario_id = destinatario_id 
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
        self.quantidade = quantidade 
        self.ativo = ativo

    def dicionario(self): 
        return { 
            "id": self.id_movimento, 
            "peca_id": self.peca_id, 
            "unidade_id": self.destinatario_id, 
            "quantidade": self.quantidade, 
            "data": self.data,
            "ativo": self.ativo
        }