import urllib.request
from bs4 import BeautifulSoup

# find()
html = urllib.request.urlopen("https://www.amazon.cn/gp/bestsellers/books/ref=br_bsl_smr/456-4063020-4086765?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-bestsellers-2&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_t=36701&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_i=desktop")
bs_obj = BeautifulSoup(html, 'lxml')

nav = bs_obj.find("span", {"class" : "nav-a-content"})
print(nav.get_text())

# findAll()
html = urllib.request.urlopen("https://www.amazon.cn/gp/bestsellers/books/ref=br_bsl_smr/456-4063020-4086765?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-bestsellers-2&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_t=36701&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_i=desktop")
bs_obj = BeautifulSoup(html, 'lxml')

nav_list = bs_obj.findAll("span", {"class" : "nav-a-content"})   #CSS
for nav in nav_list:
    print(nav.get_text())

nav_name_list = [nav.get_text() for nav in nav_list]

# 保存到文件中
with open('./output.txt', 'w', encoding='utf-8') as f:
    for nav_name in nav_name_list:
        f.write('{}\n'.format(nav_name))


# children
html = urllib.request.urlopen("http://www.pythonscraping.com/pages/page3.html")
bs_obj = BeautifulSoup(html, 'lxml')
for child in bs_obj.find("table",{"id":"giftList"}).children:
    print(child)

# descendants
html = urllib.request.urlopen("http://www.pythonscraping.com/pages/page3.html")
bs_obj = BeautifulSoup(html, 'lxml')
for child in bs_obj.find("table",{"id":"giftList"}).descendants:
    print(child)

'''-------等等------'''

'''-----正则表达式-----'''
#RegexPal验证正则表达式

#电子邮箱验证
import re
#建立规则  字符串  基本语法
pattern = re.compile(r'[A-Za-z0-9._+]+@[A-Za-z]+\.(com|org|edu|net)')
match = pattern.match('bliang33@csu.edu.au')

if match:
    print(match.group())
else:
    print('非法的邮箱地址！')

#使用正则表达式查找节点
import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen("http://www.pythonscraping.com/pages/page3.html")
bs_obj = BeautifulSoup(html, 'lxml', from_encoding='uf-8')
images = bs_obj.findAll("img", {"src":re.compile(r"\.\./img/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
