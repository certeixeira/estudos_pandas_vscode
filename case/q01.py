# Podemos remover algum tipo de massa do cardápio?
# Qual o impacto dessa ação?

# %%
import pandas as pd
# %%

df_item_pedido = pd.read_csv('../data/item_pedido.csv')
df_produto = pd.read_csv('../data/produto.csv')
# %%

# primeiro verificamos os valores únicos
df_item_pedido['descTipoItem'].unique()
# %%

filtro_massa = df_item_pedido['descTipoItem'] == 'massa'

# %%
df_massa = df_item_pedido[filtro_massa]
# %%

df_group = (df_massa.groupby(by=['descItem'])['idPedido']
                    .nunique()
                    .reset_index())
# %%

df_group['Representa(%)'] = ((df_group['idPedido'] / df_group['idPedido'].sum()) * 100).round(2)
df_group
# %%

# mergeando o df_massa com o df_produto
df_massa = df_massa.merge(df_produto, how='left')
df_massa
# %%

df_group = df_massa.groupby(by=['descItem']).agg({"idPedido":['nunique'],
                                                  "vlPreco":['sum']}).reset_index()

df_group['RepQtde(%)'] = ((df_group['idPedido'] / df_group['idPedido'].sum()) * 100).round(2)
df_group['RepReceita(%)'] = ((df_group['vlPreco'] / df_group['vlPreco'].sum()) * 100).round(2)
df_group
# %%
