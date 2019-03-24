"""
Main app
"""
import settings
import builder
import dash


app = dash.Dash(__name__)

builder.build_layout(app)

if __name__ == '__main__':
    app.run_server(host=settings.HOST, port=settings.PORT)
