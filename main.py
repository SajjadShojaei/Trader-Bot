import schedule
import time
from tradingview_ta import TA_Handler, Exchange, Interval
import matplotlib.pyplot as plt

plt.ion()  # Turn on interactive mode

rsi_values = []  # List of RSI values
timestamps = []  # List of timestamps

fig, ax = plt.subplots()

def printRSI():
    handler = TA_Handler(
    symbol='BTCUSDT',
    screener='crypto',
    exchange='binance',
    interval=Interval.INTERVAL_1_MINUTE
    )
    analysis = handler.get_analysis()
    rsi = analysis.indicators['RSI[1]']
    moving_average= analysis.indicators    
    if rsi < 30 :
        print (rsi , 'Buy')
    elif rsi > 60 :
        print ( rsi , 'Sell') 
    else : print(rsi , "Not signal")       

    rsi_values.append(rsi)  # Append RSI value to the list
    timestamps.append(time.time())  # Append current time to the list

    # Plot the chart
    ax.clear()  # Clear the previous chart
    ax.plot(timestamps, rsi_values, label='RSI')
    ax.set_xlabel('TIME')
    ax.set_ylabel('Volume RSI')
    ax.set_title('Chart RSI')
    ax.legend()
    plt.pause(0.01)  # Pause to update the chart

# Schedule the task to run every 5 seconds
schedule.every(5).seconds.do(printRSI)

while True:
    schedule.run_pending()
    time.sleep(1)

# # Import packages.
# from tradingview_ta import TA_Handler, Interval, Exchange
# import time

# # Store the last order.
# last_order = "sell"

# # Instantiate TA_Handler.
# handler = TA_Handler(
#     symbol="SYMBOL",
#     exchange="EXCHANGE",
#     screener="SCREENER",
#     interval="INTERVAL",
# )

# # Repeat forever.
# while True:
#     # Retrieve recommendation.
#     rec = handler.get_analysis()["RECOMMENDATION"]

#     # Create a buy order if the recommendation is "BUY" or "STRONG_BUY" and the last order is "sell".
#     # Create a sell order if the recommendation is "SELL" or "STRONG_SELL" and the last order is "buy".
#     if "BUY" in rec and last_order == "sell":
#         # REPLACE COMMENT: Create a buy order using your exchange's API.

#         last_order = "buy"
#     elif "SELL" in rec and last_order == "buy":
#         # REPLACE COMMENT: Create a sell order using your exchange's API.

#         last_order = "sell"

#     # Wait for x seconds before retrieving new analysis.
#     # The time should be the same as the interval.
#     time.sleep(x)    

