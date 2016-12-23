import os

directory = raw_input('Enter the directory location: ')
i = 1

with open("list.txt", 'w') as out:
	for item in os.listdir(directory):
		items = "{:2}. {}\n".format(i, item)
		out.write(items)
		i+=1