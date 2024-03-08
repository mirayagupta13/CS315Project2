import json
with open('raw_tiktokData/Sec2Gr1_77783.json') as fin:
    data = json.load(fin)

urls = [entry['Link'] for entry in data['VideoList']]

import pyktok as pyk
pyk.specify_browser('chrome')
pyk.save_tiktok_multi_urls(urls, True, 'tiktok_data.csv', 5)


