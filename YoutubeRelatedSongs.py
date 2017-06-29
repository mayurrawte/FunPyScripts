from bs4 import BeautifulSoup
import requests
from subprocess import call

url = raw_input("Initial Youtube song url ")
noOfSongs = int(raw_input("Enter the number of Related songs to download : "))

while noOfSongs:
	command = "youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 "+ url
	call(command.split(), shell=False)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	resultset = soup.find_all(class_='autoplay-bar')
	for a in resultset:
		link = 'http://www.youtube.com'
		link += a.find('a').get('href')
	url = link
	noOfSongs-=1

