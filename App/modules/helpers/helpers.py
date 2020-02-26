from App import app
import flask
import json
import glob
import time
import re
import os


def determine_slash_type():
    """
    Gets the right type of slash for compatibility between linux/mac/windows

    Returns:
        slash_type

    """
    current_path = os.path.dirname(__file__)

    if '\\' in current_path:
        slash_type = '\\'
    elif '/' in current_path:
        slash_type = '/'
    else:
        slash_type = '/'

    return slash_type


def log_view(post, ip):
    """
    Logs a view for a given post and IP

    Args:
        post (dict)
        ip (str)

    """
    url = post['url']
    filename = post['filename']
    slash = determine_slash_type()
    full_path = f'{app.root_path}{slash}data{slash}views{slash}views.json'

    while True:
        try:
            views_log = json.loads(open(full_path, 'r').read())
            break
        except FileNotFoundError:
            views_log = list()
            views_log.append({'url': url, 'filename': filename, 'views': 1, 'ips': [ip]})
            open(full_path, 'w+').write(json.dumps(views_log, indent=4))
            return
        except:
            # In case flask workers try an access the same file at the same time...
            pass

    for post in views_log:
        if post['url'] == url and post['filename'] == filename:
            if ip not in post['ips']:
                post['views'] += 1
                post['ips'].append(ip)
                open(full_path, 'w+').write(json.dumps(views_log, indent=4))
                return
            else:
                return

    views_log.append({'url': url, 'filename': filename, 'views': 1, 'ips': [ip]})
    open(full_path, 'w+').write(json.dumps(views_log, indent=4))
    return


def get_views(post):
    """
    Gets views for a given post

    Args:
        post (dict)

    """
    url = post['url']
    filename = post['filename']
    slash = determine_slash_type()
    full_path = f'{app.root_path}{slash}data{slash}views{slash}views.json'

    while True:
        try:
            views_log = json.loads(open(full_path, 'r').read())
            break
        except FileNotFoundError:
            return '0 Views'
        except:
            # In case flask workers try an access the same file at the same time...
            pass

    for post in views_log:
        if post['url'] == url and post['filename'] == filename:
            views = post['views']
            if views == 1:
                return f'{views} View'
            else:
                return f'{views} Views'

    return '0 Views'


def write_meta(metadata, data, index_1, index_2, filename):
    """
    Writes modified metadata back to an existing file

    Args:
       metadata (dict)
       data (str)
       index_1 (int)
       index_2 (int)
       filename (str)

    """
    start_tag = '{{ META START }}'
    end_tag = '{{ META END }}'
    data_to_keep = data[index_2 + len(end_tag):].strip()

    meta = f'{start_tag}\n{json.dumps(metadata, indent=4)}\n{end_tag}\n\n'

    slash = determine_slash_type()
    open(f'{app.root_path}{slash}posts{slash}{filename}', 'w+').write(meta + data_to_keep)
    return


def get_post_data(data, filename):
    """
    Gets metadata for a given post

    Args:
        data (str)
        filename (str)

    Returns:
        metadata (dict)

    """
    start_tag = '{{ META START }}'
    end_tag = '{{ META END }}'
    index_1 = data.find(start_tag)
    index_2 = data.find(end_tag)

    if index_1 != -1 and index_2 != -1:
        try:
            metadata = json.loads(data[index_1 + len(start_tag):index_2])
        except:
            raise Exception('Error parsing post JSON metadata!')

        try:
            metadata['timestamp']
        except KeyError:
            metadata['timestamp'] = int(time.time())
            write_meta(metadata, data, index_1, index_2, filename)

        metadata['content'] = data[index_2 + len(end_tag):].strip()
        return metadata


def get_posts():
    """
    Gets a list of all posts located in the posts directory
    *NOTE* Posts must conform to the following format: "category-subcategory-title.md"

    Returns:
        posts (list)

    """
    posts = []
    slash = determine_slash_type()
    post_filenames = glob.glob(f'{app.root_path}{slash}posts{slash}*.md')

    for filename in post_filenames:
        post = dict()
        post['filename'] = filename.split(slash)[len(filename.split(slash)) - 1]
        if len(re.findall('^(.*)-(.*)-(.*).md$', post['filename'])) == 1:
            data = open(f'{app.root_path}{slash}posts{slash}{post["filename"]}', 'r', encoding='utf-8').read()
            post['url'] = '/'.join(post['filename'].rstrip('.md').split('-'))
            post['data'] = get_post_data(data, post['filename'])
            posts.append(post)
        else:
            continue

    posts.sort(key=lambda x: x['data']['timestamp'], reverse=True)
    return posts


def get_categories(posts):
    """
    Gets a list of all categories for sorting

    Args:
        posts (list)

    Returns:
        categories (list)

    """
    categories = []
    for post in posts:
        category = post['data']['category']
        if category not in categories:
            categories.append(category)
    return categories


def login_required(f):
    def wrapper():
        try:
            if not flask.session['active']:
                return flask.redirect('/login')
        except KeyError:
            return flask.redirect('/login')
        return f()
    return wrapper
