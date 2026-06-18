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
            return 1

        return max(movi["id"] for movi in movimentos) + 1

    def listar(self):
        if not self.api.ler_json():
            return []
        
        return self.api.dados["movimentos"]

    def desativar(self, id):
        pass

    def cancelar_movimento(self, id,dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False

            dados = self.api.dados

        verifica_mov = self.buscar_por_id(id, dados)

        if not verifica_mov:
            return False

        dados["movimentos"].remove(verifica_mov)
        self.api.salvar_json()

        return True

    def buscar_por_id(self,id, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None
            dados = self.api.dados
        
        for movimento in dados["movimentos"]:
            if id == movimento["id"]:
                return movimento
        
        return None

    def pesquisar(self, termo,dados=None):
        if dados is None:
            if not self.api.ler_json():
                return []
            dados = self.api.dados

        resultado_da_busca = []

        for movimento in dados["movimentos"]:
            if (
                str(movimento["id"]) == str(termo) 
                or str(movimento["peca_id"]) == str(termo)
                or str(movimento["destinatario_id"]) == str(termo)
                or termo in movimento["data"]
            ):
                resultado_da_busca.append(movimento)

        return resultado_da_busca


    def buscar_por_peca(self,id, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None
            dados = self.api.dados
        
        resultado_da_busca = []

        for peca_id in dados["movimentos"]:
            if peca_id["peca_id"] == id:
                resultado_da_busca.append(peca_id)
            
        return resultado_da_busca
    
    def buscar_por_destinatario(self, id, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None
            dados = self.api.dados
        
        resultado_da_busca = []

        for destinatario_id in dados["movimentos"]:
            if destinatario_id["unidade_id"] == id:
                resultado_da_busca.append(destinatario_id)

        return resultado_da_busca

