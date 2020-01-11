from werkzeug.contrib.fixers import ProxyFix
from flask import Flask

# Initialize the application
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)

# Register application routes
from App.routes.routes import main
app.register_blueprint(main)
