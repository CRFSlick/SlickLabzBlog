from App import app
import requests
import json


def get_data():
    api_url = 'https://api.github.com/'
    headers = {'content-type': 'text/plain; charset=UTF-8'}

    data = {
        'text': open(app.root_path + '\\posts\\blog.md', 'r').read(),
        "mode": "gfm",
        "context": "github/gollum"
    }

    data = json.dumps(data)
    r = requests.post(url=api_url + 'markdown', headers=headers, data=data)

    return r.text


