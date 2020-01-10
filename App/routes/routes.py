from flask import render_template
from flask import Blueprint
from flask import abort
from App import app
from App.modules.api.api import github_markdown
from App.modules.helpers.helpers import get_post_data, get_posts, get_categories

main = Blueprint('main', __name__)


@main.route('/')
def index():
    posts = get_posts()
    return render_template('home.html', posts=posts)


@main.route('/posts')
def posts():
    posts = get_posts()
    categories = get_categories(posts)
    return render_template('posts.html', posts=posts, categories=categories)


@main.route('/<category>/<subcategory>/<post>')
def display_post(category, subcategory, post):
    request = f'{category}-{subcategory}-{post}'
    posts = get_posts()

    for post in posts:
        if request == post['filename'].rstrip('.md'):
            post['data']['content'] = github_markdown(post['data']['content'])
            return render_template('post.html', post=post)

    abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404