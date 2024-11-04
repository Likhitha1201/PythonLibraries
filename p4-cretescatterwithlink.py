import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd

def main():
    data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
    x_val = data['Rank']
    y_val = data['Population']

    app = dash.Dash()

    app.layout = html.Div([
        dcc.Graph(
            id='line_and_scatter',
            figure={
                'data': [
                    {
                        'x': x_val,
                        'y': y_val,
                        'mode': 'markers',
                        'name': 'Scatter plot from given URL'
                    }
                ],
                'layout': {
                    'title': 'Line and Scatterplot with Given Points',
                    'xaxis': {'title': 'Rank (x-axis)'},
                    'yaxis': {'title': 'Population (y-axis)'}
                }
            }
        )
    ])

    app.run_server(port=5605)

if __name__ == "__main__":
    main()
