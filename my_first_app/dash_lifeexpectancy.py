from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate a data source
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the Dash app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Life Expectancy'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
