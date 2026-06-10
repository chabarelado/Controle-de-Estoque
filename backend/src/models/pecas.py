class Peca: 
    def __init__(self, peca_id, nome, quantidade, codigo): 
        self.peca_id = peca_id 
        self.codigo = codigo 
        self.nome = nome 
        self.quantidade = quantidade
    
    def dicionario(self):
        return {
            "id": self.peca_id,
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade
        }