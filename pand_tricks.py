import pandas as pd
import numpy as np

# Generate sample time series data
np.random.seed(0)
date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
stock_prices = pd.Series(np.random.randint(50, 200, size=len(date_rng)), index=date_rng)
# Downsampling to monthly averages
monthly_averages = stock_prices.resample('M').mean()
print(monthly_averages)


# Generate sample time series data
date_rng_sales = pd.date_range(start='2022-01-01', end='2022-12-31', freq='M')
monthly_sales = pd.Series(np.random.randint(10000, 50000, size=len(date_rng_sales)), index=date_rng_sales)

# Upsampling to daily data with forward fill
daily_sales = monthly_sales.resample('D').ffill()
print(daily_sales)

# Generate sample time series data
np.random.seed(0)
date_rng = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
stock_prices = pd.Series(np.random.randint(50, 200, size=len(date_rng)), index=date_rng)
# Shifting the entire series by one day to calculate daily returns
daily_returns = (stock_prices - stock_prices.shift(1)) / stock_prices.shift(1)
print(daily_returns)


# Generate sample time series data
date_rng_sales = pd.date_range(start='2022-01-01', end='2022-12-31', freq='M')
monthly_sales = pd.Series(np.random.randint(10000, 50000, size=len(date_rng_sales)), index=date_rng_sales)

# Creating a lag feature for the previous month's sales
monthly_sales['Previous_Month_Sales'] = monthly_sales.shift(1)
print(monthly_sales)

# Generate sample time series data
np.random.seed(0)
date_rng = pd.date_range(start='2022-01-01', end='2022-01-31', freq='D')
daily_temperature = pd.Series(np.random.randint(0, 30, size=len(date_rng)), index=date_rng)
# Calculating the 7-day rolling mean
rolling_mean_7d = daily_temperature.rolling(window=7).mean()
print(rolling_mean_7d)

# Generate sample time series data
np.random.seed(0)
date_rng = pd.date_range(start='2022-01-01', end='2022-01-31', freq='D')
daily_temperature = pd.Series(np.random.randint(0, 30, size=len(date_rng)), index=date_rng)
# Calculating the 7-day rolling mean
rolling_mean_7d = daily_temperature.rolling(window=7).mean()
print(rolling_mean_7d)

# Generate sample time series data
np.random.seed(0)
date_rng = pd.date_range(start='2022-01-01', end='2022-01-31', freq='D')
daily_temperature = pd.Series(np.random.randint(0, 30, size=len(date_rng)), index=date_rng)
# Calculating the 7-day rolling mean
rolling_mean_7d = daily_temperature.rolling(window=7).mean()
print(rolling_mean_7d)


# Sample Excel data
excel_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 75000]
})

# Writing Excel data to a file
excel_data.to_excel('sample.xlsx', index=False)
# Reading Excel data into a DataFrame
df_excel = pd.read_excel('sample.xlsx')
print(df_excel)


# Sample CSV data
csv_data = "Name,Age,Salary\nAlice,25,50000\nBob,30,60000\nCharlie,35,75000"
# Reading CSV data into a DataFrame
df = pd.read_csv(pd.compat.StringIO(csv_data))
print(df)


add = lambda x, y: x + y
print(add(3, 5))  # Output: 8


time_series_data = [10, 15, 8, 20, 25, 5, 18]
threshold = 15

filtered_data = list(filter(lambda x: x <= threshold, time_series_data))
print(filtered_data)
# Output: [10, 8, 5]


time_series_data = [1, 2, 3, 4, 5]

squared_data = list(map(lambda x: x**2, time_series_data))
print(squared_data)
# Output: [1, 4, 9, 16, 25]


def safe_divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(f"Error: {e}. Cannot divide by zero.")
        result = None
    else:
        print(f"Result of division: {result}")
    finally:
        print("Division operation completed.")

# Example usage
safe_divide(10, 2)
safe_divide(8, 0)



names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped_data = zip(names, ages)
result = list(zipped_data)
print(result)
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

