import requests
from bs4 import BeautifulSoup
import json

stations = {}
file = open('codes.json','w')

for i in range(1,41):
	url = 'http://irfca.org/apps/station_codes?page='+str(i)
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	table = soup.find_all(class_='zebra-striped')[0]
	trs = table.find_all('tr')[1:]
	for tr in trs:
		#stations[tr.find_all('td')[0].text] = tr.find_all('td')[1].text
		stations.update({tr.find_all('td')[0].text : tr.find_all('td')[1].text})
	print("Working on page " +str(i))	
file.write(json.dumps(stations))	
file.close()
