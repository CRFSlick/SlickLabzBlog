import json


def get_post(data):
    start_tag = '{{ META START }}'
    end_tag = '{{ META END }}'
    index_1 = data.find(start_tag)
    index_2 = data.find(end_tag)

    if index_1 != -1 and index_2 != -1:
        metadata = json.loads(data[index_1 + len(start_tag):index_2])
        metadata['content'] = data[index_2 + len(end_tag):].strip()
        return metadata
