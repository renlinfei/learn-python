from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.prettify())

# 找到title标签
print(soup.title)
# title标签的内容
print(soup.title.string)

# 找到p标签
print(soup.p)

# 找到p标签对应的class
print(soup.p['class'])

# 找到第一个a标签
print(soup.a)

# 找到所有的a标签
print(soup.findAll('a'))
# 找到id为link3的标签
print(soup.findAll(id='link3'))

# 找到所有<a>标签的链接
for link in soup.findAll('a'):
    print(link.get('href'))

# 找到文档中所有文本内容
print(soup.getText())
