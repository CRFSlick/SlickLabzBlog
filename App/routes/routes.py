from App.modules.helpers.helpers import get_posts, get_categories, log_view, get_views, login_required, is_authenticated
from App.modules.api.api import get_markdown
from flask import send_from_directory
from flask import render_template
from flask import Blueprint
from flask import abort
from flask import request
from App import app
import os
import flask

main = Blueprint('main', __name__)


@app.route('/favicon.ico')
def favicon():
    path = os.path.join(app.root_path, 'static', 'images')
    return send_from_directory(path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@main.route('/', methods=['GET'])
def index():
    posts = get_posts()
    return render_template('home.html', posts=posts, shown_posts=3, page_title="Home")


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
            page_tile = post["data"]["title"]
            return render_template('post.html', post=post, page_title=page_tile, post_footer=True)

    abort(404)


'''#Todo'''
# @main.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         if is_authenticated():
#             return flask.redirect('/admin')
#         return render_template('login.html', page_title="Login")
#     elif request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         if username == app.config['USERNAME'] and password == app.config['PASSWORD']:
#             flask.session['username'] = username
#             flask.session['password'] = password
#             flask.session['active'] = True
#             return flask.redirect('/admin')
#         else:
#             return render_template('login.html', page_title="Login")


'''#Todo'''
# @main.route('/admin', methods=['GET'])
# @login_required
# def admin():
#     return render_template('admin.html', page_title="Admin")
