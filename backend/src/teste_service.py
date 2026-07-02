from services.estoque_service import EstoqueService

service = EstoqueService()

print("=" * 60)
print("CADASTRANDO PEÇA")
print("=" * 60)

resultado = service.cadastrar_peca(
    nome="Mouse Gamer",
    codigo="MOU001",
    quantidade=10
)
print(resultado)


print("\n" + "=" * 60)
print("CADASTRANDO UNIDADE")
print("=" * 60)

resultado = service.cadastrar_unidade(
    nome="TI",
    endereco="Rua Principal, 100"
)
print(resultado)


print("\n" + "=" * 60)
print("LISTANDO PEÇAS")
print("=" * 60)

for peca in service.listar_pecas():
    print(peca)


print("\n" + "=" * 60)
print("LISTANDO UNIDADES")
print("=" * 60)

for unidade in service.listar_unidades():
    print(unidade)


print("\n" + "=" * 60)
print("PESQUISANDO PEÇA")
print("=" * 60)

print(service.pesquisar_peca("Mouse"))
print(service.pesquisar_peca("MOU001"))


print("\n" + "=" * 60)
print("REGISTRANDO MOVIMENTO")
print("=" * 60)

resultado = service.registrar_movimento(
    peca_id=1,
    unidade_id=1,
    quantidade=2
)

print(resultado)


print("\n" + "=" * 60)
print("MOVIMENTOS")
print("=" * 60)

for movimento in service.listar_todos_movimentos():
    print(movimento)


print("\n" + "=" * 60)
print("MOVIMENTOS ATIVOS")
print("=" * 60)

for movimento in service.lista_movimentos_ativos():
    print(movimento)


print("\n" + "=" * 60)
print("CANCELANDO MOVIMENTO")
print("=" * 60)

resultado = service.cancelar_movimento(23)
print(resultado)


print("\n" + "=" * 60)
print("MOVIMENTOS CANCELADOS")
print("=" * 60)

for movimento in service.lista_movimentos_cancelados():
    print(movimento)


print("\n" + "=" * 60)
print("EDITANDO PEÇA")
print("=" * 60)

resultado = service.editar_peca(
    "MOU001",
    {
        "nome": "Mouse Logitech",
        "codigo": "MOU999"
    }
)

print(resultado)


print("\n" + "=" * 60)
print("EDITANDO UNIDADE")
print("=" * 60)

resultado = service.editar_unidade(
    "TI",
    {
        "nome": "Tecnologia da Informação"
    }
)

print(resultado)


print("\n" + "=" * 60)
print("REMOVENDO PEÇA")
print("=" * 60)

resultado = service.remover_peca("MOU999")
print(resultado)


print("\n" + "=" * 60)
print("REMOVENDO UNIDADE")
print("=" * 60)

resultado = service.remover_unidade("Tecnologia")
print(resultado)


print("\n" + "=" * 60)
print("ESTADO FINAL")
print("=" * 60)

print("Peças:")
for peca in service.listar_pecas():
    print(peca)

print("\nUnidades:")
for unidade in service.listar_unidades():
    print(unidade)

print("\nMovimentos:")
for movimento in service.listar_todos_movimentos():
    print(movimento)