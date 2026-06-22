from repositories.repositorio_movimento import RepositorioMovimentacao
from repositories.repositorio_peca import RepositorioPecas
from repositories.repositorio_destinatario import RepositorioDestinatario

class Service:
    def __init__(self):
        self.movimento = RepositorioMovimentacao()
        self.peca = RepositorioPecas()
        self.destinatario = RepositorioDestinatario()

    def registar_entrada(self):
        pass

    def registrar_saida(self):
        pass 
    
    def cancelar_movimento(self):
        pass

    def pesquisar_peca(self):
        pass 
    
    