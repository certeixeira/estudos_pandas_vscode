# %%

import pandas as pd
# %%

path = "data/pedido.csv"
df = pd.read_csv(path)
df
# %%

# columns é um atributo
df.columns
# %%

df.shape
# %%

df.index
# %%

df.info(memory_usage='deep')
# %%

df.dtypes
# %%
df.head()
# %%
df