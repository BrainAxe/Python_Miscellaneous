"""Script to gather IMDB keywords from 2013's top grossing movies."""
import sys
from itertools import chain, izip
import requests
from bs4 import BeautifulSoup
import csv


year = raw_input("Enter the year: ")
URL = "http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=1&year=" + year + "," +year

def get_top_grossing_movie_links(url):
    """Return a list of tuples containing the top grossing movies name, rating, earning of your desire year according to IMDB page."""
    response = requests.get(url)
    movies_list = []
    movies_rank = []
    movies_earn = []
    
    for each_url in BeautifulSoup(response.text).select('.title a[href*="title"]'):
        movie_title = each_url.text
        if movie_title != 'X':
            movies_list.append(movie_title)
            
    for each_url1 in BeautifulSoup(response.text).select('.value'):
        movie_rating = each_url1.text
        movies_rank.append(movie_rating)
            
    for each_url2 in BeautifulSoup(response.text).select('.sort_col'):
        movie_earning = each_url2.text
        movies_earn.append(movie_earning)                         
    
    args = [i for i in chain.from_iterable(izip(movies_list, movies_rank, movies_earn))]
    return args



def main():
    """Main entry point for the script."""
    movies = get_top_grossing_movie_links(URL)
    with open('output.csv', 'w') as output:
        csvwriter = csv.writer(output)
        #csvwriter.writerow(movies) ''' All output in one row'''
        for title in movies:
            csvwriter.writerow([title]) 
            
        output.close()
        
            
if __name__ == '__main__':
    sys.exit(main())
