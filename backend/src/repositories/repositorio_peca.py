from api.api import Api

class RepositorioPecas:
    def __init__(self):
        self.api = Api()

    def listar(self):
        if not self.api.ler_json():
            return False
        
        return self.api.dados["pecas"]

    def adicionar(self, nova_peca):
        if not self.api.ler_json():
            return False
    
        dados = self.api.dados
        verifica_peca_existente = self.buscar_por_id(nova_peca["codigo"])

        if verifica_peca_existente:
            verifica_peca_existente["quantidade"] += nova_peca["quantidade"]
        else:
            dados["pecas"].append(nova_peca)
        
        self.api.salvar_json()
        return True

    def remover(self):
        pass

    def atualizar(self):
        pass

    def buscar_por_id(self, codigo):
        if not self.api.ler_json():
            return None

        else:
            dado = self.api.dados
            for peca in dado["pecas"]:
                if peca["codigo"] ==  codigo:
                    return peca

        return None