import django
import django_heroku
import gunicorn
from flask import Flask
import os
import pandas as pd
import plotly.express as px
import numpy as np
import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_daq as daq
import seaborn as sns
import matplotlib as plt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[external_stylesheets])

df = pd.read_csv('dissertationlog.csv')

colors = {
    'background': '#090802',
    'text': '#BDB477'
}

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div([
    html.H1('Martin, KJ (2020) Dissertation', style = {'color':colors['text']})]),
    html.Div([
        dcc.Dropdown(id='x', options = [
            {'label':'Muscle','value':'muscle'},
            {'label':'KEAP1','value':'keap1c'},
            {'label':'Nuclear Nrf2','value':'nrf2n'},
            {'label':'Cytosolic Nrf2','value':'nrf2c'},
            {'label':'SOD1','value':'sod1t'},
            {'label':'HO1','value':'ho1t'}]),
        dcc.Dropdown(id='y', options = [
            {'label':'KEAP1','value':'keap1c'},
            {'label':'Nuclear Nrf2','value':'nrf2n'},
            {'label':'Cytosolic Nrf2','value':'nrf2c'},
            {'label':'SOD1','value':'sod1t'},
            {'label':'HO1','value':'ho1t'}]),
        daq.ToggleSwitch(
        id='group',
        value=False
        ),
        dcc.Graph(
            id = 'graph')
        ])
    ], className = 'Row')

                

@app.callback(
        Output('graph', 'children'),
        Input('x', 'value'),
        Input('y', 'value'),
        Input('by-exercise', 'value')
)
def update_graph(x, y, group):
    return {
        'figure':go.Figure(
            data = [
                Scatter(
                    x=df[x],
                    y=data[y]
                )
            ]
        )
    }

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

