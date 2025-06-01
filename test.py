from dash import Dash, html, dcc
stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div([
    html.Div(dcc.Dropdown(), className='four columns'),
    html.Div(dcc.Dropdown(), className='four columns'),
    html.Div(dcc.Dropdown(), className='four columns'),
    ], className='row')


if __name__ == '__main__':
    app.run(debug=True)