# %%

import pandas as pd
# %%

idade = pd.Series([10, 20, 30, 40, 50, 60, 70 ])
idade.describe()
# %%

df = pd.DataFrame({
    "nome":["teo", "leo", "jao"],
    "idade":[30, 48, 15]
})

df
# %%

df_pedido = pd.read_csv("data/pedido.csv")
df_pedido
# %%

df_pedido.tail()
# %%

df.head(10)
# %%

# linhas aleatórias
df_pedido.sample(3)
# %%

df_pedido[['descUF', 'txtRecado']]
# %%

# buscar linha associada a posição
df_pedido.iloc[890:900]
# %%

# loc é baseado no índice
df_pedido.loc[900]
# %%
