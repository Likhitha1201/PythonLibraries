# @Author: Likhitha S
# @Date: 30-10-2024 12:50
# @Last Modified by: Likhitha S
# @Last Modified time: 30-10-2024 12:50
# @Title: Write a program to draw a scatter plot for random 1000 x and y coordinates

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

def main():
    """
    Description: 
        This function is used to draw a scatter plot using plotly.
    Parameters: 
        x, y are the plots taken from the random.randint()
    return:
        It displays the graph with scatter plots.
    """
    
    app = dash.Dash(__name__)
    
    app.layout = html.Div([
        html.H1('Scatterplot Using Plotly Library'),
      
        dcc.Graph(
            id='simplechart',
            figure={
                'data': [
                    {
                        'x': np.random.randint(1, 1000, size=100), 
                        'y': np.random.randint(1, 1000, size=100),
                        'type': 'scatter',
                        'mode': 'markers',
                        'name': 'Very first chart'
                    }
                ],
                'layout': {
                    'title': 'Scatter plot using random'
                }
            }
        )
    ])
   
    app.run_server(port=5501)
    
if __name__ == "__main__":
    main()
