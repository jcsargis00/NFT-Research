# Interactive Pricing on Cryptocurrencies
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Cryptocurrency price analysis'),
    dcc.Graph(id="time-series-chart"),
    html.P("Select cryptocurrency:"),
    dcc.Dropdown(
        id="ticker",
        options=["BTC", "ETH", "USDT", "USDC"],
        value="BTC",
        clearable=False,
    ),
])


@app.callback(
    Output("time-series-chart", "figure"), 
    Input("ticker", "value"))
def display_time_series(ticker):
    df = pd.read_csv('coins.csv')
    #df = px.data.stocks() # replace with your own data source
    fig = px.line(df, x='date', y=ticker)
    return fig


app.run_server(debug=True)