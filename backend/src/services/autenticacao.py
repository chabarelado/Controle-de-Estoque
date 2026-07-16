from models.user import User
from repositories.repositorio_user import RepositorioUser
from util.seguranca import Seguranca

class AutenticacaoService:
    def __init__(self):
        self.repo_user = RepositorioUser
        self.usuario_logado = None

    
    def login(self, login, senha):
        
        usuario = self.repo_user.buscar_por_login(login)

        if not usuario:
            return (False, "Usuário não encontrado")
        
        senha_valida = Seguranca.verificar_senha(senha, usuario["senha"])

        if not senha_valida:
            return (False, "Senha incorreta.")
        
        self.usuario_logado = usuario

        return (True, "Acesso liberado.")

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
