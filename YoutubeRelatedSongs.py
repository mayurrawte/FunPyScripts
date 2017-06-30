from bs4 import BeautifulSoup
import requests
from subprocess import call, Popen, PIPE
import os
import random
url = raw_input("Initial Youtube song url ")
noOfSongs = int(raw_input("Enter the number of Related songs to download : "))

while noOfSongs:
	command = "youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 "+ url
	call(command.split(), shell=False)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	command1 = "youtube-dl --get-filename "+url
	p = Popen(command1.split(), stdout=PIPE, stderr=PIPE)
	output, err = p.communicate()
	filename = output[:-1]
	filename = str(filename.replace(filename[-3:],'mp3'))
	files = os.listdir(os.getcwd())
	if filename in files:
		resultset = soup.find(id='watch-related')
		links = resultset.find_all('a')
		link = 'http://www.youtube.com'+links[random.randrange(2,len(links)-1)].get('href')
		url = link
	else:
		resultset = soup.find_all(class_='autoplay-bar')
		for a in resultset:
			link = 'http://www.youtube.com'
			link += a.find('a').get('href')
		url = link
	noOfSongs-=1


