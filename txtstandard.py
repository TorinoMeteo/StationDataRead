import urllib2 as url
from datetime import datetime as DT
from time import strftime
import re


def gettxtdata(urlfield, DTParser, TParser):
	try:	
		data = url.urlopen(url=str(urlfield),timeout=10000).read(20000)
		data = re.sub('<.*?>', "", data)
		data = re.sub(' ', "", data)
		data = re.sub('[\t\r\f\v]', "", data)
		data = data.split("\n")
		print str(data[1]+" "+ data[2])
		print DT.now()
		#datetime
		station['datetime'] = DT.strptime(str(data[1]+" "+ data[2]), DTParser)
		if station['datetime'] <= DT.now():
			#temperature
			m = re.search('\d+(\.?\,?)?\d*', data[4])
			if m != None:
				station['temperature'] =  float(m.group(0))
			else :
				station['temperature'] = 'NaN'		

			#max temperature
			m = re.search('\d+(\.?\,?)?\d*', data[5])
			if m != None:
				station['temperature_max'] =  float(m.group(0))
			else :
				station['temperature_max'] = 'NaN'		

			#max temperature time
			station['temperature_max_time'] = DT.strptime(str(data[6]), TParser).strftime("%H:%M")

			#min temperature
			m = re.search('\d+(\.?\,?)?\d*', data[7])
			if m != None:
				station['temperature_min'] =  float(m.group(0))
			else :
				station['temperature_min'] = 'NaN'		

			#min temperature time
			station['temperature_min_time'] = DT.strptime(str(data[8]), TParser).strftime("%H:%M")

			#relative humidty
			m = re.search('\d+(\.?\,?)?\d*', data[16])
			if m != None:
				station['relative_humidity'] =  float(m.group(0))
			else :
				station['relative_humidity'] = 'NaN'	

			#max relative_humidity
			m = re.search('\d+(\.?\,?)?\d*', data[5])
			if m != None:
				station['relative_humidity_max'] =  float(m.group(0))
			else :
				station['relative_humidity_max'] = 'NaN'		

			#max relative_humidity_max_time
			station['relative_humidity_max_time'] = DT.strptime(str(data[18]), TParser).strftime("%H:%M")

			#min relative_humidity_min
			m = re.search('\d+(\.?\,?)?\d*', data[7])
			if m != None:
				station['relative_humidity_min'] =  float(m.group(0))
			else :
				station['relative_humidity_min'] = 'NaN'		

			#min realtive_humidity_min_time
			station['relative_humidity_min_time'] = DT.strptime(str(data[20]), TParser).strftime("%H:%M")

			#dew_point
			m = re.search('\d+(\.?\,?)?\d*', data[16])
			if m != None:
				station['dew_point'] =  float(m.group(0))
			else :
				station['dew_point'] = 'NaN'	

			#dew_point_max
			m = re.search('\d+(\.?\,?)?\d*', data[5])
			if m != None:
				station['dew_point_max'] =  float(m.group(0))
			else :
				station['dew_point_max'] = 'NaN'		

			#dew_point_max_time
			station['dew_point_max_time'] = DT.strptime(str(data[24]), TParser).strftime("%H:%M")

			#dew_point_min
			m = re.search('\d+(\.?\,?)?\d*', data[7])
			if m != None:
				station['dew_point_min'] =  float(m.group(0))
			else :
				station['dew_point_min'] = 'NaN'		

			#dew_point_min_time
			station['dew_point_min_time'] = DT.strptime(str(data[26]), TParser).strftime("%H:%M")

			#pressure
			m = re.search('\d+(\.?\,?)?\d*', data[16])
			if m != None:
				station['pressure'] =  float(m.group(0))
			else :
				station['pressure'] = 'NaN'	

			#pressure_max
			m = re.search('\d+(\.?\,?)?\d*', data[5])
			if m != None:
				station['pressure_max'] =  float(m.group(0))
			else :
				station['pressure_max'] = 'NaN'		

			#pressure_max_time
			station['pressure_max_time'] = DT.strptime(str(data[30]), TParser).strftime("%H:%M")

			#pressure_min
			m = re.search('\d+(\.?\,?)?\d*', data[7])
			if m != None:
				station['pressure_min'] =  float(m.group(0))
			else :
				station['pressure_min'] = 'NaN'		

			#pressure_min_time
			station['pressure_min_time'] = DT.strptime(str(data[32]), TParser).strftime("%H:%M")

			#wind_strength
			m = re.search('\d+(\.?\,?)?\d*', data[34])
			if m != None:
				station['wind_strength'] =  float(m.group(0))
			else :
				station['wind_strength'] = 'NaN'	

			#wind_direction
			m = re.search('(\d+)?((N?S?O?W?E?n?s?o?w?e?)+)?', data[35])
			if m != None:
				station['wind_direction'] =  m.group(0)
			else :
				station['wind_direction'] = 'NaN'

			#wind_strength_max
			m = re.search('\d+(\.?\,?)?\d*', data[36])
			if m != None:
				station['wind_strength_max'] =  float(m.group(0))
			else :
				station['wind_strength_max'] = 'NaN'	

			#wind_direction_max
			m = re.search('(\d+)?((N?S?O?W?E?n?s?o?w?e?)+)?', data[35])
			if m != None:
				station['wind_direction_max'] =  m.group(0)
			else :
				station['wind_direction_max'] = 'NaN'

			#wind_direction_max_time
			station['wind_direction_max_time'] = DT.strptime(str(data[38]), TParser).strftime("%H:%M")
			print "fetched"
			
			print "insert done"
	except url.HTTPError, e:
		print "HTTP Error: %r" %e
	except url.URLError, e:
		print "URL Error: %r" %e
	except ValueError, e:
		print "Parsing Error: %r" %e
	except Exception, e:
		print "Generale error: %r" %e

