#!/usr/bin/python3
import imdb

__imdb_api = imdb.IMDb()

def __get_top_movies():
    return __imdb_api.get_top250_movies()

def __get_movie_details(movie):
    __imdb_api.update(movie, info=['plot'])

def main():
    top_movies = __get_top_movies()
    for movie in top_movies:
        __get_movie_details(movie)
        print(movie.current_info)
        print(movie['plot'][0])
        print(movie['synopsis'][0])

if __name__ == "__main__": main()

