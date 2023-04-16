#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WebPage import Webpage


class IndexPage(Webpage):
    def __init__(self, url):
        super().__init__(url)
        self.indexlist = []
        
    def save_link(self,filename):
        with open (filename, "a", encoding="utf-8") as f:
            for i in self.get_index_list():
                f.write(i)
                f.write('\n')

    def get_index_list(self):
        return self.indexlist


class NatureIndexPage(IndexPage):
    def __init__(self, url):
        super().__init__(url)
        self.indexlist = []
        link_list_soup = self.get_soup().find_all('a', class_="c-card__link u-link-inherit") 
        for i in range(len(link_list_soup)):
            self.indexlist.append(link_list_soup[i].get("href"))


class NatureMethodsIndexPage(NatureIndexPage):
    pass


class NatureBiotechnologyIndexPage(NatureIndexPage):
    pass


class ScienceIndexPage(IndexPage):
    def __init__(self,url):
        super().__init__(url)
        self.indexlist = []
        self.link_list_soup = self.get_soup().find_all('a', class_="text-reset animation-underline")
        for i in range(len(self.link_list_soup)):
            self.indexlist.append(self.link_list_soup[i].get("href"))


class CellIndexPage(IndexPage):
    def __init__(self, url):
        super().__init__(url)
        self.indexlist = []
        self.link_list_soup = self.get_soup().find_all('div', class_="toc__item__body")
        for i in range(len(self.link_list_soup)):
            self.indexlist.append(self.link_list_soup[i].find('a').get("href"))
        

class ElsevierIndexPage(IndexPage):
    def __init__(self,url):
        super().__init__(url)
        self.indexlist = []
        self.link_list_soup = self.get_soup().find_all('a', class_="anchor article-content-title u-margin-xs-top u-margin-s-bottom anchor-default")
        for i in range(len(self.link_list_soup)):
            self.indexlist.append(self.link_list_soup[i].get("href"))


class UltramicroscopyIndexPage(ElsevierIndexPage):
    pass


class JSBIndexPage(ElsevierIndexPage):
    pass


