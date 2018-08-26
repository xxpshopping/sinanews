import re
import urllib2
from bs4 import BeautifulSoup

__author__ = 'xxp'
url='http://mil.news.sina.com.cn/china/2017-08-15/doc-ifyixias0895721.shtml'
response=urllib2.urlopen(url)
html_cont=response.read()
soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
links = soup.find_all('a',href=re.compile(r"http://news.sina.com.cn/"))
new_urls=set()
for link in links:
    new_url=link['href']
    #new_full_url=urlparse.urljoin(page_url,new_url)
    new_urls.add(new_url)
    print new_url
res_data={}
res_data['url']=url


title_node=soup.find('h1',id="main_title")
res_data['title']=title_node.get_text()


        #<div class="lemma-summary" label-module="lemmaSummary">
        #<div class="content_wrappr_left" style="width: 680px;">
        #<div class="content" id="artibody" data-sudaclick="blk_content">
summary_node=soup.find('div',class_="content").find_all('p')

for a in summary_node:

    print a.get_text()

print res_data['url'],res_data['title']
