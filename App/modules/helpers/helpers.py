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
    tmp_posts = glob.glob(app.root_path + '\\posts\\*.md')

    try:
        tmp_posts.remove(app.root_path + '\\posts\\template.md')
    except ValueError:
        pass

    for post in tmp_posts:
        post_data = dict()
        post_data['filename'] = post.split("\\")[len(post.split("\\")) - 1]
        post_data['url'] = '/'.join(post_data['filename'].rstrip('.md').split('-'))
        posts.append(post_data)

    return posts
