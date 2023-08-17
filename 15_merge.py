# %%

import pandas as pd

# %%
df_item_pedido = pd.read_csv('data/item_pedido.csv')
df_item_pedido.head(20)
# %%

df_produto = pd.read_csv('data/produto.csv')
df_pedido = pd.read_csv('data/pedido.csv')
# %%

# dando um 'join' no df_item_pedido com o df_produto
df_item_pedido.merge(df_produto, how='left', on='descItem')
# %%

# se os nomes forem diferentes?
df_item_pedido = df_item_pedido.rename(columns={'descItem': 'descProduto'})
# %%

df_item_pedido.merge(right=df_produto, how='left',
                     left_on=['descProduto'],
                     right_on=['descItem'])
# %%

df_item_pedido = df_item_pedido.rename(columns={'descProduto': 'descItem'})

# %%
df_join = df_item_pedido.merge(df_produto, how='left', on='descItem')

# %%

df_join.merge(df_pedido, how='left')
# %%

df_join2 = (df_item_pedido.merge(right=df_produto, how='left')
                          .merge(right=df_pedido, how='left'))

df_join2
# %%
