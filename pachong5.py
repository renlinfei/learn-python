import requests
import re

url = 'http://www.cnu.cc/inspirationPage/recent-110'
content = requests.get(url).text


# <img src="http://imgoss.cnu.cc/2204/28/431d786b730e3e26ba400a68603cad34.jpg?width=1056&amp;height=704&x-oss-process=style/flow280" alt="绿 | 色彩大师Harry Gruyaert">
#
# print(content)
pattern = re.compile(r'<img src="(.*?)".*?alt="(.*?)"', re.S)
results = re.findall(pattern, content)
# print(results)
for res in results:
    url_path, alt_text = res
    print(re.sub(r'\?.*', '', url_path), alt_text)
