import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load your formatted data
df = pd.read_csv('formatted_output.csv')

# Convert sales to numeric
df['sales'] = pd.to_numeric(df['sales'])

# Convert date to datetime and sort
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create the line chart
fig = px.line(df,
              x='date',
              y='sales',
              title='Pink Morsel Sales Over Time',
              labels={'date': 'Date', 'sales': 'Sales ($)'})

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis",
            style={'textAlign': 'center',
                   'color': '#2c3e50',
                   'padding': '20px'}),

    html.H3("Did the price increase on Jan 15, 2021 affect sales?",
            style={'textAlign': 'center',
                   'color': '#7f8c8d',
                   'marginBottom': '30px'}),

    dcc.Graph(figure=fig),

    html.Div([
        html.P("The price increase occurred on January 15, 2021.",
               style={'textAlign': 'center', 'marginTop': '20px'}),
        html.P("Looking at the chart, sales show an upward trend after the price increase.",
               style={'textAlign': 'center', 'color': 'green'})
    ], style={'backgroundColor': '#f8f9fa', 'padding': '15px', 'borderRadius': '5px'})
])

# FIXED: Use app.run() instead of app.run_server()
if __name__ == '__main__':
    app.run(debug=True)