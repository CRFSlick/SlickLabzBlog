from App.modules.helpers.helpers import get_posts, get_categories, log_view, get_views
from App.modules.api.api import get_markdown
from flask import render_template
from flask import Blueprint
from flask import abort
from flask import request
from App import app

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    posts = get_posts()
    return render_template('home.html', posts=posts, page_title="Home")


@main.route('/posts', methods=['GET'])
def posts():
    posts = get_posts()
    categories = get_categories(posts)
    return render_template('posts.html', posts=posts, categories=categories, page_title="All Posts")


@main.route('/<category>/<subcategory>/<post>', methods=['GET'])
def display_post(category, subcategory, post):
    requested_post = f'{category}-{subcategory}-{post}'
    posts = get_posts()

    for post in posts:
        if requested_post == post['filename'].rstrip('.md'):
            log_view(post, request.remote_addr)
            post['data']['views'] = get_views(post)
            post['data']['content'] = get_markdown(post['data']['content'], requested_post)
            page_tile = f'{post["data"]["sub_category"]} - {post["data"]["title"]}'
            return render_template('post.html', post=post, page_title=page_tile)

    abort(404)
