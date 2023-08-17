# Hoje só atendemos em Sp, quais os próximos estados que devemos abrir filiais?

# %% 
import pandas as pd
# %%

df_pedidos = pd.read_csv('../data/pedido.csv')

# %%

df_not_sp = df_pedidos[df_pedidos['descUF']!='São Paulo']

df_not_sp.groupby('descUF')['idPedido'].nunique().reset_index().sort_values('idPedido', ascending=False).head(5)
# %%
