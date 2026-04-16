import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Simple direct path - the CSV is in the same folder
df = pd.read_csv('formatted_output.csv')

# Create the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer"),

    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all'
    ),

    dcc.Graph(id='sales-chart')
])


# Callback
@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(filtered_df, x='date', y='sales')
    fig.update_layout(
        title=f'Pink Morsel Sales - {selected_region.upper()}',
        xaxis_title='Date',
        yaxis_title='Sales ($)'
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)