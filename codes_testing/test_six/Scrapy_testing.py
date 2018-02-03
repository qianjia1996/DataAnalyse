'''
Scrapy:
开源的爬虫框架，不同包
快速强大
易扩展，添加新的功能模块
用户群
Scrapy抓取过程：
    使用start_urls作为初始URL生成request，默认将parse、作为他的回调函数
    在parse函数中解析目标url
Scrapy高级特性：
    内置数据抽取器css/xpath/re
    交互式控制台用于调试
    结果输出的格式支持
    自动处理编码
    支持自定义扩展
    Spiders-->Scrapy Engine-->Scheduler-->Internet-->Downloader-->Item Pipeline
Scrapy使用过程：
    pip install scrapy
    创建工程
    定义Item，构造爬取的对象---可选
    编写Spider，爬虫主体、、
    编写配置和Pipeline，用于处理爬取的结果---可选
    执行爬虫
'''
