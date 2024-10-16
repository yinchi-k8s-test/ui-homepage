"""Webpage for the Homepage service."""

import dash_bootstrap_components as dbc
from dash import Dash, html
from dash_compose import composition

from .common import settings
from .db import get_session, init_db, list_services

app = Dash(
    external_stylesheets=[dbc.themes.UNITED],
    requests_pathname_prefix=settings.root_path + ('' if settings.root_path[-1] == '/' else '/')
)


@composition
def layout():
    """Set the homepage layout."""

    with get_session() as session:
        svcs = list_services(session)

    with html.Div(className='m-3') as ret:
        yield html.H1('Kind test cluster')
        with dbc.Stack(gap=2, style={'max-width': '600px'}):
            for svc in svcs:
                with dbc.Button(
                    size='lg',
                    style={'width': '100%'},
                    target='_blank',
                    href=f"""\
{svc.protocol}://{settings.host}:{svc.port}/{svc.path if svc.path != '/' else ''}""",
                    external_link=True,
                    color='primary'
                ):
                    yield f'{svc.name} ({svc.cluster_name})'

    return ret


app.layout = layout


# Production server
def server():
    """Initialise the app and return the Flask server"""
    init_db()
    return app.server


# Development server
if __name__ == '__main__':
    init_db()
    print(settings)
    app.run(debug=True)
