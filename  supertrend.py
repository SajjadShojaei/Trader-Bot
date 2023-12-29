import schedule
import time
import pandas as pd
from tradingview_ta import TA_Handler, Exchange, Interval
import pandas_ta as ta
import matplotlib.pyplot as plt

plt.ion()  # Turn on interactive mode

# Fetch market data from the tradingview_ta
def fetch_market_data():
    # Replace with your own code to fetch real market data
    # Simulating market data
    data = {
        'open': [62000, 63000, 64000],
        'high': [62500, 63500, 64500],
        'low': [61500, 62500, 63500],
        'close': [62200, 63200, 64200],
    }
    df = pd.DataFrame(data)
    df['timestamp'] = pd.date_range(start='2021-10-01', periods=len(df), freq='H')
    return df.set_index('timestamp')

# Calculate EMA and Supertrend
def calculate_indicators(dataframe):
    dataframe.ta.ema(length=20, append=True)  # Calculate EMA with length 20
    dataframe.ta.supertrend(append=True)  # Calculate Supertrend
    return dataframe

# Combine the indicators and create buy/sell signals
def create_signals(dataframe):
    # Define your strategy here
    dataframe['buy_signal'] = (dataframe['close'] > dataframe['EMA_20']) & (dataframe['close'] > dataframe['SUPERTd_7_3.0'])
    dataframe['sell_signal'] = (dataframe['close'] < dataframe['EMA_20']) & (dataframe['close'] < dataframe['SUPERTd_7_3.0'])
    return dataframe

# Function to plot the data and signals
def plot_data(dataframe):
    buy_signals = dataframe[dataframe['buy_signal']]
    sell_signals = dataframe[dataframe['sell_signal']]

    plt.figure(figsize=(12,8))
    plt.plot(dataframe.index, dataframe['close'], label='Close Price', color='blue')
    plt.scatter(buy_signals.index, buy_signals['close'], marker='^', color='green', label='Buy Signal')
    plt.scatter(sell_signals.index, sell_signals['close'], marker='v', color='red', label='Sell Signal')
    plt.plot(dataframe.index, color='orange', linestyle='--')
    plt.plot(dataframe.index, color='purple', linestyle='--')
    plt.title('Market Data with Indicators and Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Function to print the chart and data
def print_chart_and_data():
    # Fetch market data
    market_data = fetch_market_data()

    # Calculate indicators
    indicators_data = calculate_indicators(market_data)

    # Create buy/sell signals
    signals_data = create_signals(indicators_data)

    # Plot data and signals
    plot_data(signals_data)

# Schedule to run the printing and plotting function every minute
schedule.every(5).seconds.do(print_chart_and_data)

# Main loop to keep the application running
while True:
    schedule.run_pending()
    time.sleep(1)