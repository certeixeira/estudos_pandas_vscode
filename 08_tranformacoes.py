# %%

import pandas as pd
import numpy as np
# %%

df = pd.read_csv('data/produto.csv')
# %%
df.head()
# %%
df
# %%
df.info()
# %%

# aumentando todos os valores em 9%:
df['precoAjustado'] = df['vlPreco'] * 1.09
df['precoAjustado'] = df['precoAjustado'].round(2)
df
# %%

# ou:
df['precoAjustado'] = (df['vlPreco'] * 1.09).round(2)
df
# %%

# verificando o ajuste de preço:
df['txAjuste(%)'] = (100 * (df['precoAjustado'] / df['vlPreco'] - 1)).round(2)
df
# %%

df = df.drop(columns=['txAjuste'])
df
# %%

df['txAjuste(%)']
# %%

np.log([2.14, 10, 1.03])
# %%

df['logTxAjuste'] = np.log(df['txAjuste(%)'])
df

# %%

df['expTxAjuste'] = np.exp(df['txAjuste(%)'])
df
# %%

def fatorial(x):
    total = 1
    for i in range(2, int(x) + 1):
        total *= i
    return total
# %%

fatorial(2)
# %%
fatorial(3)
# %%
fatorial(5)
# %%

# como aplicar a função fatorial em um dataset?
df['precoAjustado'].apply(fatorial)
# %%
