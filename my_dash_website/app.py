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
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css'
])
server = app.server  # for deployment

# 🔧 Function to render nav bar with active link
def render_navbar(current_path):
    def link(label, href, icon_class):
        is_active = 'active' if current_path == href else ''
        return dcc.Link(
            html.Span([
                html.I(className=icon_class),
                f' {label}'
            ]),
            href=href,
            className=is_active
        )

    return html.Div([
        html.Div([
            html.Img(src='/assets/logo.png', style={'height': '40px', 'margin-right': '10px'}),
        ], style={'display': 'flex', 'alignItems': 'center', 'gap': '10px'}),

        html.Div([
            link('Home', '/', 'fas fa-home'),
            link('About Us', '/about', 'fas fa-info-circle'),
            link('Contact Us', '/contact', 'fas fa-envelope'),
            link('Dashboard', '/dashboard', 'fas fa-chart-line'),
            link('FAQ', '/faq', 'fas fa-question-circle'),
            link('Services', '/services', 'fas fa-cogs'),
            link('Feedback', '/feedback', 'fas fa-comment')
        ], style={'margin-top': '10px', 'display': 'flex', 'flexWrap': 'wrap', 'gap': '10px'})
    ], className='navbar')


# 🔧 Define layout with placeholders for URL-based content
app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id='navbar-container'),
    html.Hr(),
    html.Div(id='page-content', style={'padding': '20px'})
])

# 🔁 Callback to update navbar based on current URL
@app.callback(
    Output('navbar-container', 'children'),
    Input('url', 'pathname')
)
def update_navbar(pathname):
    return render_navbar(pathname)

# 🔁 Callback to render pages
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
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
        return home.layout  # default

# 🚀 Run app
if __name__ == '__main__':
    app.run(debug=True)
