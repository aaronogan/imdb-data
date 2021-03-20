#!/usr/bin/python3
import argparse
import wikipedia

def main():
    parser = argparse.ArgumentParser(description='Wikipedia Data')
    parser.add_argument('-s', '--search', help='Search', required=True)

    args = vars(parser.parse_args())
    search = args['search']
    print(wikipedia.search(search))

if __name__ == "__main__": main()

