from repositories.repositorio_destinatario import RepositorioDestinatario
from models.destinatario import Destinatario

repo = RepositorioDestinatario()

print("=" * 50)
print("LISTANDO DESTINATÁRIOS")
print("=" * 50)
print(repo.listar())

print("\n" + "=" * 50)
print("CRIANDO OBJETO DESTINATÁRIO")
print("=" * 50)

novo_destinatario = Destinatario(
    id=999,
    nome="Unidade de Teste",
    endereco="Endereço de Teste"
)

print(novo_destinatario.dicionario())

print("\n" + "=" * 50)
print("ADICIONANDO DESTINATÁRIO")
print("=" * 50)

resultado = repo.adicionar(novo_destinatario.dicionario())
print("Resultado:", resultado)

print("\n" + "=" * 50)
print("BUSCANDO POR ID")
print("=" * 50)

destinatario = repo.buscar_por_id(999)
print(destinatario)

print("\n" + "=" * 50)
print("BUSCANDO POR NOME")
print("=" * 50)

destinatario = repo.buscar_por_nome("Unidade de Teste")
print(destinatario)

print("\n" + "=" * 50)
print("PESQUISANDO")
print("=" * 50)

resultado_pesquisa = repo.pesquisar("Teste")
print(resultado_pesquisa)

print("\n" + "=" * 50)
print("ATUALIZANDO DESTINATÁRIO")
print("=" * 50)

resultado = repo.atualizar(
    999,
    {
        "nome": "Unidade de Teste Atualizada",
        "endereco": "Novo Endereço"
    }
)

print("Resultado:", resultado)
print(repo.buscar_por_id(999))

print("\n" + "=" * 50)
print("REMOVENDO DESTINATÁRIO")
print("=" * 50)

resultado = repo.remover(999)
print("Resultado:", resultado)

print("\n" + "=" * 50)
print("BUSCANDO APÓS REMOÇÃO")
print("=" * 50)

print(repo.buscar_por_id(999))

print("\n" + "=" * 50)
print("LISTA FINAL")
print("=" * 50)

print(repo.listar())