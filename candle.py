import schedule
import time
from tradingview_ta import TA_Handler, Exchange, Interval
import plotly.graph_objects as go
import pandas as pd

# Create an empty figure
fig = go.Figure()

# Add an empty candlestick trace
fig.add_trace(go.Candlestick(x=[], open=[], high=[], low=[], close=[]))

# Define a function to update the figure
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
    
    # Update the figure data with new values
    fig.data[0].x = [pd.Timestamp.now()]
    fig.data[0].open = [open_price]
    fig.data[0].high = [max(open_price, close_price)]
    fig.data[0].low = [min(open_price, close_price)]
    fig.data[0].close = [close_price]

    # Update the figure layout
    fig.update_layout(xaxis_rangeslider_visible=False)
    
    # Show the updated figure
    fig.show()

# Schedule the task to run every 5 seconds
schedule.every(5).seconds.do(printCandle)

while True:
    schedule.run_pending()
    time.sleep(1)