# %%

import pandas as pd
# %%
df = pd.read_csv('data/pedido.csv')
# %%
df
# %%

idade = [20, 18, 30, 67, 54, 19, 24]
# %%

idade_20 = []
for i in idade:
    if i > 20:
        idade_20.append(i)
        
idade_20
# %%

idade_25 =[i for i in idade if i > 25]

idade_25
# %%

# transformando a lista em serie:
idade = pd.Series([20, 18, 30, 67, 54, 19, 24])

filtro = idade >= 20
# %%

idade[filtro]
# %%

df.head()
# %%

filtro_uf = df['descUF'] == 'São Paulo'

# %%

df[filtro_uf]
# %%

# é de sp e pediu ketchup
filtro_sp_ketchup = (df['descUF'] == 'São Paulo') & (df['flKetchup'])
df[filtro_sp_ketchup]
# %%

filtros_ufs_ketchup = (df['descUF'] == 'São Paulo') | (df['descUF'] == 'Rio de Janeiro') | (df['descUF'] == 'Paraná')
df[filtros_ufs_ketchup]
# %%

# verifica os valores únicos dessa série, no caso a coluna descUF
df[filtros_ufs_ketchup]['descUF'].unique()
# %%

# adicionando o ketchup ao filtro:
# maneira 1
filtros_ufs_ketchup = ((df['descUF'] == 'São Paulo') | (df['descUF'] == 'Rio de Janeiro') | (df['descUF'] == 'Paraná')) & (df['flKetchup'])
df[filtros_ufs_ketchup]
# %%

df[filtros_ufs_ketchup]['flKetchup'].unique()
# %%

# maneira 2 isin (série):
uf_recortes = ['São Paulo', 'Rio de Janeiro', 'Paraná']
filtro_ufs_ketchup = df['descUF'].isin(uf_recortes) & (df['flKetchup'])
df[filtro_ufs_ketchup]

# %%

df['txtRecado'].isna()
# %%

filtro_txt_na = df['txtRecado'].isna()
df[filtro_txt_na]
# %%
