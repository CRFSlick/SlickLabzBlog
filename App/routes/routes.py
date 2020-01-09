from flask import render_template
from flask import Blueprint
from flask_scss import Scss
from flaskext.markdown import Markdown
from App import app
from App.modules.api.api import github_markdown
from App.modules.helpers.helpers import get_metadata, get_post
import mistune

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('home.html')


# @main.route('/2')
# def index2():
#     # data = open('_posts/2017-02-01-markdown-examples.md').read()
#     # data = mistune.markdown(data)
#     data = get_data()
#     return render_template('home2.html', content=data)


@main.route('/ctf/htb/craft')
def craft():
    markdown_raw = open(app.root_path + '\\posts\\blog.md').read()
    post = get_post(markdown_raw)
    post['content'] = github_markdown(post['content'])
    return render_template('post.html', post=post)


@main.route('/ctf/htb/obscurity')
def obscurity():
    markdown_raw = open(app.root_path + '\\posts\\blog_neo.md').read()
    post = get_post(markdown_raw)
    post['content'] = github_markdown(post['content'])
    return render_template('post.html', post=post)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404