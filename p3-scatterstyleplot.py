import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

def main():
    """
        Description: 
            This function is used to draw a scatter plot using plotly with style.
        Parameters: 
            x, y are the plots taken from the random.rand()
        return:
            It displays the graph with scatter plots.
    """
   
    np.random.seed(42)
    x = np.random.rand(500)
    y = np.random.rand(500)

    # Define color scheme
    colors = {
        'plot_color': 'aqua',  
        'paper_color': 'pink', 
        'text': 'green'         
    }

    app = dash.Dash()
    
    app.layout = html.Div([
       html.H1(children="Welcome to Scatter Plot Styling..",
               style={
                   'textAlign': 'center',
                   'color': colors['text']
               }
           ),
       
       dcc.Graph(
            id='scatterplot styling',
            
           figure={
               'data': [
                   {
                       'x': x,
                       'y': y,
                       'mode': 'markers',
                       'name': 'Very first chart with scatter',
                       'marker': {'color': 'rgba(152, 0, 0, .8)', 'size': 10},
                   },
               ],
               'layout': {
                   'title': 'Scatterplot Styling',
                   'plot_bgcolor': colors['plot_color'],
                   'paper_bgcolor': colors['paper_color'],
                   'xaxis':{'title':'x-axis'},
                   'yaxis':{'title':'y-axis'},
                   'font': {
                       'color': colors['text']
                   }
               }
           }
       ) 
   ])
    
    app.run_server(port=5605)
    
if __name__ == "__main__":
    main()
