# %%

import pandas as pd

pd.set_option('display.max_rows', 100)
# %%

df_produto = pd.read_csv('data/produto.csv')
df_produto
# %%

# essa função lambda pega o primeiro valor do nome (separado por ' ') e cria uma coluna com a primeira palavra
df_produto['primeiroNome'] = df_produto['descItem'].apply(lambda x: x.lower().split(' ')[0])
df_produto
# %%

df_produto.sort_values(
    by=['vlPreco', 'descItem'],
    ascending=[False, True]
)
# tirando nomes repetidos
# o drop_duplicate remove linhas que sejam iguais, mas usando o subset ele apaga referente a uma coluna
df_produto.drop_duplicates(subset=['primeiroNome'], keep='first')
# %%

df_pedido = pd.read_csv('data/pedido.csv')
df_pedido
# %%

# removendo qualquer linha que contenha NaN na coluna txtRecado
df_pedido.dropna(subset=['txtRecado', 'flKetchup'], how='any')
# %%

