from App import app
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
    url = post['url']
    filename = post['filename']
    slash = determine_slash_type()
    full_path = f'{app.root_path}{slash}data{slash}views.json'
    views_log = json.loads(open(full_path, 'r').read())

    for post in views_log:
        if post['url'] == url and post['filename'] == filename:
            if ip not in post['ips']:
                post['views'] += 1
                post['ips'].append(ip)
                open(full_path, 'w+').write(json.dumps(views_log, indent=4))
                return
            else:
                return

    views_log.append({'url': url, 'views': 1, 'filename': filename, 'ips': [ip]})
    open(full_path, 'w+').write(json.dumps(views_log, indent=4))
    return


def write_meta(metadata, data, index_1, index_2, filename):
    start_tag = '{{ META START }}'
    end_tag = '{{ META END }}'
    data_to_keep = data[index_2 + len(end_tag):].strip()

    meta = '{{ META START }}\n' \
           f'{json.dumps(metadata, indent=4)}\n' \
           '{{ META END }}\n\n'

    slash = determine_slash_type()
    open(f'{app.root_path}{slash}posts{slash}{filename}', 'w+').write(meta + data_to_keep)
    return


def get_post_data(data, filename):
    start_tag = '{{ META START }}'
    end_tag = '{{ META END }}'
    index_1 = data.find(start_tag)
    index_2 = data.find(end_tag)

    if index_1 != -1 and index_2 != -1:
        metadata = json.loads(data[index_1 + len(start_tag):index_2])

        try:
            metadata['timestamp']
        except KeyError:
            metadata['timestamp'] = int(time.time())
            write_meta(metadata, data, index_1, index_2, filename)

        metadata['content'] = data[index_2 + len(end_tag):].strip()
        return metadata


def get_posts():
    posts = []
    slash = determine_slash_type()
    post_filenames = glob.glob(f'{app.root_path}{slash}posts{slash}*.md')

    for filename in post_filenames:
        post = dict()
        post['filename'] = filename.split(slash)[len(filename.split(slash)) - 1]
        if len(re.findall('(.*)-(.*)-(.*).md', post['filename'])) == 1:
            post['url'] = '/'.join(post['filename'].rstrip('.md').split('-'))
            post['data'] = get_post_data(open(f'{app.root_path}{slash}posts{slash}{post["filename"]}', 'r').read(),
                                         post['filename'])
            posts.append(post)
        else:
            continue

    posts.sort(key=lambda x: x['data']['timestamp'], reverse=True)
    return posts


def get_categories(posts):
    categories = []
    for post in posts:
        category = post['data']['category']
        if category not in categories:
            categories.append(category)
    return categories
