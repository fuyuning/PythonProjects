#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-25 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :spider2.py
#@Software  :PyCharm
import re
import sys
from urllib import request


#爬虫类
class Spider(object):
    #各部分正则表达式
    index_url = 'http://d81fb43e-d.parkone.cn'
    index_pattern = '<div class="pagination[\s\S]*?<strong>([\s\S]*?)</div>'
    root_pattern = '<a href="([\s\S]*?)">'
    url_pattern = '<div class="col-sm-3 col[\s\S]*?<a href="([\s\S]*?)"'
    name_pattern = '<h2>([\s\S]*?)</h2>'
    author_pattern = '<a href="/author/[0-9]*">([\s\S]*?)</a>'
    language_pattern = 'label-default">([\s\S]*?)</span>'
    star_pattern = 'glyphicon glyphicon-star good'
    publish_pattern = '<span>(出版社:[\s\S]*?)</span>'
    public_time_pattern = '<p>(出版日期:[\s\S]*?) </p>'
    description_pattern = 'description">([\s\S]*?)</p>'
    download_pattern = '下载[\s\S]*?<a href="([\s\S]*?)" id="btnGroupDrop1pdf"'
    download_list_pattern = '<ul class="dropdown-menu"[\s\S]*?<li><a href="([\s\S]*?)">PDF'
    space_pattern = '</span>PDF \(([\s\S]*?)\)'

    #通过url获取内容
    @staticmethod
    def _get_content(url):
        content = request.urlopen(url).read()
        content = content.decode('utf-8')
        return content

    #获取初始网页
    def _get_index_content(self):
        index_content = Spider._get_content(self.index_url)
        return index_content

    #获取分页的url列表
    def _get_page_url_list(self, content):
        page_url_list = [self.index_url]
        root_content = re.findall(self.index_pattern, content)
        page_content_list = re.findall(self.root_pattern, root_content[0])
        for page_part_url in page_content_list:
            page_url = self.index_url + page_part_url
            page_url_list.append(page_url)
        return page_url_list

    #获取书的url列表
    def _get_book_urls(self, page_url):
        page_content = Spider._get_content(page_url)
        book_urls = re.findall(self.url_pattern, page_content)
        book_urls = [self.index_url + book_url for book_url in book_urls]
        return book_urls

    #解析页面信息
    def _analysis(self, book_url):
        book_content = Spider._get_content(book_url)
        name = re.findall(self.name_pattern, book_content)
        author = re.findall(self.author_pattern, book_content)
        language = re.findall(self.language_pattern, book_content)
        star = len(re.findall(self.star_pattern, book_content))
        publish = re.findall(self.publish_pattern, book_content)
        public_time = re.findall(self.public_time_pattern, book_content)
        description = re.findall(self.description_pattern, book_content)
        download = re.findall(self.download_pattern, book_content)
        if not download:
            download = re.findall(self.download_list_pattern, book_content)
        download = self.index_url + download[0]
        big = re.findall(self.space_pattern, book_content)
        book = {'name': name, 'author': author, 'language': language, 'star': star,
                'publish': publish, 'public_time': public_time, 'description': description,
                'download': download, 'big': big
                }
        return book

    #run方法
    def run(self):
        index_content = self._get_index_content()
        page_urls = self._get_page_url_list(index_content)
        for page_url in page_urls:
            book_urls = self._get_book_urls(page_url)
            for book_url in book_urls:
                book = self._analysis(book_url)
                print(book)
                print('_______________________________________________________________________')


if __name__ == '__main__':

    spider = Spider()
    spider.run()
