import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_price = 100  # Initial stock price
drift = 0.05  # Drift parameter (mean rate of return)
volatility = 0.3  # Volatility parameter (standard deviation of returns)
num_minutes = 360  # Number of minutes to simulate

# Generate Wiener process (Brownian motion)
dt = 1 / 60  # Time increment (1 minute)
num_points = int(num_minutes * 60)  # Number of points to simulate
z = np.random.normal(0, np.sqrt(dt), num_points)  # Random samples from normal distribution
increments = drift * dt + volatility * z  # Stock price increments

# Simulate stock prices
prices = np.zeros(num_points)
prices[0] = initial_price
for i in range(1, num_points):
    prices[i] = prices[i - 1] * (1 + increments[i])

# Aggregate prices into 1-minute candlesticks
open_prices = prices.reshape(-1, 60)[:, 0]
high_prices = np.max(prices.reshape(-1, 60), axis=1)
low_prices = np.min(prices.reshape(-1, 60), axis=1)
close_prices = prices.reshape(-1, 60)[:, -1]

# Plot 1-minute candlesticks
# plt.figure(figsize=(24, 6))
# for i in range(len(open_prices)):
#     plt.plot([i, i], [low_prices[i], high_prices[i]], color='black')
#     plt.plot([i, i], [open_prices[i], close_prices[i]], color='red' if close_prices[i] < open_prices[i] else 'green')
# plt.title('Simulated 1-Minute Candlesticks')
# plt.xlabel('Time (minutes)')
# plt.ylabel('Price')
# plt.grid(True)
# plt.show()

# Plot 1-minute candlesticks after the 250th minute
plt.figure(figsize=(12, 6))
for i in range(len(open_prices)):
    if i >= 250:  # Plot only points after the 250th minute
        plt.plot([i, i], [low_prices[i], high_prices[i]], color='black')
        plt.plot([i, i], [open_prices[i], close_prices[i]], color='red' if close_prices[i] < open_prices[i] else 'green')
plt.title('Simulated 1-Minute Candlesticks (After 250th Minute)')
plt.xlabel('Time (minutes)')
plt.ylabel('Price')
plt.grid(True)
plt.show()