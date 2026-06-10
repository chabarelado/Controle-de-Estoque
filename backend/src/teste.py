from repositories.repositorio_peca import RepositorioPecas

repo = RepositorioPecas()

nova_peca = {
    "id": 1,
    "codigo": "P001",
    "nome": "Fonte 550W PK PCWELLS",
    "quantidade": 3
}

repo.adicionar(nova_peca)

lista = repo.listar()
for i in lista:
    print(i)

