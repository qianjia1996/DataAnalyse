'''
爬虫：
自动获取互联网信息的程序
利用互联网数据进行分析/开发产品
爬虫基本架构：
URL管理模块
    URL进行管理
    防止重复爬取或循环指向
    set数据结构/数据表/缓存数据库
网页下载模块
    将URL对应的网页下载到本地或读入内存
    erllib/requests模块
    response = urllib.request.urlopen(url)
    response.getcode()
    response.read()
网页解析模块
    解析网页下载模块中的URL，处理或保存数据
'''
# Python 3.x
import urllib.request

test_url = "http://www.google.com"

#URL下载模块
response = urllib.request.urlopen(test_url)
print(response.getcode()) # 200 表示访问成功
print(response.read())

'''
URL下载模块：
    request访问/Cookie访问
网页解析模块：
    爬取数据
    实现方式：
        正则表达式：字符串
        html.parser/BeautifulSoup结构化的网页解析/lxml
    DOM树形结构

'''