import plotly.graph_objects as go
import pandas as pd

# ساخت داده‌های مصنوعی برای نمونه
data = pd.DataFrame({
    'timestamp': pd.date_range(start='2022-01-01', periods=10, freq='D'),
    'open': [100, 110, 120, 115, 125, 130, 128, 132, 135, 130],
    'close': [110, 120, 115, 125, 130, 128, 132, 135, 130, 140],
    'high': [120, 125, 130, 128, 132, 135, 135, 138, 140, 145],
    'low': [100, 110, 115, 110, 120, 125, 127, 128, 130, 128]
})

fig = go.Figure()

for i in range(len(data)):
    color = 'green' if data['close'].iloc[i] > data['open'].iloc[i] else 'red'  # تعیین رنگ الگوی شمع
    fig.add_trace(go.Candlestick(x=[data['timestamp'][i]],
                    open=[data['open'][i]],
                    high=[data['high'][i]],
                    low=[data['low'][i]],
                    close=[data['close'][i]],
                    increasing_line_color= 'green',
                    decreasing_line_color= 'red',
                    line=dict(width=2)  # تعیین ضخامت خط برای بدنه‌ی شمع
    ))

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()