from flask import render_template
from flask import Blueprint
from flask import abort
from App import app
from App.modules.api.api import github_markdown
from App.modules.helpers.helpers import get_post, get_posts

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/<category>/<subcategory>/<post>')
def display_post(category, subcategory, post):
    request = f'{category}-{subcategory}-{post}.md'
    posts = get_posts()

    if request in posts:
        markdown_raw = open(app.root_path + f'\\posts\\{request}').read()
        post = get_post(markdown_raw)
        post['content'] = github_markdown(post['content'])
        return render_template('post.html', post=post)
    else:
        abort(404)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404