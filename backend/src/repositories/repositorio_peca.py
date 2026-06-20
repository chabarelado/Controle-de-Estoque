from api.api import Api
class RepositorioPecas:
    def __init__(self):
        self.api = Api()

    def listar(self):
        if not self.api.ler_json():
            return []
        
        return self.api.dados["pecas"]

    def adicionar(self, nova_peca):
        if not self.api.ler_json():
            return False
    
        dados = self.api.dados
        verifica_peca_existente = self.buscar_por_codigo(nova_peca["codigo"], dados)

        if verifica_peca_existente:
            if verifica_peca_existente["nome"] != nova_peca["nome"]:
                    return False
            verifica_peca_existente["quantidade"] += nova_peca["quantidade"]
        else:
            dados["pecas"].append(nova_peca)

        return self.api.salvar_json()
    

    def remover(self, codigo):
        if not self.api.ler_json():
            return False
        
        dados = self.api.dados
        verifica_peca_existente = self.buscar_por_codigo(codigo, dados)

        if not verifica_peca_existente:
            return False
        
        dados["pecas"].remove(verifica_peca_existente)
        return self.api.salvar_json()


        """if verifica_peca_existente:
            for peca in dados["pecas"]:
                if peca["codigo"] == codigo:
                    dados["pecas"].remove(peca)
                    self.api.salvar_json()
                    return True
        """

    def atualizar(self, codigo, novos_dados):
        if not self.api.ler_json():
            return False
        
        dados = self.api.dados
        verifica_peca_existente = self.buscar_por_codigo(codigo,dados)

        if not verifica_peca_existente:
            return False

        verifica_peca_existente.update(novos_dados)
        return self.api.salvar_json()
    
        """if verifica_peca_existente:
            for peca in dados["pecas"]:
                if peca["codigo"] == codigo:
                    peca.update(novos_dados)
                    self.api.salvar_json()
                    return True
        """
                
    def buscar_por_codigo(self, codigo,dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None
            dados = self.api.dados

        for peca in dados["pecas"]:
            if peca["codigo"] == codigo:
                return peca
    
        return None
    
    def buscar_por_id(self, id, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None

            dados = self.api.dados

        for peca in dados["pecas"]:
            if peca["id"] == id:
                return peca

        return None

    def buscar_por_nome(self, nome, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None
            dados = self.api.dados
        
        for peca in dados["pecas"]:
            if peca["nome"].lower() == nome.lower():
                return peca
            
        return None

    def pesquisar(self, termo, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return []
            dados = self.api.dados
        
        resultado_da_busca = []

        for peca in dados["pecas"]:
            if (termo.lower() in peca["codigo"].lower() 
                or termo.lower() in peca["nome"].lower() or str(termo) == str(peca["id"])):
                resultado_da_busca.append(peca)

        return resultado_da_busca        