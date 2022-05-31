import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

API_KEY = NLHR04LATEYL0K16
COINS = ['BTC', 'ETH', 'MKR', 'BCH', 'DOGE']
rolling_period = 15
date_time = str(datetime.datetime.now())[0:16].replace(':','-').replace(' ','_') # File Explorer Safe Name
with open('Crypto_Report_'+date_time+'.html', 'a') as f:
    for coin in COINS:
        df = load_data(coin, API_KEY)
        df = calculate_rsi(df, rolling_period)
        df_group = generate_table(df)

        fig = go.Figure(make_subplots(
            rows=4, cols=1, shared_xaxes=True,
            vertical_spacing=0.05,
            specs=[[{}],[{}],[{}],[{"type": "table"}]]
        ))
        fig.add_trace(
            go.Candlestick(
                x=df.index, open=df['open'], high=df['high'],
                low=df['low'], close=df['close'], name= coin + ' Candlestick',
                increasing_line_color= 'rgb(27,158,119)', decreasing_line_color= 'rgb(204,80,62)'
            ), row=1, col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=df.index, y=df['close'],
                name= coin+' Price', marker_color='#0099C6'
            ),row=2, col=1
        )
        fig.add_trace(
            go.Scatter(
                x=list(df.index)+list(df.index[::-1]),
                y=list(df['close'].transform(lambda x: x.rolling(rolling_period,1).mean()) + (2*df['close'].transform(lambda x: x.rolling(rolling_period,1).std())))
                    +list(df['close'].transform(lambda x: x.rolling(rolling_period,1).mean()) - (2*df['close'].transform(lambda x: x.rolling(rolling_period,1).std()))[::-1]),
                fill='toself',
                fillcolor='rgba(0,176,246,0.2)', line_color='rgba(255,255,255,0)',
                name='Bollinger Bands', showlegend=False,
            ),row=2, col=1
        )
        fig.add_trace(
            go.Scatter(
                x=df.index, y=df['close'].transform(lambda x: x.rolling(rolling_period,1).mean()),
                line = dict(dash='dot'), marker_color='rgba(0,176,246,0.2)',
                showlegend=False, name='Moving Average'
            ),row=2, col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=df.index, y=df['RSI'],
                name='RSI', marker_color='#109618'
            ), row=3, col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=df.index, y=[70] * len(df.index),
                name='Overbought', marker_color='#109618',
                line = dict(dash='dot'), showlegend=False,
            ), row=3, col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=df.index, y=[30] * len(df.index),
                name='Oversold', marker_color='#109618',
                line = dict(dash='dot'),showlegend=False,
            ),row=3, col=1,
        )
        fig.add_trace(
            go.Table(
                header=dict(
                    values=list(df_group.columns),
                    font=dict(size=10), align="left"),
                cells=dict(
                    values=[df_group[k].tolist() for k in df_group.columns[0:]],align = "left")
            ),row=4, col=1
        )
        fig.update_layout(
            title= coin + ' Report',
            yaxis_title='Price',
            template='plotly_dark',
            xaxis1_rangeslider_visible=False,
            height=800
        )
        f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))