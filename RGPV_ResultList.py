import BeautifulSoup as bs
import cv2 
import requests
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from StringIO import StringIO
import time

starting_no = raw_input("starting roll number")
ending_no = raw_input("ending roll number")
sem = raw_input("semester")
starting_init = starting_no[:6]
starting_last = starting_no[6:]
ending_init = ending_no[:6]
ending_last = ending_no[6:]

rollnos =[starting_init+str(x) for x in range(int(starting_last),int(ending_last))]

for rollno in rollnos:
	time.sleep(3)
	r = requests.get("http://result.rgpv.ac.in/Result/BErslt.aspx")
	if r.status_code == 200:
		soup = bs.BeautifulSoup(r.text)
		eventvalidation = soup.find(id="__EVENTVALIDATION").get('value')
		viewstate =  soup.find(id="__VIEWSTATE").get('value')
		Captcha = soup.find(alt="Captcha").get('src')
		Captcha_src = requests.get("http://result.rgpv.ac.in/Result/"+Captcha)
		im = Image.open(StringIO(Captcha_src.content)) # the second one
		im = im.filter(ImageFilter.MedianFilter())
		enhancer = ImageEnhance.Contrast(im)
		im = enhancer.enhance(2)
		im = im.convert('1')
		im.save('temp2.jpg')
		time.sleep(3)
		cap_text = pytesseract.image_to_string(Image.open('temp2.jpg'))
		text = cap_text.replace(" ","")
		#print("\n\n\n\nCaptca image is "+text)
		if len(text) == 5:
			#rollno = raw_input("Enter Roll Number")
			time.sleep(3)
			formdata = { '__EVENTTARGET': '','__EVENTARGUMENT':'','__VIEWSTATE': viewstate, '__EVENTVALIDATION': eventvalidation,'ctl00$ContentPlaceHolder1$txtrollno':rollno,'ctl00$ContentPlaceHolder1$drpSemester':sem,'ctl00$ContentPlaceHolder1$rbtnlstSType':'G','ctl00$ContentPlaceHolder1$TextBox1':text,'ctl00$ContentPlaceHolder1$btnviewresult':'View Result'}
			result = requests.post("http://result.rgpv.ac.in/Result/BErslt.aspx",data=formdata,cookies=r.cookies)
			if result.status_code == 200:
				sp = bs.BeautifulSoup(result.text)
				try:
					print sp.find(id ='ctl00_ContentPlaceHolder1_lblNameGrading').text,
					print " -- ",
					print sp.find(id='ctl00_ContentPlaceHolder1_lblResultNewGrading').text,
					print " -- ",
					print sp.find(id='ctl00_ContentPlaceHolder1_lblSGPA').text
				except Exception:
					print Exception
		else:
			print "Escaped "+rollno 

