# %% 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

def get_historical_data(ticker, start_date):
    filename = f"{ticker}.csv"
    try:
        data = pd.read_csv(filename, header=0)
    except:
        # Pull Historical Data
        data = yf.download(ticker, start=start_date)
        # Calculate Daily Returns
        data['Daily Return'] = data['Adj Close'].pct_change()  
        # persist in file
        data.to_csv(filename)
        # reread file in order to get the same format
        data = pd.read_csv(filename, header=0)

    return data.dropna()


def std_dev(data):
    # Get number of observations
    n = len(data)
    # Calculate mean
    mean = sum(data) / n
    # Calculate deviations from the mean
    deviations = sum([(x - mean)**2 for x in data])
    # Calculate Variance & Standard Deviation
    variance = deviations / (n - 1)
    s = variance**(1/2)
    return s

def sharpe_ratio(data, risk_free_rate=0.0):
    # Calculate Average Daily Return
    mean_daily_return = sum(data) / len(data)
    # Calculate Standard Deviation
    s = std_dev(data)
    # Calculate Daily Sharpe Ratio
    daily_sharpe_ratio = (mean_daily_return - risk_free_rate) / s
    # Annualize Daily Sharpe Ratio
    sharpe_ratio = 252**(1/2) * daily_sharpe_ratio
    
    return sharpe_ratio

plt.style.use('ggplot')
data = get_historical_data('MSFT', '2023-01-01')


# Select 'Date' and 'Close' columns
data = data[['Date', 'Close']]

# Convert 'Date' column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Plot 'Date' vs 'Close'
# %% 
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], marker='o', linestyle='-')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

sns.lineplot(x=data.index, y=data['Close'], label='Close')
plt.show()

print("Terminé")
