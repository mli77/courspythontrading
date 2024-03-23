import numpy as np

# Exemple de gains en % pour chaque trade d'une stratégie de trading
pnl_des_trades = np.array([0.001, -0.015, 0.002, 0.001, -0.003, 0.005, -0.007, 0.001, -0.005])

# Calcul de la moyenne
moyenne = np.mean(pnl_des_trades)
stddev = np.std(pnl_des_trades, ddof=1)  
"""
 ddof=1 = sample standard deviation
 En Python avec la bibliothèque NumPy, le paramètre ddof signifie 
 "Delta Degrees of Freedom" (degrés de liberté ajustés).
 Il est utilisé pour ajuster le calcul de l'écart-type dans les cas 
 où les données représentent un échantillon plutôt qu'une 
 population entière.

Lorsque ddof est défini sur 0 (la valeur par défaut), 
NumPy calcule l'écart-type de la population. Cela est 
approprié lorsque vous disposez de l'ensemble des données de la population.

Lorsque ddof est défini sur 1, NumPy calcule l'écart-type 
de l'échantillon. Cela est approprié lorsque vous disposez 
d'un échantillon de données de la population et que vous souhaitez 
estimer l'écart-type de l'ensemble de la population sur la base de 
cet échantillon. L'ajustement ddof=1 est utilisé pour fournir une 
estimation non biaisée de l'écart-type de la population, 
en particulier pour les petites tailles d'échantillon.

Par exemple, si vous avez un tableau data contenant des données 
d'échantillon, vous pouvez calculer l'écart-type de l'échantillon 
en utilisant np.std(data, ddof=1). Cela ajustera le calcul pour 
tenir compte du fait que les données sont un échantillon plutôt 
que l'ensemble de la population.
"""

# Nombre de trades (N)
nombre_de_trades = len(pnl_des_trades)

# Calcul du ratio de Sharpe
ratio_de_sharpe = np.sqrt(nombre_de_trades) * (moyenne / stddev)

print(f"Moyenne des PnL: {moyenne}")
print(f"Standard Deviation de les PnL: {stddev}")
print(f"Ratio de Sharpe : {ratio_de_sharpe}")