# %% 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

def get_donnees_historiques(code, date_depart):
    filename = f"{code}.csv"
    try:
        data = pd.read_csv(filename, header=0)
    except:
        # On récupère les données de Yahoo Finance
        data = yf.download(code, start=date_depart)
        print(data)
        # On calcule les variations quotidiennes
        data['Daily Return'] = data['Adj Close'].pct_change()  
        print(data)
        # On sauvegarde ces données dans un fichier pour éviter de rappeler Yahoo Finance chaque fois
        data.to_csv(filename)
        # On relit le format (juste pour être sûr de ne pas se tromper dans le format)
        data = pd.read_csv(filename, header=0)

    # on renvoie les données en enlevant celles qui seraient nulles (au cas où)
    return data.dropna()


def std_dev(data):
    # La longueur de la liste data donne le nombre d'observations
    n = len(data)
    # on calcule la moyenne
    moyenne = sum(data) / n
    # On calcule l'écart à la moyenne
    ecart = sum([(x - moyenne)**2 for x in data])
    # On calcule la variance puis l'écart type
    variance = ecart / (n - 1)
    ecart_typr = variance**(1/2)
    return ecart_typr

def ratio_sharpe(data, taux_sans_risque=0.0):
    # Calcul de la variation moyenne
    variation_moyenne_par_jour = sum(data) / len(data)
    # Calculate Standard Deviation
    s = std_dev(data)
    # Calculate Daily Sharpe Ratio
    ratio_sharpe_quotidien = (variation_moyenne_par_jour - taux_sans_risque) / s
    # On annualise (on prend 252 jours de cotation dans l'année)
    ratio_sharpe = 252**(1/2) * ratio_sharpe_quotidien
    
    return ratio_sharpe


# %% 
# Début du programme
plt.style.use('ggplot')
data = get_donnees_historiques('AAPL', '2023-01-01')


# Sélectionne les colonnes 'Date', 'Close' et 'Daily Return'
data = data[['Date', 'Close', 'Daily Return']]
print(data)

# Convertit la colonne 'Date' en type datetime
data['Date'] = pd.to_datetime(data['Date'])

# Affiche les cours
# %% 
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], marker='o', linestyle='-')
plt.title('Prix de clôture / temps')
plt.xlabel('Date')
plt.ylabel('Prix de clôture')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#sns.lineplot(x=data.index, y=data['Close'], label='Close')
#plt.show()
# %% 
print(f"Ratio de Sharpe: {ratio_sharpe(data['Daily Return']): .2f}")

print("Terminé")

# %%
