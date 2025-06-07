from dash import Dash, html, dcc, Input, Output, State
import pages.home as home
import pages.about as about
import pages.contact as contact
import pages.dashboard as dashboard
import pages.faq as faq
import pages.services as services
import pages.feedback as feedback
import pages.admin_login as admin_login
import pages.admin_dashboard as admin_dashboard
import pages.admin_signup as admin_signup
from dash.exceptions import PreventUpdate

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
        html.Img(src='/assets/logo.png', style={'height': '100px'}),

        html.Div([
            link('Home', '/', 'fas fa-home'),
            link('About Us', '/about', 'fas fa-info-circle'),
            link('Contact Us', '/contact', 'fas fa-envelope'),
            link('Dashboard', '/dashboard', 'fas fa-chart-line'),
            link('FAQ', '/faq', 'fas fa-question-circle'),
            link('Services', '/services', 'fas fa-cogs'),
            link('Feedback', '/feedback', 'fas fa-comment'),
            link('Sign-Up', '/admin-signup', 'fas fa-user-plus'),
            link('Login', '/admin-login', 'fas fa-user-shield'),
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
    elif pathname == '/admin-login':
        return admin_login.layout
    elif pathname == '/admin-signup':
        return admin_signup.layout
    elif pathname == '/admin-dashboard':
        return admin_dashboard.layout
    else:
        return home.layout  # default
    
# 🔐 Admin login validation
@app.callback(
    Output('admin-login-message', 'children'),
    Output('url', 'pathname'),
    Input('admin-login-btn', 'n_clicks'),
    State('admin-username', 'value'),
    State('admin-password', 'value'),
    prevent_initial_call=True
)
def validate_admin_login(n_clicks, username, password):
    if n_clicks is None:
        raise PreventUpdate

    if not username or not password:
        return 'Please enter username and password.', dash.no_update

    if username == 'admin' and password == 'password123':
        return '', '/admin-dashboard'
    else:
        return 'Invalid credentials', dash.no_update

#Sidebar
app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id='navbar-container'),

    # Main content and sidebar container
    html.Div([

        # Page Content on the left
        html.Div(id='page-content', style={'flex': 1, 'padding': '20px'}),

        # Sidebar on the right
        html.Div([
            html.H2("Menu", style={'margin-bottom': '20px'}),
            dcc.Link("Dashboard", href="/dashboard", className='sidebar-link'),
            dcc.Link("Profile", href="/profile", className='sidebar-link'),
            dcc.Link("Settings", href="/settings", className='sidebar-link'),
            dcc.Link("Logout", href="/logout", className='sidebar-link'),
        ], className='sidebar')

    ], style={'display': 'flex', 'flex': 1}),

    # Footer
    html.Footer([
        html.Div([
            html.Div([
                dcc.Link("Privacy Policy", href="/privacy", style={'margin-right': '15px'}),
                dcc.Link("Terms of Service", href="/terms")
            ], style={'margin-bottom': '10px'}),

            html.Div("© 2025 My Awesome Site"),

            html.Div([
                html.A(html.I(className="fab fa-facebook"), href="https://facebook.com", target="_blank", style={'margin-right': '10px'}),
                html.A(html.I(className="fab fa-twitter"), href="https://twitter.com", target="_blank", style={'margin-right': '10px'}),
                html.A(html.I(className="fab fa-linkedin"), href="https://linkedin.com", target="_blank")
            ], className='footer-social-icons')
        ], style={
            'display': 'flex',
            'justifyContent': 'space-between',
            'flexWrap': 'wrap',
            'padding': '10px 20px',
            'borderTop': '1px solid #ccc',
            'backgroundColor': '#f9f9f9',
            'fontSize': '14px'
        })
    ])
], style={
    'display': 'flex',
    'flexDirection': 'column',
    'minHeight': '100vh'
})


# 🚀 Run app
if __name__ == '__main__':
    app.run(debug=True)
