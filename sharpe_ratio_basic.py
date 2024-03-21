import numpy as np

# Example PnL data for an intraday trading strategy
pnl_per_trade = np.array([0.002, -0.005, 0.003, 0.004, -0.002, 0.001, -0.005, 0.002, -0.004, 0.006])

# Number of trades (N)
num_trades = len(pnl_per_trade)

# Calculate Sharpe Ratio components
mean_pnl = np.mean(pnl_per_trade)
std_dev_pnl = np.std(pnl_per_trade, ddof=1)  
# ddof=1 for sample standard deviation

# Calculate Sharpe Ratio
sharpe_ratio = np.sqrt(num_trades) * (mean_pnl / std_dev_pnl)

print(f"Mean of PnL: {mean_pnl}")
print(f"Standard Deviation of PnL: {std_dev_pnl}")
print(f"Sharpe Ratio: {sharpe_ratio}")