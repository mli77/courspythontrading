import numpy as np
import matplotlib.pyplot as plt

# Function to simulate trading algorithm
def simulate_trading_algorithm(num_days, good_sharpe=True):
    np.random.seed(0)  # Set random seed for reproducibility
    
    # Simulate daily returns
    if good_sharpe:
        returns = np.random.normal(0.005, 0.02, num_days)  # Good Sharpe: mean return of 0.1% and volatility of 2%
    else:
        returns = np.random.normal(0.001, 0.18, num_days)  # Bad Sharpe: mean return of 0.1% and volatility of 4%
    
    # Calculate cumulative returns
    cumulative_returns = np.cumprod(1 + returns) - 1
    
    # Calculate daily Sharpe Ratio
    sharpe_ratio = np.mean(returns) / np.std(returns)
    
    return cumulative_returns, sharpe_ratio

# Simulate trading algorithm with good Sharpe Ratio
num_days = 252  # 1 year of trading (252 trading days)
good_cumulative_returns, good_sharpe_ratio = simulate_trading_algorithm(num_days, good_sharpe=True)

# Simulate trading algorithm with bad Sharpe Ratio
bad_cumulative_returns, bad_sharpe_ratio = simulate_trading_algorithm(num_days, good_sharpe=False)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(good_cumulative_returns, label=f'Good Sharpe Ratio ({good_sharpe_ratio:.2f})')
plt.plot(bad_cumulative_returns, label=f'Bad Sharpe Ratio ({bad_sharpe_ratio:.2f})')
plt.title('Performance of Trading Algorithm')
plt.xlabel('Trading Days')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.show()
