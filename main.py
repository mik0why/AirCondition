
import requests, json
from PIL import Image, ImageDraw, ImageFont
import cv2 as cv
import numpy as np
import os
import threading
import datetime

def get_key():
	key_file = open("key.txt")
	return key_file.readline().rstrip()


def get_average(lat1, long1, lat2, long2):
	#Getting an average air quality value in a region bounded by four points
	counter = 0 
	count_sum = 0
	address = "https://api.waqi.info/map/bounds/?latlng=" + str(lat1)  + "," + str(long1) + "," + str(lat2) + "," + str(long2) + "&token=" + get_key()
	response = requests.get(address)
	data = response.json()
	for eachEntry in data['data']:
		if eachEntry['aqi'] != "-":
			count_sum+=int(eachEntry['aqi'])
			counter+=1

	return count_sum / counter 
def det_pos(code):
	#Getting the right pixel value withing the range of a v-ship
	if(code==2):#dolnoslaskie
		return (100, 300)
	elif(code==4): #kpom
		return (150, 100)
	elif(code==6): #lubelskie
		return (360, 280)
	elif(code==8): #lubuskie
		return (50,150)
	elif(code==10): #ldz
		return (200,200)
	elif(code==12): #malopolskie
		return (250, 350)
	elif(code==14): #mazowieckie
		return (250, 150)
	elif(code==16): #opolskie
		return (140, 270)
	elif(code==18): #podkarpackie
		return (300, 300)
	elif(code==20): #podlaskie
		return (340, 120)
	elif(code == 22): #pomorskie
		return (150, 50)
	elif(code==24): #slaskie
		return ((180, 310))
	elif(code==26): #swietokrzyskie
		return (265, 270)
	elif(code==28): #war-maz
		return (245, 80)
	elif(code==30): #wlkp
		return (130, 170)
	elif(code ==32):
		return (100,100) #zpom
def color_image(isFirst, code, color) :
	#a method which calls the appropriate .png file to be modified 
	col_fill = [0,0,0]
	for i in col_fill:
		col_fill[i] = color[i]

	if isFirst == 0:
		im = Image.open("2867.png") #change: need to specify file
	else:
		im = Image.open("modified_image.png")
   	ImageDraw.floodfill(im, xy=det_pos(code), value=color)
   	im.save("modified_image.png")

   	os.system('clear')
   	print str(code/float(32)* 100) +  " %" #wipe out the prev percentage
   	return
def set_color(qual_val, vals):
	#determining the correct color to fill each v-ship with 
	if qual_val < vals[0]: #35
		value = (0, 100, 0, 255) #dark green
	elif qual_val < vals[1]: #70
		value = (50, 205, 50, 255)
	elif qual_val < vals[2]: #100
		value = (127, 255, 0, 255)
	elif qual_val < vals[3]: #150
		value = (255, 255, 153, 255)
	elif qual_val < vals[4]: #200 (prob should be like 130)
		value = (255, 255, 0, 255)
	else:
		value = (255, 0, 0)

	return value
def add_labels(vals):
	#adds labels to the image color description.
	#can be further extended by specifying the designated colors here
	im = Image.open("modified_image.png")
	draw = ImageDraw.Draw(im)
	draw.text((60,8), "Average Air Quality Value in Each Region of Poland", fill = (0,0,0))
	draw.text((18,340), " >" , fill = (0,0,0))
	draw.text((39,340), str(vals[1]), fill = (0,0,0))
	draw.text((60,340), str(vals[2]), fill = (0,0,0))
	draw.text((81,340), str(vals[3]), fill = (0,0,0))
	draw.text((102,340), str(vals[4]), fill = (0,0,0))
	draw.text((122,340), "<", fill = (0,0,0))
	draw.text((20, 387), "last updated: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), fill = (0,0,0))
	im.save("modified_image.png")
def call_methods():
	#the actual execution of the program loop
	threading.Timer(60.0, call_methods).start()
	counter = 0
	values = [30,35,40,50,60]
	color_image(0, 2,set_color(get_average(50.229722,14.816667,51.3,17.204722), values)) #dsln
	color_image(1, 4, set_color(get_average(52.670894645899565, 17.600410449865933,53.58205739916945, 19.170625129485426), values))
	color_image(1, 6, set_color(get_average(50.42390940147702, 21.78010536346148,52.10378467872945, 23.63449808103382), values))
	color_image(1, 8, set_color(get_average(51.39449400842635, 14.308934079995923, 53.08871594766961,16.37557164845528), values))
	color_image(1, 10, set_color(get_average(51.18150909626326, 18.18683141184597,52.26353814929127, 20.03340487171147), values))
	color_image(1, 12, set_color(get_average(49.60826588906249, 19.40440827755731, 50.34063461470439,21.15431511476454), values))
	color_image(1, 14, set_color(get_average(51.4,19.7, 53.11147671376918,  21.623892136292895), values))#mazowieckie
	color_image(1, 16, set_color(get_average(50.04839162590399, 17.176222927347037, 51.06998310093026, 18.661610922571764), values))#opolskie
	color_image(1, 18, set_color(get_average(48.97992839121357 ,21.105378206426312,  50.65127168311046, 24.032757131542073), values))#podkarpackie
	color_image(1, 20, set_color(get_average(52.83436534325404, 21.835014855981125,  53.669118069294484, 23.872753547386487), values))#podlaskie
	color_image(1, 22, set_color(get_average(53.592244125458116, 16.94100375473024, 54.88141021518485, 19.418373146834785), values))#pomorskie
	color_image(1, 24, set_color(get_average(49.46641028045689, 18.565244878369306, 50.4558250975039, 19.34560596141908), values))#slaskie
	color_image(1, 26, set_color(get_average(50.286250462857886 ,19.874726537130204, 51.24513703393278, 21.78716074066059), values))#swietokrzyskie
	color_image(1, 28, (50, 205, 50, 255))#war-maz (need to set the color manually)
	color_image(1, 30, set_color(get_average( 51.52624386672461, 16.305484426065646, 53.12541587605423418, 18.301106695225065), values))#wlkp
	color_image(1, 32, set_color(get_average(52.614789312582616, 14.076508253072798 , 54.58174066414152, 16.5988760639136), values))#zach-pom
	add_labels(values)
	im = Image.open("modified_image.png")
	im.show()
call_methods()
#still need to close an image once displayed
#ed45c2573a811b8a94bee86f37c8c0419257caf3
#https://www.wspolrzedne.pl
#http://aqicn.org/city/poland/swietokrzyski/polaniec/
# a potential next step would be to add a possibility to define a color range manually