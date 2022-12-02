#!/usr/bin/python3

import requests
import pprint

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


url = 'https://techcrunch.com/wp-json/wp/v2/posts?after=2022-12-01%2000:00:00&page=2&_embed=true'

res = requests.get(url)

posts = res.json()

def formatted_print():
    for i in range(0, len(posts)):
        post = posts[i]

        _links = post['_links']
        _author = post['author']
        _date = post['date']
        _link = post['link']
        _title = post['title']['rendered']
        _except = post['excerpt']['rendered']
        print(_date)
        print(_title)
        print(f"{bcolors.OKBLUE}{_link}{bcolors.ENDC}")
        print("\n")

#pp.pprint(posts[0])
formatted_print()

