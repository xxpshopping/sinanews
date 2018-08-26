# -*- coding:UTF-8 -*-
from xml import etree

__author__ = 'xxp'
import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls=set() #存到列表里面

        #<a href="http://mil.news.sina.com.cn/china/2017-08-15/doc-ifyixias0895721.shtml?

        links = soup.find_all('a',href=re.compile(r"http://news.sina.com.cn/"))
        for link in links:
            new_url=link['href']
            #new_full_url=urlparse.urljoin(page_url,new_url)
            new_urls.add(new_url)
        return new_urls


    def __get_new_data(self, page_url, soup):
        res_data={}

        res_data['url']=page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        #<h1 id="main_title">印媒称中印边界会谈未实现 但两国海军将联合演习</h1>
        title_node=soup.find('h1',id="main_title")
        res_data['title']=title_node.get_text()


        #<div class="lemma-summary" label-module="lemmaSummary">
        #<div class="content_wrappr_left" style="width: 680px;">
        summary_node=soup.find('div',class_="content").find('p')
        res_data['summary']=summary_node.get_texy()

        return res_data

