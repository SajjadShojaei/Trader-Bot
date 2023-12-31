import schedule
import time
from tradingview_ta import TA_Handler, Exchange, Interval

def getData():
    handler = TA_Handler(
    symbol='BTCUSDT',
    screener='crypto',
    exchange='binance',
    interval=Interval.INTERVAL_1_MINUTE
    )
    analysis = handler.get_analysis()
    RSI = analysis.indicators['RSI[1]']
    if RSI > 60 :
        print(RSI)
    

# Schedule the task to run every 5 seconds
schedule.every(5).seconds.do(getData)

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

