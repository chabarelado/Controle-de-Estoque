from api.api import Api
from repositories.repositorio_destinatario import RepositorioDestinatario
from repositories.repositorio_peca import RepositorioPecas

class RepositorioMovimentacao:
    def __init__(self):
        self.api = Api()

    def adicionar(self, novo_movimento):
        if not self.api.ler_json():
            return False
        
        dados = self.api.dados
        novo_movimento["id"] = self.proximo_id(dados)

        try:
            dados["movimentos"].append(novo_movimento)
            return self.api.salvar_json()
        except Exception as e:
            print("Erro ao registrar movimento.")
            return False
    
    def proximo_id(self, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False
            
            dados = self.api.dados

        movimentos = dados["movimentos"]

        if not movimentos:
            return False

        return max(movi["id"] for movi in movimentos) + 1

    def listar(self):
        if not self.api.ler_json():
            return []
        
        return self.api.dados["movimentos"]

    def desativar(self, id):
        pass

    def cancelar_movimento(self, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False

            dados = self.api.dados

        verifica_mov = self.buscar_movimento(id, dados)
        pass

    def buscar_por_id(self,id, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None
            dados = self.api.dados
        
        for movimento in dados["movimentos"]:
            if id == movimento["id"]:
                return movimento
        
        return None

    def buscar_por_peca(self, nome=None, id=None, dados=None):
        pass
    
    def buscar_por_destinatario(self, nome=None, id=None, dados=None):
        pass

