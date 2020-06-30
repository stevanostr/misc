import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import seaborn as sns

tips = sns.load_dataset('tips')
external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div( children=[
    html.H1('Hello Dash'),
    
    html.Div(children = '''
    Dash: A web app framework for Python.'''),
    
    html.Div([
        dcc.Graph(
        id='example-graph',
        figure ={
            'data':[
                {'x': tips['smoker'],'y': tips['tip'], 'type': 'bar', 'name':'smoker' }
            ],
            'layout': {
                'title': 'Tips Dash Data Visualization'
            }
        })
    ])
])

if __name__ =='__main__':
    app.run_server(debug=True)