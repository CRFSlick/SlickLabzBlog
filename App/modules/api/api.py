from App.modules.helpers.helpers import determine_slash_type
from App import app
import requests
import json


def cache_page(markdown, markdown_raw, requested_post):
    """
    Caches the page in an effort to not exceed Github API rate limit"

    Args:
        markdown (str)
        markdown_raw (str)
        requested_post (str)

    """

    slash = determine_slash_type()
    path_to_cached_files = f'{app.root_path}{slash}data{slash}cached_posts{slash}'

    with open(f'{path_to_cached_files}{requested_post}.html', 'w+', encoding='utf-8') as cached_markdown:
        cached_markdown.write(markdown)

    with open(f'{path_to_cached_files}{requested_post}.md', 'w+', encoding='utf-8') as cached_markdown_raw:
        cached_markdown_raw.write(markdown_raw)

    return


def get_markdown(markdown_raw, requested_post):
    """
    Gets markdown content but tries to use cache first if possible, and if not, will cache the content.

    Args:
        markdown_raw (str)
        requested_post (str)

    """

    slash = determine_slash_type()
    path_to_cached_files = f'{app.root_path}{slash}data{slash}cached_posts{slash}'

    try:
        cached_markdown = open(f'{path_to_cached_files}{requested_post}.html', 'r', encoding='utf-8').read()
        cached_markdown_raw = open(f'{path_to_cached_files}{requested_post}.md', 'r', encoding='utf-8').read()
    except FileNotFoundError:
        markdown = github_api(markdown_raw)
        cache_page(markdown, markdown_raw, requested_post)
        return markdown

    if markdown_raw != cached_markdown_raw:
        markdown = github_api(markdown_raw)
        cache_page(markdown, markdown_raw, requested_post)
        return markdown

    return cached_markdown


def github_api(markdown_raw):
    """
    Turns raw markdown into stylized gfm, or 'Github Flavored Markdown"

    Args:
        markdown_raw (str)
        requested_post (str)

    Returns:
        r.text (str)
    """

    response = None
    api_url = 'https://api.github.com/'
    headers = {
        'content-type': 'text/plain; charset=UTF-8',
        'Authorization': f'token {app.config["GITHUB_OAUTH"]}'
    }

    data = {
        'text': markdown_raw,
        "mode": "gfm",
        "context": "github/gollum"
    }

    data = json.dumps(data)
    r = requests.post(url=api_url + 'markdown', headers=headers, data=data)

    if r.status_code != 200:
        response = f'Github API Error [Code {r.status_code}] ' \
                   f'Something went wrong when trying to convert text to markdown using Github API.'
        # raise Exception(response)
    else:
        print(r.status_code)
        response = r.text

    return response

