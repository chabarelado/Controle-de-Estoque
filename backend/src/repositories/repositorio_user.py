from api.api_user import Api

class RepositorioUser:
    def __init__(self):
        self.api = Api()

    def buscar_por_login(self, login, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False
            dados = self.api.dados

        for user in dados["usuarios"]:
            if str(user["login"]).lower() == str(login).lower():
                return user
        
        return None

    def buscar_por_id(self, id, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False
            dados = self.api.dados

        for user in dados["usuarios"]:
            if int(user["id"]) == int(id):
                return user
            
        return None
        
    
    def proximo_id(self, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False
            dados = self.api.dados

        users = dados["usuarios"]

        if not users:
            return 1
        
        return max(user["id"] for user in users) + 1

    def remover(self, id, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False
            dados = self.api.dados

        verifica_user_existent = self.buscar_por_id(id, dados)

        if not verifica_user_existent:
            return False
        
        dados["usuarios"].remove(verifica_user_existent)
        return self.api.salvar_json()
 

    def adicionar(self, novo_usuario, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False
            dados = self.api.dados

        if self.buscar_por_id(novo_usuario["id"], dados):
            return False
        
        if self.buscar_por_login(novo_usuario["login"], dados):
            return False
        
        dados["usuarios"].append(novo_usuario)
        return self.api.salvar_json()

    def atualizar(self, id, novos_dados, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False
            dados = self.api.dados

        verificar_user = self.buscar_por_id(id, dados)

        if not verificar_user:
            return False
        
        verificar_user.update(novos_dados)
        return self.api.salvar_json()


    def listar(self, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return []
            dados = self.api.dados

        return dados["usuarios"]