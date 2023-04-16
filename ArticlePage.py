#!/usr/bin/env python
# -*- coding: utf-8 -*-
from WebPage import Webpage
from docx import Document


class ArticlePage(Webpage):
    def __init__(self, url):
        super().__init__(url)
        self.date = ''
        self.first_author = ''
        self.abstract = ''
        self.title = ''
    def save_to_docx(self,filename):
        document = Document()
    def save(self,filename):
        with open(filename,'a',encoding='utf-8') as f:
            f.write('----------------------------------------------------------------------------\n')
            f.write(f"{self.title} \n {self.date} \n {self.first_author} \n {self.abstract} \n")
            f.write('----------------------------------------------------------------------------\n\n\n')
            #  f.write(self.title)
            #  f.write('\n')
            #  f.write(self.date)
            #  f.write('\n')
            #  f.write(self.first_author)
            #  f.write('\n')
            #  f.write(self.abstract)
            #  f.write('\n')




class NatureArticlePage(ArticlePage):
    def __init__(self, url):
        super().__init__(url)
        try:
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
        except:
            print(f"{url} has failed")


class ScienceAtriclePage(ArticlePage):
    def __init__(self, url):
        super().__init__(url)
        try:
            self.title = self.get_soup().find('h1', property="name").text
            self.date = self.get_soup().find('span', property="datePublished").text
            self.first_author = self.get_soup().find('span', property='author').find('a',href='#con1').text
            self.abstract = self.get_soup().find('div', role='paragraph').text
        except:
            print(f"{url} has failed")


class CellArticlePage(ArticlePage):
    def __init__(self,url):
        super().__init__(url)
        try:
            self.abstract = self.get_soup().find_all("div", class_="section-paragraph")[1].text
            self.first_author = self.get_soup().find_all("a", attrs={"aria-controls": "au1"})[0].text
            self.date = self.get_soup().find("span", class_="article-header__publish-date__value").text
            self.title = self.get_soup().find_all("h1")[0].text
            self.doi = "DOI: " + self.get_soup().find("a", class_="article-header__doi__value").text
        except:
            print(f"{url} has failed")


class UltramicroscopyArticlePage(ArticlePage):
    def __init__(self,url):
        super().__init__(url)
        try:
            self.title = self.get_soup().find("span", class_="title-text").text
            self.date = self.get_soup().find('div', class_='text-xs').text
            self.first_author = self.get_soup().find('span', class_="react-xocs-alternative-link").text
            self.abstract = self.get_soup().find('p').text
        except:
            print(f"{url} has failed")


class JSBArticlePage(UltramicroscopyArticlePage):
    def __init__(self,url):
        super().__init__(url)


class NatureMethodsArticlePage(NatureArticlePage):
    def __init__(self,url):
        super().__init__(url)


class NatureBiotechnology(NatureArticlePage):
    def __init__(self,url):
        super().__init__(url)
