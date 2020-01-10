from flask import render_template
from flask import Blueprint
from flask import abort
from App import app
from App.modules.api.api import github_markdown
from App.modules.helpers.helpers import get_post_data, get_posts

main = Blueprint('main', __name__)


@main.route('/')
def index():
    posts = get_posts()
    posts_data = []

    for post in posts:
        data = open(app.root_path + f'\\posts\\{post["filename"]}').read()
        url = post['url']
        post = get_post_data(data)
        post['url'] = url
        posts_data.append(post)

    print(posts_data)

    return render_template('home.html', posts=posts_data)


@main.route('/<category>/<subcategory>/<post>')
def display_post(category, subcategory, post):
    request = f'{category}-{subcategory}-{post}.md'
    posts = get_posts()

    if request in posts:
        data = open(app.root_path + f'\\posts\\{request}').read()
        post = get_post_data(data)
        post['content'] = github_markdown(post['content'])
        return render_template('post.html', post=post)
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404