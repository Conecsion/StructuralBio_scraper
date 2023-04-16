#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ArticlePage import JSBArticlePage
from IndexPage import *
from ArticlePage import *
from IndexPage import JSBIndexPage
import os


#  JSBInd1 = JSBIndexPage("/home/shaodi/Downloads/Journal of Structural Biology _ Vol 215, Issue 2, In progress (June 2023) _ ScienceDirect.com by Elsevier.html")
#  JSBInd1.save_link("JSB1.txt")


dir = "/home/shaodi/Downloads/jsb"
files = [f for f in os.listdir(dir)]
for file in files:
    #  html = os.path.join(dir,file)
    #  parser = JSBArticlePage(html)
    #  parser.save("JSB.txt")
    pass



