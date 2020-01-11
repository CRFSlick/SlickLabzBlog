from werkzeug.contrib.fixers import ProxyFix
from flask import Flask
import json

# Initialize the application
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)


# Determine the type of slash this OS uses
from App.modules.helpers.helpers import determine_slash_type
slash = determine_slash_type()


# Get configuration
class Config:
    with open(f'{app.root_path}{slash}config{slash}config.json') as config_file:
        config = json.load(config_file)

    GITHUB_OAUTH = config.get('github_oauth')


# Configure the application with API keys
app.config.from_object(Config)

# Register application routes
from App.routes.routes import main
app.register_blueprint(main)
