# %%
import pandas as pd
# %%

df = pd.read_csv('data/produto.csv')
df
# %%

df['descItemPrimeiroNome'] = df['descItem'].apply(lambda x: x.lower().split(' ')[0])
df
# %%

df.sort_values(by=['vlPreco', 'descItem'], ascending=[False, True])
# %%

df.drop_duplicates(subset=['descItemPrimeiroNome'], keep='first')
# %%

df.groupby(['descItemPrimeiroNome']).count()
# %%

df.groupby(['descItemPrimeiroNome']).agg({'vlPreco':['mean', 'count']}).round(2)
# %%
