from models.user import User
from repositories.repositorio_user import RepositorioUser


class AutenticacaoService:
    def __init__(self):
        self.repo_user = RepositorioUser
        self.usuario_logado = None

    
    def login(self):
        pass

    def logout(self):
        pass

    def usuario_logado(self):
        pass

    def cadastrar_usuario(self):
        pass

    def atualizar_usuario(self):
        pass

    def _usuario(self):
        pass

    def listar_usuarios(self):
        pass

    def pesquisar_usuario(self):
        pass
