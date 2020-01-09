from flask import render_template
from flask import Blueprint
from flask_scss import Scss
from flaskext.markdown import Markdown
from App import app
from App.modules.api.api import get_data
import mistune

main = Blueprint('main', __name__)
Scss(app)
Markdown(app)


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/2')
def index2():
    # data = open('_posts/2017-02-01-markdown-examples.md').read()
    # data = mistune.markdown(data)
    data = get_data()
    return render_template('home2.html', content=data)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404