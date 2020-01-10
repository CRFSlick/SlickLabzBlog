from App import app
import re
import json
import glob


def log_view(post, ip):
    url = post['url']
    filename = post['filename']
    full_path = f'{app.root_path}\\data\\views.json'
    views_log = json.loads(open(full_path, 'r').read())

    for post in views_log:
        if post['url'] == url and post['filename'] == filename:
            if ip not in post['ips']:
                post['views'] += 1
                post['ips'].append(ip)
                open(full_path, 'w+').write(json.dumps(views_log))
                return
            else:
                return

    views_log.append({'url': url, 'views': 1, 'filename': filename, 'ips': [ip]})
    open(full_path, 'w+').write(json.dumps(views_log))
    return


def get_post_data(data):
    start_tag = '{{ META START }}'
    end_tag = '{{ META END }}'
    index_1 = data.find(start_tag)
    index_2 = data.find(end_tag)

    if index_1 != -1 and index_2 != -1:
        metadata = json.loads(data[index_1 + len(start_tag):index_2])
        metadata['content'] = data[index_2 + len(end_tag):].strip()
        return metadata


def get_posts():
    posts = []
    post_filenames = glob.glob(app.root_path + '\\posts\\*.md')

    for filename in post_filenames:
        post = dict()
        post['filename'] = filename.split("\\")[len(filename.split("\\")) - 1]
        if len(re.findall('(.*)-(.*)-(.*).md', post['filename'])) == 1:
            post['url'] = '/'.join(post['filename'].rstrip('.md').split('-'))
            post['data'] = get_post_data(open(app.root_path + f'\\posts\\{post["filename"]}').read())
            posts.append(post)
        else:
            continue

    return posts


def get_categories(posts):
    categories = []
    for post in posts:
        category = post['data']['category']
        if category not in categories:
            categories.append(category)
    return categories
