import os

c_dir = os.getcwd()
file = open("list.txt",'w')
d = raw_input('Enter the directory address: ')
i=1
for f in os.listdir(d):
	if os.path.isdir(os.path.join(d, f)):
		s1 = str(i) + ". " + f + "\n"
		file.write(s1)
		f1 = d + "/" + f
		for f2 in os.listdir(f1):
			s1 = "\t *" + f2 + "\n"
			file.write(s1)
	else:
		s = str(i) + ". " + f + "\n"
		file.write(s)
	i+=1
os.chdir(c_dir)
file.close()
