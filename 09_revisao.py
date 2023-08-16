# %%

import pandas as pd
import numpy as np
# %%

df = pd.read_csv('data/produto.csv')
df
# %%

# renomeando coluna
df = df.rename(columns={'vlPreco': 'vlPrecoReal'})
df
# %%

# uma das formas de filtrar dados na coluna
filtro = df['vlPrecoReal'] > 10
df[filtro]
# %%

# filtrando valores específicos
queijos_premium = ['queijo brie', 'queijo coalho', 'ricota']
filtro_queijo = df['descItem'].isin(queijos_premium)
df[filtro_queijo]
# %%

df['vlPrecoInflacao'] = (df['vlPrecoReal'] * 1.09).round(2)
df
# %%

# aplicando uma função do numpy
df['vlPrecoInflacaoLog'] = np.log(df['vlPrecoInflacao'])
df
# %%

# aplicando uma função usando o apply
# é necessário que a função receba apenas um valor
