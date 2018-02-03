'''
BeautifulSoup解析网页
用于解析HTML和XML
pip install beautifulsoup4
import bs4
步骤：
    创建bs对象
        bs= BeautifulSoup(
            url,
            html_parser 指定解析器
            encoding  指定编码形式
        ）
    查找节点
    获取节点信息 node  node.name
    异常处理
        网络资源或URL经常变动
'''

from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen("http://www.baidu.com")
bs_obj = BeautifulSoup(html, 'html.parser', from_encoding='utf-8');
print("title tag: ", bs_obj.title)


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

#创建对象
bs_obj = BeautifulSoup(html_doc, 'html.parser')

#按类型查找节点

# 提取所有链接
print('1. 提取所有链接')
link_list = bs_obj.find_all('a')
for link in link_list:
    print(link.name, link['href'], link.get_text())

#按属性查找节点
print('2. 提取一条链接')
link = bs_obj.find('a', id='link2')
print(link.name, link['href'], link.get_text())

# 再提取一条链接
print('3. 再提取一条链接')
link = bs_obj.find('a', class_='sister')  #class加下划线
print(link.name, link['href'], link.get_text())

# 服务器和URL的异常处理
try:
    html = urllib.request.urlopen("http://www.wandu.com")
except Exception as e:
    print(e)

# HTML标签访问异常处理
try:
    tag_content = bs_obj.title.yy_tag
    #tag_content = bs_obj.xx_tag.yy_tag
except AttributeError as e:
    print("xx_tag 标签不存在")
else:
    if tag_content is None:
        print("yy_tag 标签不存在")
    else:
        print(tag_content)

#创建一个完整的函数处理title

'''
使用CSS方式/正则表达式
保存解析的内容
DOM数形结构
    children 只返回孩子节点
    desecdants 只返回子孙节点
    next_siblings 返回下一个同辈节点
    previous_siblings 返回上一个同辈节点
    parent 返回父亲节点
'''