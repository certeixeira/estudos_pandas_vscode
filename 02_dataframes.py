# %%

import pandas as pd
# %%

data = {
    "nome":["Ana", "Jao", "Ze", "Pedro", "Alan", "Maria", "InfoSlack"],
    "idade":[30, 28, 16, 18, 45, 60, 40],
    "cor":["Preto", "Verde", "Azul", "Vermelho", "Verde", "Amarelo", "Azul"],
    "renda":[3566, 1345, 0, 6576, 4325, 5326, 10244]
    
}

data
# %%

data['idade']
# %%

df = pd.DataFrame(data)
df
# %%

# cada coluna do DataFrame é uma serie
df['nome']
# %%

type(df["idade"])
# %%

df["idade"].mean()
# %%

df.describe()
# %%

df.mean(numeric_only=True)
# %%
