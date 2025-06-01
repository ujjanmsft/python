# Import Dash modules
from dash import Dash, html, dcc, Input, Output
import pages.home as home
import pages.about as about
import pages.contact as contact
import pages.dashboard as dashboard
import pages.faq as faq
import pages.services as services
import pages.feedback as feedback

# Create Dash app and load optional external CSS
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[
    'https://codepen.io/chriddyp/pen/bWLwgP.css'  # Bootstrap-like theme
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css'
])
server = app.server  # for deployment (e.g., Heroku, Render)

# Layout with navigation and page content container
app.layout = html.Div([
    dcc.Location(id='url'),  # Tracks browser URL

    # Navigation bar
    html.Div([
        dcc.Link('Home', href='/', style={'margin-right': '15px'}),
        dcc.Link('About Us', href='/about', style={'margin-right': '15px'}),
        dcc.Link('Contact Us', href='/contact', style={'margin-right': '15px'}),
        dcc.Link('Dashboard', href='/dashboard', style={'margin-right': '15px'}),
        dcc.Link('FAQ', href='/faq', style={'margin-right': '15px'}),
        dcc.Link('Services', href='/services', style={'margin-right': '15px'}),
        dcc.Link('Feedback', href='/feedback', style={'margin-right': '15px'}),
    ], className='navbar'),

    html.Hr(),

    html.Div(id='page-content', style={'padding': '20px'})  # where pages will render
])

# Callback: decide what content to show based on URL
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/about':
        return about.layout
    elif pathname == '/contact':
        return contact.layout
    elif pathname == '/dashboard':
        return dashboard.layout
    elif pathname == '/faq':
        return faq.layout
    elif pathname == '/services':
        return services.layout
    elif pathname == '/feedback':
        return feedback.layout
    else:
        return home.layout  # default is home

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
