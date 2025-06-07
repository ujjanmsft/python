from dash import html, dcc

layout = html.Div([
    html.H2("Admin Sign-Up"),

    dcc.Input(id='signup-username', type='text', placeholder='Choose username'),
    dcc.Input(id='signup-password', type='password', placeholder='Choose password'),
    html.Button('Sign Up', id='signup-btn', n_clicks=0),
    html.Div(id='signup-message', style={'color': 'green', 'marginTop': '10px'}),

    html.Br(),
    dcc.Link("Already have an account? Login", href='/admin-login')
])