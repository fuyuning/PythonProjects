#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-25 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :spider2.py
#@Software  :PyCharm
import re
from urllib import request


#爬虫类
class Spider(object):
    #生成书的网址尾坠
    @staticmethod
    def make_root_url():
        # 生成网址列表
        first_pattern = '<div class="pagination[\s\S]*?<strong>([\s\S]*?)</div>'
        page_pattern = '<a href="([\s\S]*?)">'
        url_pattern = '<div class="col-sm-3 col[\s\S]*?<a href="([\s\S]*?)"'
        url = 'http://d81fb43e-d.parkone.cn'
        html = request.urlopen(url).read()
        html = str(html, encoding="utf-8")
        #第一次获取网页
        html = re.findall(first_pattern, html)
        #得到分页网址
        part_urls = []
        for _ in html:
            page_urls = re.findall(page_pattern, _)
            for page_url in page_urls:
                page_url = url + page_url
                part_urls.append(page_url)
            part_urls.append(url)
        book_urls = []
        for _ in part_urls:
            html = request.urlopen(_).read()
            html = str(html, encoding="utf-8")
            book_url = re.findall(url_pattern, html)
            book_urls += book_url
        urls = []
        for _ in book_urls:
            final_url = url + _
            urls.append(final_url)
        print(urls)
        #TODO 未解决问题，图书不存在
        #urls.remove('http://d81fb43e-d.parkone.cn/book/132')
        urls.remove('http://d81fb43e-d.parkone.cn/book/144')
        urls.remove('http://d81fb43e-d.parkone.cn/book/237')
        urls.remove('http://d81fb43e-d.parkone.cn/book/240')
        # TODO 未解决问题，下载地址与正常正则不符合是<li>
        urls.remove('http://d81fb43e-d.parkone.cn/book/198')
        urls.remove('http://d81fb43e-d.parkone.cn/book/199')
        urls.remove('http://d81fb43e-d.parkone.cn/book/200')
        return urls

    #获取全文
    @classmethod
    def fetch_content(cls, urls):
        html_s = []
        for url in urls:
            #获取html
            uri = request.urlopen(url)
            html = uri.read()
            #转码
            html = str(html, encoding="utf-8")
            html_s.append(html)
        return html_s

    #解析
    @staticmethod
    def analysis(html):
        books = []
        for _ in html:
            name_pattern = '<h2>([\s\S]*?)</h2>'
            author_pattern = '<a href="/author/[0-9]*">([\s\S]*?)</a>'
            language_pattern = 'label-default">([\s\S]*?)</span>'
            star_pattern = 'glyphicon glyphicon-star good'
            publish_pattern = '<span>(出版社:[\s\S]*?)</span>'
            public_time_pattern = '<p>(出版日期:[\s\S]*?) </p>'
            description_pattern = 'description">([\s\S]*?)</p>'
            download_pattern = '下载[\s\S]*?<a href="([\s\S]*?)" id="btnGroupDrop1pdf"'
            big_pattern = '</span>PDF \(([\s\S]*?)\)'
            name = re.findall(name_pattern, _)
            author = re.findall(author_pattern, _)
            language = re.findall(language_pattern, _)
            star = len(re.findall(star_pattern, _))
            publish = re.findall(publish_pattern, _)
            public_time = re.findall(public_time_pattern, _)
            description = re.findall(description_pattern, _)
            download = re.findall(download_pattern, _)
            if download is not None:
                download = 'http://d81fb43e-d.parkone.cn' + download[0]
            big = re.findall(big_pattern, _)
            book = {'name': name, 'author': author, 'language': language, 'star': star,
                    'publish': publish, 'public_time': public_time, 'description': description,
                    'download': download, 'big': big
                    }
            books.append(book)

        return books

    @staticmethod
    def show_books(books):
        for _ in books:
            print(_)
            print('-------------------------------------------------------------------------------------')


#main方法
def main():
    spider = Spider()
    #网址列表
    urls = spider.make_root_url()
    #print(urls)
    html_s = spider.fetch_content(urls)
    books = spider.analysis(html_s)
    spider.show_books(books)
    pass


if __name__ == '__main__':
    main()
