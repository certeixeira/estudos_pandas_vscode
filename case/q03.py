# Vários queijos estão estragando pela validade. 
# Quais queijos juntos atendem 90% dos pedidos?

# %%
import pandas as pd
# %%

df_item_pedido = pd.read_csv('../data/item_pedido.csv')
df_item_pedido
# %%

df_item_pedido['descTipoItem'].unique()
# %%
df_item_pedido['descTipoItem'].apply(lambda x: 'queijo' in x.lower())
# %%
filtro_queijo = df_item_pedido['descTipoItem'].isin(['queijo 1', 'queijo 2'])
# %%
df_queijo = df_item_pedido[filtro_queijo]
df_queijo
# %%

df_group = (df_queijo.groupby(['descItem'])['idPedido']
                     .nunique()
                     .reset_index()
                     .sort_values('idPedido', ascending=False)
                     )
df_group = df_group.reset_index()
# %%

# sumcum() soma acumulando os valores da %
df_group['PrepQueijo(%)'] = (100 * df_group['idPedido'] / df_group['idPedido'].sum()).round(2)
df_group['PrepQueijoAcumulado'] = df_group['PrepQueijo(%)'].cumsum()
df_group = df_group.drop('index', axis=1)
df_group
# %%
