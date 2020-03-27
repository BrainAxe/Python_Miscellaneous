import os
import sqlite3
import operator
import platform
from collections import OrderedDict
import matplotlib.pyplot as plt


def parse(url):
	try:
		parsed_url_components = url.split('//')
		sublevel_split = parsed_url_components[1].split('/',1)
		domain = sublevel_split[0].replace("www.", "")
		return domain

	except IndexError:
		pass
		#print "URL format error!"


def analyze(results):
	prompt = input("[.] Type <c> to print or <p> to plot\n [>] ")

	if prompt == "c":
		for site, count in sites_count_sorted.items():
			print(site, count)

	elif prompt == "p":
		# plt.bar(range(len(results)), results.values(), align='edge')
		results2 = {}
		for i in results:
			if results[i]>200:
				results2[i] = results[i]

		plt.bar(range(len(results2)), results2.values(), align='edge')
		plt.xticks(rotation=45)
		plt.xticks(range(len(results2)), results2.keys())
		plt.show()

	else:
		print("[.] Uh?")
		quit()


def main():
	if platform.system() != "Linux":
		print("******************************")
		print("You are not using Linux System.\nWindows SUCKS")
		print("******************************")
		quit()
	print("Choose Web Browser:")
	print("1. Firefox")
	print("2. Chromium")
	print("3. Google Chrome")
	print("4. Exit")
	choice = int(input("Enter your choice: "))

	history_db = ""

	if choice == 1:
		base_path = os.path.join(os.path.expanduser('~') + "/.mozilla/firefox/")
		for files in os.listdir(base_path):
			if '.default' in files:
				file_path = os.path.join(base_path,files)
				history_db = os.path.join(file_path,'places.sqlite')
				break

		sql = "SELECT url, visit_count FROM moz_places;"


	elif choice == 2:
		history_db = os.path.expanduser('~') + "/.config/chromium/Default/History"
		sql = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"

	elif choice == 3:
		history_db = os.path.expanduser('~') + "/.config/google-chrome/Default/History"
		sql = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"

	elif choice == 4:
		quit()

	else:
		print("Wrong Input!!")



	con = sqlite3.connect(history_db)
	con = con.cursor()
	con.execute(sql)
	results = con.fetchall()

	sites_count = {}

	for url, count in results:
		url = parse(url)
		if url in sites_count:
			sites_count[url] += 1

		else:
			sites_count[url] = 1

	global sites_count_sorted

	sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))

	analyze(sites_count_sorted)




if __name__ == '__main__':
	main()