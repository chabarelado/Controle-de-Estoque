from repositories.repositorio_peca import RepositorioPecas
from models.pecas import Peca

repo = RepositorioPecas()

print("=" * 50)
print("LISTANDO PEÇAS")
print("=" * 50)
print(repo.listar())

print("\n" + "=" * 50)
print("CRIANDO OBJETO PEÇA")
print("=" * 50)

nova_peca = Peca(
    peca_id=999,
    codigo="TESTE001",
    nome="Peça de Teste",
    quantidade=10
)

print(nova_peca.dicionario())

print("\n" + "=" * 50)
print("ADICIONANDO PEÇA")
print("=" * 50)

resultado = repo.adicionar(nova_peca.dicionario())
print("Resultado:", resultado)

print("\n" + "=" * 50)
print("BUSCANDO POR CÓDIGO")
print("=" * 50)

peca = repo.buscar_por_codigo("TESTE001")
print(peca)

print("\n" + "=" * 50)
print("BUSCANDO POR NOME")
print("=" * 50)

peca = repo.buscar_por_nome("Peça de Teste")
print(peca)

print("\n" + "=" * 50)
print("PESQUISANDO")
print("=" * 50)

resultado_pesquisa = repo.pesquisar("TESTE")
print(resultado_pesquisa)

print("\n" + "=" * 50)
print("ADICIONANDO MESMA PEÇA NOVAMENTE")
print("=" * 50)

repo.adicionar(nova_peca.dicionario())

peca = repo.buscar_por_codigo("TESTE001")
print(peca)

print("\n" + "=" * 50)
print("ATUALIZANDO PEÇA")
print("=" * 50)

resultado = repo.atualizar(
    "TESTE001",
    {
        "nome": "Peça de Teste Atualizada",
        "quantidade": 50
    }
)

print("Resultado:", resultado)
print(repo.buscar_por_codigo("TESTE001"))

print("\n" + "=" * 50)
print("REMOVENDO PEÇA")
print("=" * 50)

resultado = repo.remover("TESTE001")
print("Resultado:", resultado)

print("\n" + "=" * 50)
print("BUSCANDO APÓS REMOÇÃO")
print("=" * 50)

print(repo.buscar_por_codigo("TESTE001"))

print("\n" + "=" * 50)
print("LISTA FINAL")
print("=" * 50)

print(repo.listar())