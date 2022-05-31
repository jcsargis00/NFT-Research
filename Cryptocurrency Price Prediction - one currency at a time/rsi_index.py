def calculate_rsi(df, period=13):
    net_change = df['close'].diff()
    increase = net_change.clip(lower=0)
    decrease = -1*net_change.clip(upper=0)
    ema_up = increase.ewm(com=period, adjust=False).mean()
    ema_down = decrease.ewm(com=period, adjust=False).mean()
    RS = ema_up/ema_down
    df['RSI'] = 100 - (100/(1+RS)) 
    return df