# %%
import pandas as pd
# %%
df = pd.read_csv("data/pedido.csv")
df
# %%

df.head()
# %%

df[["dtPedido", "flKetchup"]]
# %%

# reorganizando as colunas
colunas = [
    'idPedido',
    'descUF',
    'flKetchup',
    'txtRecado',
    'dtPedido'
]

df[colunas].head()
# %%

# navegando em linhas
# criando um df com 100 dados aleatórios
df_sample = df.sample(100)
df_sample
# %%

# iloc não está relacionado ao indice, e sim a posição
df_sample.iloc[0:4]
# %%

df_sample.iloc[[0,2,5]]
# %%

df_sample.iloc[0:10][['idPedido', 'dtPedido']]
# %%
