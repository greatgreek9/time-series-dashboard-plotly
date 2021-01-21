import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

df = pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True)

server = app.server

app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='four columns div-user-controls',
					children = [
						    html.H2('Dash - STOCK PRICES'),
						    html.P('''Visualising time series with Plotly - Dash'''),
						    html.P('''Pick one or more stocks from the dropdown below.''')
						]),  # Define the left element
				
                                  html.Div(className='eight columns div-for-charts bg-grey',
					children = [
						dcc.Graph(id='timeseries',
          config={'displayModeBar': False},
          animate=True,
          figure=px.line(df,
                         x='Date',
                         y='value',
                         color='stock',
                         template='plotly_dark').update_layout(
                                   {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )
						])  # Define the right element
                                  ])
                                ])


if __name__ == '__main__':
    app.run_server(port = 5000, debug=True)
