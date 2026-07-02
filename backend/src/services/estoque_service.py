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
            return (False, "Preencha o nome corretamente.")

        if not codigo.strip():
            return (False, "Preencha o codigo corretamente.")

        if quantidade <= 0:
            return (False, "Adicione um valor válido.") 

        if self.repo_peca.buscar_por_codigo(codigo) or self.repo_peca.buscar_por_nome(nome):
            return (False, "Já existe uma peça com essas informações")
        
        peca_id = self.repo_peca.proximo_id()
        
        nova_peca = Peca(peca_id=peca_id, nome=nome, codigo=codigo, quantidade=quantidade)
        
        return self.repo_peca.adicionar(nova_peca.dicionario())

    def remover_peca(self, termo):
        pesquisa = self.pesquisar_peca(termo)
        
        if len(pesquisa) == 0:
            return (False, "Peça não encontrada.")

        if len(pesquisa) > 1:
            return (False, "Mais de uma peça encontrada.")

        peca = pesquisa[0]

        movimentos = self.repo_movi.buscar_por_peca(peca["id"])
        
        if movimentos:
            return (False, "Esta peça possui movimentações.")

        return self.repo_peca.remover(peca["codigo"])
    
    def editar_peca(self, termo, novos_dados):
        pesquisa = self.pesquisar_peca(termo)
        
        if len(pesquisa) == 0:
            return (False, "Peça não encontrada.")

        if len(pesquisa) > 1:
            return (False, "Mais de uma peça encontrada.")

        peca = pesquisa[0]
        
        if "codigo" in novos_dados:
            existente = self.repo_peca.buscar_por_codigo(novos_dados["codigo"])

            if existente and existente["id"] != peca["id"]:
                return (False, "Código já cadastrado.")
        
        if "nome" in novos_dados:
            existente = self.repo_peca.buscar_por_nome(novos_dados["nome"])

            if existente and existente["id"] != peca["id"]:
                return (False, "Nome já cadastrado.")

        atualiza = self.repo_peca.atualizar(peca["codigo"], novos_dados)

        if not atualiza:
            return (False, "Não foi possível ao atuailizar.")
        
        return (True, "Atualizado com sucesso.")
#===================================================================================================================
    
    def cadastrar_unidade(self, nome, endereco):
        if not nome.strip():
            return (False, "Preencha o nome corretamente.") 

        if not endereco.strip():
            return (False, "Preencha o endereço corretamente.")
        
        if self.repo_unid.buscar_por_nome(nome):
            return (False, "Já existe uma unidade cadastrada com esse nome.")
        
        proximo_id = self.repo_unid.proximo_id()
        nova_unidade = Destinatario(id= proximo_id, nome=nome, endereco=endereco)

        return self.repo_unid.adicionar(nova_unidade.dicionario())
    
    def remover_unidade(self, termo):
        pesquisa = self.pesquisar_unidade(termo)
        
        if len(pesquisa) == 0:
            return (False, "Unidade não encontrada.")

        if len(pesquisa) > 1:
            return (False, "Mais de uma unidade encontrada.")

        unidade = pesquisa[0]

        movimentos = self.repo_movi.buscar_por_destinatario(unidade["id"])

        if movimentos:
            return (False, "Esta unidade possui movimentações")
        
        return self.repo_unid.remover(unidade["id"])

    def editar_unidade(self, termo, novos_dados):
        pesquisa = self.pesquisar_unidade(termo)
        
        if len(pesquisa) == 0:
            return (False, "Unidade não encontrada.")

        if len(pesquisa) > 1:
            return (False, "Mais de uma unidade encontrada.")

        unidade = pesquisa[0]

        if not unidade:
            return (False, "Unidade não encontrada.")
        
        if "nome" in novos_dados:
            existente = self.repo_unid.buscar_por_nome(novos_dados["nome"])

            if existente and existente["nome"] != unidade["nome"]:
                return (False, "Nome já cadastrado.")
        
        if "id" in novos_dados:
            existente = self.repo_unid.buscar_por_id(novos_dados["id"])

            if existente and existente["id"] != unidade["id"]:
                return (False, "ID já cadastrado.")
        
        atualiza = self.repo_unid.atualizar(unidade["id"], novos_dados)

        if not atualiza:
            return (False, "Não foi possível atualizar")
        
        return (True, "Atualizado com sucesso.")

#===================================================================================================================

    def registrar_movimento(self, peca_id, unidade_id, quantidade):

        if quantidade <= 0:
            return (False, "Quantidade inválida.")

        peca = self.repo_peca.buscar_por_id(peca_id)
        unidade = self.repo_unid.buscar_por_id(unidade_id)

        if not peca:
            return (False, "Peça não encontrada.")
        
        if not unidade:
            return (False, "Unidade não encontrada.")
        
        if peca["quantidade"] < quantidade:
            return (False, "Estoque insuficiente.")
        
        nova_quantidade = peca["quantidade"] - quantidade
        movimento = Movimentacao(peca_id=peca_id, destinatario_id=unidade_id, quantidade=quantidade, ativo=True)
        
        if not self.repo_peca.atualizar(peca["codigo"], {"quantidade":nova_quantidade}):
            return (False, "Não foi possível atualizar o estoque.")

        if not self.repo_movi.adicionar(movimento.dicionario()):
            self.repo_peca.atualizar(peca["codigo"], {"quantidade": peca["quantidade"]})
            return (False, "Não foi possivel registrar.")
        
        return (True, "Movimento registrado com sucesso!")
    

    def cancelar_movimento(self, movimento_id ):

        movimento = self.repo_movi.buscar_por_id(movimento_id)

        if not movimento:
            return (False, "Movimento não encontrado.")
        
        if not movimento["ativo"]:
            return (False, "Movimento ja esta cancelado.")
        
        peca = self.repo_peca.buscar_por_id(movimento["peca_id"])

        if not peca:
            return (False, "Peca não encontrada.")
        
        estoque_original = peca["quantidade"]
        atualiza_quantidade = peca["quantidade"] + movimento["quantidade"]

        if not self.repo_peca.atualizar(peca["codigo"], {"quantidade":atualiza_quantidade}):
            return (False, "Erro ao atualizar estoque.")

        if not self.repo_movi.cancelar_movimento(movimento_id):
            self.repo_peca.atualizar(peca["codigo"],{"quantidade": estoque_original})
            return (False, "Erro ao cancelar movimento.")
        
        return (True, "Movimentação cancelada com sucesso.")

    
#===================================================================================================================

    def pesquisar_peca(self, termo):
        return self.repo_peca.pesquisar(termo)

    def pesquisar_unidade(self, termo):
        return self.repo_unid.pesquisar(termo)

    def pesquisar_movimento(self,termo):
        return self.repo_movi.pesquisar(termo)

#===================================================================================================================

    def listar_pecas(self):
        return self.repo_peca.listar()

    def listar_unidades(self):
        return self.repo_unid.listar()

    def lista_movimentos_ativos(self):
        movimentos = self.listar_todos_movimentos()
        movimentos_ativos = []

        for movi in movimentos:
            if movi["ativo"]:
                movimentos_ativos.append(movi)

        return movimentos_ativos
    
    def lista_movimentos_cancelados(self):
        movimentos = self.listar_todos_movimentos()
        movimentos_cancelados = []

        for movi in movimentos:
            if not movi["ativo"]:
                movimentos_cancelados.append(movi)

        return movimentos_cancelados

    def listar_todos_movimentos(self):
        return self.repo_movi.listar()
