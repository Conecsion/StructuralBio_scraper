#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ArticlePage import JSBArticlePage
from IndexPage import *
import ArticlePage
import IndexPage
import argparse
import os


def save_links(idx_dir='/home/shaodi/Work/spider/source_idx', output_dir='./urls'):
    idx_files = [f for f in os.listdir(idx_dir)]
    for idx_file in idx_files:
        if "Journal of Structural Biology" in idx_file:
            journal = 'JSB'
        elif "Cell" in idx_file:
            journal = 'Cell'
        elif "Science" in idx_file:
            journal = "Science"
        elif "Ultramicroscopy" in idx_file:
            journal = 'Ultramicroscopy'
        elif 'Nature Biotechnology' in idx_file:
            journal = 'NatureBiotechnology'
        elif 'Nature Methods' in idx_file:
            journal = 'NatureMethods'
        else:
            journal = 'Nature'
        idx_path = os.path.join(idx_dir, idx_file)
        idx = eval("IndexPage." + journal + "IndexPage" + "('" + idx_path +
                   "')")
        filename = journal + "_urls"
        filename = os.path.join(output_dir, filename)
        idx.save_link(filename)


def write_output(input_dir="/home/shaodi/Work/spider/articlepages", output_dir='./output/'):
    htmls = [f for f in os.listdir(input_dir)]
    for html in htmls:
        html_path = os.path.join(input_dir, html)
        if "Journal of Structural Biology" in html:
            journal = 'JSB'
        elif "Cell" in html:
            journal = 'Cell'
        elif "Science" in html:
            journal = "Science"
        elif "Ultramicroscopy" in html:
            journal = 'Ultramicroscopy'
        elif 'Nature Biotechnology' in html:
            journal = 'NatureBiotechnology'
        elif 'Nature Methods' in html:
            journal = 'NatureMethods'
        else:
            journal = 'Nature'

        parser = eval("ArticlePage." + journal + 'ArticlePage' + '("' + html_path + '")')
        filename = journal + '.txt'
        filename = os.path.join(output_dir, filename)
        parser.save(filename)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-l', '--save_links', action='store_true')
    argparser.add_argument('-p', '--save_pages', action='store_true')
    args = argparser.parse_args()
    if args.save_links:
        save_links()
    elif args.save_pages:
        write_output()
