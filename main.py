from utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total
)

# Categorias
cadastrar_receitas = cadastrar_categoria('receitas')
categoraia_contas = cadastrar_categoria('Contas Fixas')
categoria_laser = cadastrar_categoria('Laser')
categoria_viagens = cadastrar_categoria('Viagens')

# Transações
cadastrar_transacao(
    descricao = 'Salário Jan/2025',
    valor = 1000.0,
    categoria = cadastrar_receitas
)

cadastrar_transacao(
    descricao = 'Mesada Mamãe',
    valor = 50.0,
    categoria = cadastrar_receitas
)

cadastrar_transacao(
    descricao = 'Ingresso Show',
    valor = -150.0,
    categoria = categoria_laser 
)

cadastrar_transacao(
    descricao = 'Conta de Luz',
    valor = -100.0,
    categoria = categoraia_contas
)

cadastrar_transacao(
    descricao = 'Disney',
    valor = -400.0,
    categoria = categoria_viagens
)

total = saldo_total()

print('Saldo Total: ', total)