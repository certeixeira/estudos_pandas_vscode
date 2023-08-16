# %%
import pandas as pd
import numpy as np

# aumentando a quantidade de linhas para visualizar
pd.set_option('display.max_rows', 500)
# %%

df_produto = pd.read_csv('data/produto.csv')
df_produto
# %%

# ordenando do menor para o maior
df_produto.sort_values(by='vlPreco')
# %%

# ordenando do maior para o menor
df_produto.sort_values(by='vlPreco', ascending=False)
# %%

# ordenando por um segundo critério
df_produto.sort_values(by=['vlPreco', 'descItem'], ascending=False)
# %%
# ordenando por um segundo critério
df_produto.sort_values(by=['vlPreco', 'descItem'], ascending=[False, True])
# %%
