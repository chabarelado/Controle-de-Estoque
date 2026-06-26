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

    def cadastrar_peca(self, nome='', codigo='', quantidade=0):

        if not nome or not codigo or quantidade == 0:
            return False

        if self.repo_peca.buscar_por_codigo(codigo) or self.repo_peca.buscar_por_nome(nome):
            return False
        
        peca_id = self.repo_peca.proximo_id()
        
        nova_peca = Peca(id=peca_id, nome=nome, codigo=codigo, quantidade=quantidade)
        
        self.repo_peca.adicionar(nova_peca.dicionario())

    def registar_entrada(self):
        pass

    def registrar_saida(self):
        pass 
    
    def cancelar_movimento(self):
        pass

    def pesquisar_peca(self):
        pass 
    
    