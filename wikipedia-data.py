#!/usr/bin/python3
import argparse
import wikipedia

def __get_parser():
    parser = argparse.ArgumentParser(description='Wikipedia Data')
    parser.add_argument('-s', '--search', help='Search term', required=True)
    parser.add_argument('-c', '--count', help='Result count', type=int, default=5, required=False)

    return parser

def __get_arguments():
    parser = __get_parser()
    return vars(parser.parse_args())

def __get_search_results(arguments):
    search = arguments['search']
    count = arguments['count']
    return wikipedia.search(search, results=count, suggestion=True)

def __get_pages(arguments):
    search_results = __get_search_results(arguments)
    titles = search_results[0]
    return [wikipedia.page(title=title, auto_suggest=False, redirect=True, preload=True) for title in titles]

def main():
    args = __get_arguments()
    pages = __get_pages(args)

    for page in pages:
        print('==============')
        print(page.links)
        print(page.summary)

if __name__ == "__main__": main()

