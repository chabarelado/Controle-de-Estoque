from api.api_user import Api

class Repositorio_User:
    def __init__(self):
        self.api = Api()

    def buscar_por_login(self, login, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False
            dados = self.api.dados

        for user in dados["login"]:
            if str(user["login"]).lower() == str(login).lower():
                return user
        
        return None

    def buscar_por_id(self, id, dados=None):
        if dados is None:
            if not self.api.ler_json():
                return False
            dados = self.api.dados

        for user in dados["id"]:
            if int(user["id"]) == int(id):
                return user
        
        return None
    
    def proximo_id(self):
        pass
    