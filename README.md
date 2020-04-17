# fundamentalista
Coletor de dados financeiros de empresas listadas na B3

# Dependencies
```
pandas 1.0.3
lxml <- NEED TO BE INSTALLED
```

# Installation
Instalar diretamente pelo PyPI:
```
$ pip install fundamentalista
```

# Running
- Retorna um DataFrame com o Demonstrativo de Resultado do Exercício (DRE) dos períodos disponíveis:
```
from fundamentalista.fundamentalista import findata

tick = "PETR4"
df = findata.dre(tick)

print(df)
```

- Retorna um DataFrame com o Balanço Patrimonial do Ativo dos períodos disponíveis:
```
from fundamentalista.fundamentalista import findata

tick = "PETR4"
df = findata.bpa(tick)

print(df)
```

- Retorna um DataFrame com o Balanço Patrimonial do Passivo dos períodos disponíveis:
```
from fundamentalista.fundamentalista import findata

tick = "PETR4"
df = findata.bpp(tick)

print(df)
```

- Retorna um DataFrame com o Fluxo de Caixa dos períodos disponíveis:
```
from fundamentalista.fundamentalista import findata

tick = "PETR4"
df = findata.fca(tick)

print(df)
```

- Retorna um DataFrame com o Demonstração do Valor Adicionado dos períodos disponíveis:
```
from fundamentalista.fundamentalista import findata

tick = "PETR4"
df = findata.dva(tick)

print(df)
```
