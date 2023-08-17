# %%
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 100)

# %%
df_produto = pd.read_csv('data/produto.csv')
df_produto
# %%

df_produto['vlPreco'].describe()
# %%

df_produto['vlPrecoInflacao'] = (df_produto['vlPreco'] * 1.09).round(2)
df_produto.describe()
# %%

df_produto['descItem'].describe()
# %%

df_produto['descItemPrimeiro'] = df_produto['descItem'].apply(lambda x: x.lower().split(' ')[0])
df_produto[['descItem', 'descItemPrimeiro']].describe()
# %%

# tabela de frequência de cada um dos valores
frequ_items = pd.value_counts(df_produto['descItemPrimeiro'])
plt.bar(frequ_items.index[:7], frequ_items.values[:7])
plt.grid(True)
plt.title('top 7 produtos')
plt.xlabel('Produto')
plt.ylabel('Frequência')
# %%

# agrupando e pegando a média de preços
df_produto.groupby(by=['descItemPrimeiro']).mean(numeric_only=True)
# %%
df_produto.groupby(by=['descItemPrimeiro']).describe()
# %%

df_produto.groupby(by=['descItemPrimeiro']).agg({'vlPreco':['mean', 'min', 'max', 'median']})
# %%

# adicionando uma nova função no agg:
import random
def random_num(x):
    return random.choice(x.values)

df_produto.groupby(by=['descItemPrimeiro']).agg({'vlPreco':[random_num, 'mean', 'min', 'max', 'median']})

# %%
