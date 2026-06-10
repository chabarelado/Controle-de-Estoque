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
        else:
            dados = self.api.dados
            verifica_peca_existente = self.buscar_por_codigo(nova_peca["codigo"], dados)

            if verifica_peca_existente:
                verifica_peca_existente["quantidade"] += nova_peca["quantidade"]
            else:
                dados["pecas"].append(nova_peca)

            self.api.salvar_json()
            return True

    def remover(self, codigo):
        if not self.api.ler_json():
            return False
        
        else:
            dados = self.api.dados
            verifica_peca_existente = self.buscar_por_codigo(codigo, dados)

            if verifica_peca_existente:
                for peca in dados["pecas"]:
                    if peca["codigo"] == codigo:
                        dados["pecas"].remove(peca)
                        self.api.salvar_json()
                        return True
        
        return False

    def atualizar(self, codigo, novos_dados):
        if not self.api.ler_json():
            return False
        else:
            dados = self.api.dados
            verifica_peca_existente = self.buscar_por_codigo(codigo,dados)

            if verifica_peca_existente:
                for peca in dados["pecas"]:
                    if peca["codigo"] == codigo:
                        peca.update(novos_dados)
                        self.api.salvar_json()
                        return True
                    
        return False

    def buscar_por_codigo(self, codigo,dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None
            dados = self.api.dados

        for peca in dados["pecas"]:
            if peca["codigo"] == codigo:
                return peca

        return None