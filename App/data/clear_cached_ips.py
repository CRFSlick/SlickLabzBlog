"""
This file is run when you want to clear the cached IP's so that a following visit from that IP will result in an
additional view for that page. Otherwise, a person from a given IP can only contribute 1 view to a page.
"""

import json

view_log = json.loads(open('views.json', 'r').read())
for post in view_log:
    post['ips'] = []
open('views.json', 'w+').write(json.dumps(view_log, indent=4))

print('Done')
