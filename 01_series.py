# %%
import pandas as pd

# %%
idade = [31, 33, 2, 29, 60, 58, 31, 45, 24]
type[idade]

# %%
media = sum(idade) / len(idade)
print(media)

# %%
# pegando a estrutura de séries da idade
s_idade = pd.Series(idade)
s_idade
# %%
# métodos das séries
s_idade.mean()
# %%
# variancia
variancia = s_idade.var
variancia
# %%
# desvio padrão
desvio_padrao = s_idade.std()
desvio_padrao
# %%
# estatística descritiva
s_idade.describe()
# %%

# pegar idade > 30
nova_idade = []

for i in idade:
    if i >= 30:
        nova_idade.append(i)
        
nova_idade
# %%

# pegar idade > 30 com list comprehension
# for é assassino de performance
nova_idade  = [i for i in idade if i >= 30]
nova_idade
# %%

# comparação lógica retorna uma série
filtro = s_idade >= 30
filtro

# %%

# pega os valores verdadeiros dentro da série filtro
s_idade[filtro]
# %%

# lista com valores arbitrários
s_idade[[True, False, True, True, False, False, False, False, True]]
# %%

# usa o ~ para pegar a negativa
filtro = s_idade >= 30
s_idade[~filtro]
# %%
