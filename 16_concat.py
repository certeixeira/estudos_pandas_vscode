# %%
import pandas as pd
# %%

df_mods = pd.DataFrame(
    {
        "nome": ['Sky', 'Maria', 'Joao', 'Vera'],
        "idade": [34, 34, 33, 35]
     }
)
# %%
df_mods
# %%

df_subs = pd.DataFrame(
    {
        'nome': ['Sky', 'Mari', "Bell", 'Maltrapilho', 'Matheus'],
        'idade': [34, 19, 19, 35, 26],
        'meses_subs': [24, 1, 1, 6, 1]
     }
) 

df_subs
# %%

# empilhando os dados dos dois dfs
pd.concat([df_mods, df_subs])
# %%
pd.concat([df_mods, df_subs]).sort_values(['nome', 'meses_subs'])
# %%

# removendo os valores duplicados e preenchendo os NaN com 0
(pd.concat([df_mods, df_subs])
   .sort_values(['nome', 'meses_subs'])
   .drop_duplicates(subset='nome')
   .fillna(0)
)
# %%
