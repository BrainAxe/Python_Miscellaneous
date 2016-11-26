import requests
from bs4 import BeautifulSoup


def main():
	year = raw_input("Enter the year: ")
	url = "http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=1&year=" + year + "," +year

	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml") 


	movies_list = []
	movies_rank = []
	movies_earn = []


	contents = soup.find_all('div', {"class": "lister-item-content"})



	for item in contents:
		movies_list.append(item.find('a').text)
		movies_rank.append(item.find('strong').text)

		earns = item.find_all('span',{"name": "nv"})
		movies_earn.append(earns[1].text) 
		
	

	print "\n\n{:44} {:16} {}".format("Movie Name", "Ranking", "Earning")
	print "="*70

	All = ''.join('{:44} -->  {:6}  --> {}\n'.format(*t) for t in zip(movies_list, movies_rank, movies_earn))

	print All

	

	


if __name__=="__main__":
	main()
