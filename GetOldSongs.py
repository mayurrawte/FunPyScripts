import requests
from bs4 import BeautifulSoup

url = 'http://songspkband.in/top-50-old-bollywood-songs-download/'
soup = BeautifulSoup(requests.get(url).content,'html.parser')
songlist = soup.table.find_all('a')
for song in songlist:
	songlink = song.get('href')
	songname = songlink[songlink.rfind('/')+1:len(songlink)]
	songname = songname.replace('%20',' ')
	print('Downloading '+songname+'...........')
	actualsong = requests.get(songlink)
	with open(songname,'wb') as songfile:
		songfile.write(actualsong.content)
	print('Downloaded '+songname +' ;) ')



