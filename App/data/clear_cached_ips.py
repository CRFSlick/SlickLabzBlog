import json

view_log = json.loads(open('views.json', 'r').read())
for post in view_log:
    post['ips'] = []
open('views.json', 'w+').write(json.dumps(view_log, indent=4))

print('Done')