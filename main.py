#!/usr/bin/python3

import requests
import pprint
import time
from bs4 import BeautifulSoup


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

pp = pprint.PrettyPrinter(indent=2)


def get_posts():
    posts = []
    for i in range(1, 4):
        url = f'https://techcrunch.com/wp-json/wp/v2/posts?after=2022-12-01%2000:00:00&page={i}&_embed=true'
        res = requests.get(url)
        for post in res.json():
            posts.append(post)
    return posts


def get_current_time():
    seconds = time.time()
    local_time = time.ctime(seconds)
    formatted_local_time = str(local_time).replace(" ", "").replace(":", "")
    return formatted_local_time


def formatted_print(posts):
    # f.open(report_name)
    # report_name = f"~/dev/formatted_techchrunch/reports/report.html"
    for i in range(0, len(posts)):
        post = posts[i]

        _links = post['_links']
        _author = post['author']
        _date = post['date']
        _link = post['link']
        _title = post['title']['rendered']
        _except = post['excerpt']['rendered']
        _content = post['content']['rendered']
        print(f"{_date} | {_title}")
        print(f"{bcolors.OKBLUE}{_link}{bcolors.ENDC}")
        soup = BeautifulSoup(_content, "lxml")
        print(soup.get_text())
        print("\n")


if __name__ == '__main__':
    # pp.pprint(posts[0])
    # cur_time = get_current_time()
    posts = get_posts()
    formatted_print(posts)


