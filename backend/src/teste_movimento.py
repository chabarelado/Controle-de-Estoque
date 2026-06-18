from repositories.repositorio_movimento import RepositorioMovimentacao
from models.movimento import Movimentacao

repo = RepositorioMovimentacao()

print("\n" + "=" * 50)
print("LISTANDO MOVIMENTAÇÕES")
print("=" * 50)
print(repo.listar())

print("\n" + "=" * 50)
print("CRIANDO OBJETO MOVIMENTAÇÃO")
print("=" * 50)

movimento = Movimentacao(
    peca_id=1,
    destinatario_id=5,
    data="18/06/2026",
    quantidade=2
)

print(movimento.dicionario())

print("\n" + "=" * 50)
print("ADICIONANDO MOVIMENTAÇÃO")
print("=" * 50)

resultado = repo.adicionar(movimento.dicionario())
print("Resultado:", resultado)

ultimo_movimento = repo.listar()[-1]
ultimo_id = ultimo_movimento["id"]

print("\n" + "=" * 50)
print("BUSCANDO POR ID")
print("=" * 50)

print(repo.buscar_por_id(ultimo_id))

print("\n" + "=" * 50)
print("BUSCANDO POR PEÇA")
print("=" * 50)

print(repo.buscar_por_peca(1))

print("\n" + "=" * 50)
print("BUSCANDO POR DESTINATÁRIO")
print("=" * 50)

print(repo.buscar_por_destinatario(5))

print("\n" + "=" * 50)
print("PESQUISANDO POR DATA")
print("=" * 50)

print(repo.pesquisar("18/06/2026"))

print("\n" + "=" * 50)
print("DESATIVANDO MOVIMENTAÇÃO")
print("=" * 50)

resultado = repo.desativar(ultimo_id)
print("Resultado:", resultado)

print(repo.buscar_por_id(ultimo_id))

print("\n" + "=" * 50)
print("CANCELANDO MOVIMENTAÇÃO")
print("=" * 50)

resultado = repo.cancelar_movimento(ultimo_id)
print("Resultado:", resultado)

print("\n" + "=" * 50)
print("BUSCANDO APÓS CANCELAMENTO")
print("=" * 50)

print(repo.buscar_por_id(ultimo_id))

print("\n" + "=" * 50)
print("LISTA FINAL")
print("=" * 50)

print(repo.listar())