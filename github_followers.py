# -*- coding: utf-8 -*-
# @Author: rizwan
# @Date:   2018-11-23 16:40:43
# @Last Modified by:   Tanzim Rizwan
# @Last Modified time: 2020-03-27 12:32:52


import os
import requests
import platform


FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)



def check_new(flist):
	fdata = []
	Followers = []
	followers_file_path = os.path.join(BASE_DIR,'followers.txt')

	if os.path.exists(followers_file_path):
		with open(followers_file_path, 'r') as rfile:
			for line in rfile:
				line = line.strip()
				fdata.append(line)


	with open(followers_file_path, 'a') as wfile:
		for i in flist:
			if i in fdata:
				# print("Exists!!")
				pass
			else:
				Followers.append(i)
				wfile.write(i + '\n')



	if Followers:
		title = "New Follower!!!"
		sys_name = platform.system()
		if sys_name=="Linux":
			os.system('/usr/bin/notify-send " '+title+' " " '+'\n'.join(Followers)+' " ')
		else:
			print("******************************")
			print("You are not using Linux System.\nWindows SUCKS")
			print("******************************")
			for f in Followers:
				print(f)



def follower_list():
	username = "brainaxe"     #  <----- SET YOUR USERNAME HERE
	api = 'https://api.github.com/users/{}/followers'.format(username)
	r = requests.get(api)
	data = r.json()
	followers = []

	for i in data:
		follower = i['login']
		followers.append(follower)

	return followers


if __name__ == '__main__':
	flist = follower_list()
	check_new(flist)
