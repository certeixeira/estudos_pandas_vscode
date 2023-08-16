# %%
import pandas as pd
# %%

df_produto = pd.read_csv('data/produto.csv')
df_produto
# %%

# verificando os valores distintos
df_produto['descItem'].unique()
# %%

# buscando valores que começam com massa:
def is_massa(x):
    return x.lower().startswith('massa')

# %%

# aplicando a função usando o apply
filtro_massa = df_produto['descItem'].apply(is_massa)
df_produto[filtro_massa]
# %%

# criando uma coluna flagando se é massa
df_produto['flMassa'] = df_produto['descItem'].apply(is_massa)
df_produto
# %%

# pegando os valores True na coluna flMassa:
df_produto[df_produto['flMassa']]
# %%

# criando uma função lambda e usando no apply
filtro_queijo = df_produto['descItem'].apply(lambda x: x.lower().startswith('queijo'))
df_produto[filtro_queijo]
# %%

# outra forma 
df_produto['descItem'].str.lower().str.startswith('massa')
# %%
