from repositories.repositorio_movimento import RepositorioMovimentacao
from repositories.repositorio_peca import RepositorioPecas
from repositories.repositorio_destinatario import RepositorioDestinatario

from models.pecas import Peca
from models.destinatario import Destinatario
from models.movimento import Movimentacao

class Service:
    def __init__(self):
        self.repo_movi = RepositorioMovimentacao()
        self.repo_peca = RepositorioPecas()
        self.repo_unid = RepositorioDestinatario()

        self.peca = Peca()
        self.unidade = Destinatario()
        self.movimento = Movimentacao()
        

    def registar_entrada(self):
        pass

    def registrar_saida(self):
        pass 
    
    def cancelar_movimento(self):
        pass

    def pesquisar_peca(self):
        pass 
    
    