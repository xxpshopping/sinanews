# -*- coding:UTF-8 -*-
from sinanews import url_manager
from sinanews import html_downloader
from sinanews import html_parser
from sinanews import html_outputer

__author__ = 'xxp'




class SpideMain(object):
    #初始化对象
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)#把初始URL添加进URL管理器
        while self.urls.has_new_url():#当URL管理器中有待爬取的URL

                new_url=self.urls.get_new_url()#获取当前爬取得URL
                print 'craw %d : %s'%(count,new_url)
                html_cont=self.downloader.download(new_url)#启动下载器下载页面
                new_urls,new_data=self.parser.parse(new_url,html_cont)#解析器解析页面数据得到新的URL列表，新的数据
                self.urls.add_new_urls(new_urls)#添加批量URL
                self.outputer.collect_data(new_data)


                if count==1000:
                    break

                count=count+1

        self.outputer.output_html()#收集好数据

if __name__=="_main_":
    root_url="http://news.sina.com.cn/"
    obj_spider=SpideMain()
    obj_spider.craw(root_url)
