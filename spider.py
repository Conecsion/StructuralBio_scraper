#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os.path


class Webpage:
    def __init__(self, url):
        if os.path.isabs(url):
            with open(url, "r") as html:
                self.__soup = BeautifulSoup(html, 'lxml')
        else:
            response = requests.get(url)
            self.__soup = BeautifulSoup(response.content, 'lxml')
        self.__content = self.__soup.prettify()

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.get_content())

    def get_soup(self):
        return self.__soup

    def get_content(self):
        return self.__content


class IndexPage(Webpage):
    def __init__(self, url):
        super().__init__(url)


class ArticlePage(Webpage):
    def __init__(self, url):
        super().__init__(url)


class NatureIndexPage(IndexPage):
    def __init__(self, url):
        super().__init__(url)


class NatureArticlePage(ArticlePage):
    def __init__(self, url):
        super().__init__(url)
        self.date = self.get_soup().find('time').string
        self.title = self.get_soup().find_all(
            "h1", class_="c-article-title")[0].string
        self.__author_list_soup = self.get_soup().find_all(
            "a", attrs={"data-test": "author-name"})
        self.first_author = self.__author_list_soup[0].text
        self.abstract = self.get_soup().find_all(
            'div', id="Abs1-content")[0].find_all('p')[0].text
        self.doi = self.get_soup().find(
            'li',
            class_=
            "c-bibliographic-information__list-item c-bibliographic-information__list-item--doi"
        ).find('p').text
        self.__figure_soup = self.get_soup().find('picture')
        if self.__figure_soup != None:
            self.figure_url = "https:" + self.__figure_soup.find('source').get(
                'srcset')


class ScienceAtriclePage(ArticlePage):
    def __init__(self, url):
        super().__init__(url)
        self.title = self.get_soup().find('h1', property="name").text
        self.date = self.get_soup().find('span', property="datePublished").text
        self.first_author = self.get_soup().find('span', property='author').find('a',href='#con1').text
        self.abstract = self.get_soup().find('div', role='paragraph').text


class CellArticlePage(ArticlePage):
    def __init__(self,url):
        super().__init__(url)
        self.abstract = self.get_soup().find_all("div", class_="section-paragraph")[1].text
        self.first_author = self.get_soup().find_all("a", attrs={"aria-controls": "au1"})[0].text
        self.date = self.get_soup().find("span", class_="article-header__publish-date__value").text
        self.title = self.get_soup().find_all("h1")[0].text
        self.doi = "DOI: " + self.get_soup().find("a", class_="article-header__doi__value").text


class UltramicroscopyArticlePage(ArticlePage):
    def __init__(self,url):
        super().__init__(url)
        self.title = self.get_soup().find("span", class_="title-text").text
        self.date = self.get_soup().find('div', class_='text-xs').text
        self.first_author = self.get_soup().find('span', class_="react-xocs-alternative-link").text
        self.abstract = self.get_soup().find('p').text


class JSBArticlePage(UltramicroscopyArticlePage):
    def __init__(self,url):
        super().__init__(url)


class NatureMethodsArticlePage(NatureArticlePage):
    def __init__(self,url):
        super().__init__(url)


class NatureBiotechnology(NatureArticlePage):
    def __init__(self,url):
        super().__init__(url)


web = ScienceAtriclePage("/home/shaodi/Downloads/Germline-encoded amino acid–binding motifs drive immunodominant public antibody responses _ Science (2023_4_11 22_04_44).html")
print(web.first_author)
print(web.date)
print(web.title)
print(web.abstract)
#  print(web.get_content())
web.save("ultra.txt")
#  print(web.doi)


#  web = ScienceAtriclePage("https://www.science.org/doi/10.1126/science.add0089")



#  print("%s\n%s\n%s\n%s\n%s\n%s" % (web.date, web.title, web.first_author,
#  web.abstract, web.doi, web.figure_url))
