import os
import urllib
import requests
from bs4 import BeautifulSoup

def get_img():
	url = raw_input("Enter url: ")
	if 'www.' in url:
		url = url.replace('www.', "")
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml")
	dir_name = url.split("/")[2]
	os.mkdir(dir_name)
	os.chdir(dir_name)
	images = [img for img in soup.findAll('img')]
	print "Total " + str(len(images)) + "  images found."
	img_links = [each.get('src') for each in images]
	for link in img_links:
		print link
		li = link.split('/')[0]
		if li != "http:":
			link = "http:" + link
		fname = link.split('/')[-1]
		urllib.urlretrieve(link, fname)

	print "Download Complete!!!"



if __name__ == '__main__':
	get_img()