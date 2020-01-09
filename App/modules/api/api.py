import requests
import json


def github_markdown(markdown_raw):
    api_url = 'https://api.github.com/'
    headers = {'content-type': 'text/plain; charset=UTF-8'}

    data = {
        'text': markdown_raw,
        "mode": "gfm",
        "context": "github/gollum"
    }

    data = json.dumps(data)
    r = requests.post(url=api_url + 'markdown', headers=headers, data=data)

    return r.text


