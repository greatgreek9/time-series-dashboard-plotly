import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

import numpy as np
import json

from datetime import datetime
from keras.models import load_model

model = load_model('my_time_series_model.h5')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('data/AAPL.csv', parse_dates=True)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children = [
						    html.H2('Dash - STOCK PRICES'),
						    html.P('''Visualising time series with Plotly - Dash'''),
						    html.P('''Pick one or more stocks from the dropdown below.'''),
                             html.Div(
                             children = [
                             dcc.Graph(id='timeseries',
                             config={'displayModeBar': False},
                             animate=True,
                             figure=px.line(df,
                                    x='Date',
                                    y='Close',
                                    template='plotly_dark').update_layout(
                                                  {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                                   'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                                   )
						]),
                         html.Div(
           children = [
                     dcc.Graph(id='timeseries1',
                     config={'displayModeBar': False},
                     animate=True,
                     figure=px.line(df,
                            x='Date',
                            y='Close',
                            template='plotly_dark').update_layout(
                                          {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                           'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                           )
                        ])
                    ])


if __name__ == '__main__':
    app.run_server(port = 5000, debug=True)
