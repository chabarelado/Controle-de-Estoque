from repositories.repositorio_movimento import RepositorioMovimentacao
from repositories.repositorio_peca import RepositorioPecas
from repositories.repositorio_destinatario import RepositorioDestinatario

from models.pecas import Peca
from models.destinatario import Destinatario
from models.movimento import Movimentacao

class EstoqueService:
    def __init__(self):
        self.repo_movi = RepositorioMovimentacao()
        self.repo_peca = RepositorioPecas()
        self.repo_unid = RepositorioDestinatario()

    def cadastrar_peca(self, nome, codigo, quantidade=0):

        if not nome.strip():
            return False

        if not codigo.strip():
            return False

        if quantidade <= 0:
            return False

        if self.repo_peca.buscar_por_codigo(codigo) or self.repo_peca.buscar_por_nome(nome):
            return False
        
        peca_id = self.repo_peca.proximo_id()
        
        nova_peca = Peca(id=peca_id, nome=nome, codigo=codigo, quantidade=quantidade)
        
        return self.repo_peca.adicionar(nova_peca.dicionario())

    def remover_peca(self):
        pass
    
    def editar_peca(self):
        pass

#===================================================================================================================
    
    def cadastrar_unidade(self, nome, endereco):
        if not nome.strip():
            return False

        if not endereco.strip():
            return False
        
        if self.repo_unid.buscar_por_nome(nome):
            return False
        
        proximo_id = self.repo_unid.proximo_id()
        nova_unidade = Destinatario(id= proximo_id, nome=nome, endereco=endereco)

        return self.repo_unid.adicionar(nova_unidade.dicionario())
    
    def remover_unidade(self):
        pass
    
    def editar_unidade(self):
        pass

#===================================================================================================================

    def registrar_movimento(self, peca_id, unidade_id, quantidade):

        if quantidade <= 0:
            return False, "Quantidade inválida."

        peca = self.repo_peca.buscar_por_id(peca_id)
        unidade = self.repo_unid.buscar_por_id(unidade_id)

        if not peca:
            return False, "Peça não encontrada."
        
        if not unidade:
            return False, "Unidade não encontrada."
        
        if peca["quantidade"] < quantidade:
            return False, "Estoque insuficiente."
        
        nova_quantidade = peca["quantidade"] - quantidade
        
        if not self.repo_peca.atualizar(peca["codigo"], {"quantidade":nova_quantidade}):
            return False, "Não foi possível atualizar o estoque."
        
        movimento = Movimentacao(peca_id=peca_id, destinatario_id=unidade_id, quantidade=quantidade, ativo=True)

        if not self.repo_movi.adicionar(movimento.dicionario()):
            self.repo_peca.atualizar(peca["codigo"], {"quantidade": peca["quantidade"]})
            return False, "Não foi possivel registrar."
        
        return True, "Movimento registrado com sucesso!"
    

    def desativar_movimento(self, movimento_id ):

        movimento = self.repo_movi.buscar_por_id(movimento_id)

        if not movimento:
            return False, "Movimento não encontrado."
        
        if not movimento["ativo"]:
            return False, "Moviment ja esta cancelado."
        
        peca = self.repo_peca.buscar_por_id(movimento["peca_id"])

        if not peca:
            return False, "Peca não encontrada."
        
        atualiza_quantidade = peca["quantidade"] + movimento["quantidade"]

        if not self.repo_peca.atualizar(peca["codigo"], {"quantidade":atualiza_quantidade}):
            return False, "Erro ao atualizar estoque."

        if not self.repo_movi.cancelar_movimento(movimento_id):
            return False, "Erro ao cancelar movimento."
        
        return True, "Movimentação cancelada com sucesso."

    
#===================================================================================================================

    def pesquisar_peca(self):
        pass

    def pesquisar_unidade(self):
        pass

    def pesquisar_movimento(self):
        pass

#===================================================================================================================

    def listar_pecas(self):
        pass

    def listar_unidades(self):
        pass

    def lista_movimentos_ativos(self):
        pass

    def listar_movimentos_ativos(self):
        pass

    def listar_todos_movimentos(self):
        pass
