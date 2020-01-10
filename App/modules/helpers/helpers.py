from App import app
import json
import glob


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

    try:
        post_filenames.remove(app.root_path + '\\posts\\template.md')
    except ValueError:
        pass

    for filename in post_filenames:
        post = dict()
        post['filename'] = filename.split("\\")[len(filename.split("\\")) - 1]
        post['url'] = '/'.join(post['filename'].rstrip('.md').split('-'))
        post['data'] = get_post_data(open(app.root_path + f'\\posts\\{post["filename"]}').read())
        posts.append(post)

    return posts


def get_categories(posts):
    categories = []
    for post in posts:
        category = post['data']['category']
        if category not in categories:
            categories.append(category)
    return categories
