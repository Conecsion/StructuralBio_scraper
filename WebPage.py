#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os.path
from abc import ABC, abstractclassmethod


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
