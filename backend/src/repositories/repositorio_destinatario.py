from api.api import Api

class RepositorioDestinatario:
    def __init__(self):
        self.api = Api()

    def adicionar(self, novo_destinatario):
        if not self.api.ler_json():
            return False

        dados = self.api.dados
        
        if self.buscar_por_id(novo_destinatario["id"], dados):
            return False
        
        if self.buscar_por_nome(novo_destinatario["nome"], dados):
            return False

        dados["unidades"].append(novo_destinatario)
        return self.api.salvar_json()
    

    def remover(self, id):
        if not self.api.ler_json():
            return False

        dados = self.api.dados
        verifica_dest_existente = self.buscar_por_id(id, dados)

        if not verifica_dest_existente:
            return False


        dados["unidades"].remove(verifica_dest_existente)
        self.api.salvar_json()

        return True
    
        """    
        if verifica_dest_existente:
            for destinatario in dados["unidades"]:
                if destinatario["id"] == id:
                    dados["unidades"].remove(destinatario)
                    self.api.salvar_json()
                    return True
        """
     
    def atualizar(self, id, novos_dados):
        if not self.api.ler_json():
            return False

        dados = self.api.dados
        verifica_dest_existente = self.buscar_por_id(id, dados)

        if not verifica_dest_existente:
            return False
        
        verifica_dest_existente.update(novos_dados)

        self.api.salvar_json()
        return True
    
        """if verifica_dest_existente:
            for destinatario in dados["unidades"]:
                if destinatario["id"] == id:
                    destinatario.update(novos_dados)
                    self.api.salvar_json()
                    return True
        """

    def listar(self):
        if not self.api.ler_json():
            return []
        
        return self.api.dados["unidades"]

    def buscar_por_id(self, id, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None
            dados = self.api.dados

        for destinatario in dados["unidades"]:
            if destinatario["id"] == id:
                return destinatario
        
        return None
    
    def buscar_por_nome(self, nome, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return None
            dados = self.api.dados
        
        for destinatario in dados["unidades"]:
            if destinatario["nome"].lower() == nome.lower():
                return destinatario
            
        return None
    
    def pesquisar(self, termo, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return []
            dados = self.api.dados
        
        resultado_da_busca = []

        for destinatario in dados["unidades"]:
            if(termo.lower() in destinatario["nome"].lower() 
               or str(destinatario["id"]) == str(termo) 
               or termo.lower() in destinatario["endereco"].lower()):
                resultado_da_busca.append(destinatario)

        return resultado_da_busca        