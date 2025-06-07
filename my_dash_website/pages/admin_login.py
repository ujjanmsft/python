from dash import Dash, html, dcc, Input, Output, State

layout = html.Div([
    html.H2("Admin Login"),
    
    html.Div([
        dcc.Input(id='admin-username', type='text', placeholder='Username'),
        dcc.Input(id='admin-password', type='password', placeholder='Password'),
        html.Button('Login', id='admin-login-btn', n_clicks=0),
        html.Div(id='admin-login-message', style={'color': 'red', 'marginTop': '10px'})
    ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '10px', 'maxWidth': '300px'})
])