import schedule
import time
from tradingview_ta import TA_Handler, Exchange, Interval
import matplotlib.pyplot as plt

plt.ion()  # Turn on interactive mode

# Lists to store data
open_prices = []
close_prices = []
timestamps = []

fig, ax = plt.subplots()


def printCandle():
    handler = TA_Handler(
        symbol='BTCUSDT',
        screener='crypto',
        exchange='binance',
        interval=Interval.INTERVAL_1_MINUTE
    )
    analysis = handler.get_analysis()
    open_price = analysis.indicators['open']
    close_price = analysis.indicators['close']

    open_prices.append(open_price)  # Append open price to the list
    close_prices.append(close_price)  # Append close price to the list
    timestamps.append(time.time())  # Append current time to the list

    # Plot the chart
    ax.clear()  # Clear the previous chart
    ax.plot(timestamps, close_prices, label='Close Price', color='black')  # Plot close prices
    for i in range(len(close_prices)):
        color = 'green' if close_prices[i] > open_prices[i] else 'red'  # Set color based on close and open prices
        ax.bar(timestamps[i], close_prices[i]-open_prices[i], 0.0001, bottom=open_prices[i], color=color)  # Plot candlesticks
    ax.set_xlabel('TIME')
    ax.set_ylabel('Price')
    ax.set_title('Candlestick Chart')
    ax.legend()
    plt.pause(0.01)  # Pause to update the chart


# Schedule the task to run every 5 seconds
schedule.every(5).seconds.do(printCandle)

while True:
    schedule.run_pending()
    time.sleep(1)