""" 
    @Author: Likhitha S
    @Date: 31-10-2024 12:50
    @Last Modified by: Likhitha S
    @Last Modified time: 31-10-2024 12:50
    @Title: Write a program to draw line and scatter plots for random 100 x and y coordinates. 

"""

import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

def main():
    """

        Description: 
            This function is used to draw a line and scatter plot using plotly.
        Parameters: 
            x, y are the plots taken from the random.randint()
        return:
            It displays the graph with scatter plots.

    """
   
    np.random.seed(42)
    x = np.random.rand(100)
    y = np.random.rand(100)

    app=dash.Dash()
    
    app.layout=html.Div([
       
       dcc.Graph(
        id='line and scatter',
        figure={
           'data':[
            go.Scatter(
               x= x,
               y= y,
               
               mode='markers'
           ),
            go.Scatter(
                x= x,
                y= y,
                mode='lines'
            )
           ],
           'layout':go.Layout(
               title='Line and Scatterplot with Random points',
               xaxis={'title':'Random x-axis'},
               yaxis={'title':'Random y-axis'}
           )
        }
       )
   ])
    
    app.run_server(port=5605)
    
if __name__=="__main__":
    main()
   