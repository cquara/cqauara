import urllib2
import commands
import re
import math
import subprocess
import time



def get_geolocation():
		R = 6731
		alert = "Quake Occured At A Distance Of : "
		file_name = "test"
		dist = []
		response = commands.getstatusoutput('/etc/networks/interfaces')
		lines = response[1].split('\n')
		geourl = 'https://maps.googleapis.com/maps/api/browserlocation/json?browser=firefox&sensor=true'
		for i in range(1,len(lines)):
			macs = re.compile('([^ ].+) ([^ ]+:[^ ]+:[^ ]+:[^ ]+:[^ ]+:[^ ]+) ([^ ]+)').findall(lines[i])
			name = macs[0][0]
			mac = macs[0][1]
			ss = macs[0][2]
			geourl += '&wifi=mac:%s%%7Cssid:%s%%7Css:%s' % (mac.replace(":", "-"), name.replace(" ", "%20"), ss)
		# look up google maps API for lat/lng
		response = urllib2.urlopen(geourl)
		html = response.read()
		lat = re.compile('"lat" : (.+),').findall(html)[0]
		lng = re.compile('"lng" : (.+)').findall(html)[0]
		#return (lat, lng)
		print lat," ",lng,"\n\n"
		data_url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"
		data = urllib2.urlopen(data_url)
		for line in data:
			lst = line.split(" ")
			lst1 = lst[0].split(",")
			lat1 = lst1[1]
			lng1 = lst1[2]
			if(lat1.isalpha()):
				continue
			lat1 = float(lst1[1])
			lng1 = float(lst1[2])
			mag = float(lst1[4])
			lat = float(lat)
			lng = float(lng)
			#print lat1," ",lng1," ",mag,"\n"
			
			dlat = (lat1-lat)
			dlng = (lng1-lng)

			lat_new = lat
			lng_new = lng

			a = math.sin(dlat/2)*math.sin(dlat/2)+math.sin(dlng/2) * math.sin(dlng/2) * math.cos(lat) * math.cos(lat1); 
			c = 2 * math.atan2(math.sqrt(abs(a)),math.sqrt(1-a));
			d = R * c
			dist.append(d)
		print dist,"\n"
		minimum = min(dist)
		print minimum
		if(minimum < 2000.0):
			subprocess.call(["espeak",alert+str(minimum)+" kilometers","-w"+file_name+".wav"])
			print "Alert message..."
			#for i in range(1,20):
				#subprocess.call(["sudo","./pifm","test.wav","96"])

while(True):
	get_geolocation()
	time.sleep(300)
