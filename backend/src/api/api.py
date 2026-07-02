import json
from pathlib import Path
class Api:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        self.caminho_json = base_dir / "data" / "pecas.json"
        self.dados = None

    def ler_json(self):
        try:
            with open(self.caminho_json, 'r', encoding='utf-8') as arquivo:
                self.dados = json.load(arquivo)
            return True
        except FileNotFoundError:
            print("Arquivo não encontrado!")
            return False
        except json.JSONDecodeError:
            print("Arquivo Json inválido!")
            return False

    def salvar_json(self):
        try:
            with open(self.caminho_json, "w", encoding='utf-8') as arquivo:
                json.dump(self.dados, arquivo, indent=4, ensure_ascii=False)
                return True
        except Exception as erro:
            print(f"Erro ao salvar! {erro}")
            return False
