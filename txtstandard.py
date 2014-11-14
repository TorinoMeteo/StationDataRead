import urllib2 as url
from datetime import datetime as DT
from time import strftime
import re

station = {'fetch_ok': False, 'datetime': None, 'weather': None, 'temperature': None, 'temperature_max': None, 'temperature_max_time': None, 'temperature_min': None, 'temperature_min_time': None, 'relative_humidity': None, 'relative_humidity_max': None, 'relative_humidity_max_time': None, 'relative_humidity_min': None, 'relative_humidity_min_time': None, 'dewpoint': None, 'dewpoint_max': None, 'dewpoint_max_time': None, 'dewpoint_min': None, 'dewpoint_min_time': None, 'pressure': None, 'pressure_max': None, 'pressure_max_time': None, 'pressure_min': None, 'pressure_min_time': None, 'wind_strength': None, 'wind_dir': None, 'wind_strength_max': None, 'wind_dir_max': None, 'wind_max_time': None, 'rain': None, 'rain_rate': None, 'rain_rate_max': None, 'rain_rate_max_time': None, 'rain_month': None, 'rain_year':None}


def gettxtdata(urlfield, DTParser, TParser, LastRead):
	try:	
		data = url.urlopen(url=str(urlfield),timeout=10000).read(20000)
		data = re.sub('<.*?>', "", data)
		data = re.sub(' ', "", data)
		data = re.sub('[\t\r\f\v]', "", data)
		data = data.split("\n")
		station['fetch_ok'] = True
		#datetime
		station['datetime'] = DT.strptime(str(data[1]+" "+ data[2]), DTParser)
		if (station['datetime'] <= DT.now()) and (station['datetime'] != LastRead):
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

			#dewpoint
			m = re.search('\d+(\.?\,?)?\d*', data[22])
			if m != None:
				station['dewpoint'] =  float(m.group(0))
			else :
				station['dewpoint'] = 'NaN'	

			print station['dewpoint'] 

			#dewpoint_max
			m = re.search('\d+(\.?\,?)?\d*', data[23])
			if m != None:
				station['dewpoint_max'] =  float(m.group(0))
			else :
				station['dewpoint_max'] = 'NaN'		

			#dewpoint_max_time
			station['dewpoint_max_time'] = DT.strptime(str(data[24]), TParser).strftime("%H:%M")

			#dewpoint_min
			m = re.search('\d+(\.?\,?)?\d*', data[25])
			if m != None:
				station['dewpoint_min'] =  float(m.group(0))
			else :
				station['dewpoint_min'] = 'NaN'		

			#dewpoint_min_time
			station['dewpoint_min_time'] = DT.strptime(str(data[26]), TParser).strftime("%H:%M")

			#pressure
			m = re.search('\d+(\.?\,?)?\d*', data[28])
			if m != None:
				station['pressure'] =  float(m.group(0))
			else :
				station['pressure'] = 'NaN'	

			#pressure_max
			m = re.search('\d+(\.?\,?)?\d*', data[29])
			if m != None:
				station['pressure_max'] =  float(m.group(0))
			else :
				station['pressure_max'] = 'NaN'		

			#pressure_max_time
			station['pressure_max_time'] = DT.strptime(str(data[30]), TParser).strftime("%H:%M")

			#pressure_min
			m = re.search('\d+(\.?\,?)?\d*', data[31])
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
				station['wind_dir'] =  m.group(0)
			else :
				station['wind_dir'] = 'NaN'

			#wind_strength_max
			m = re.search('\d+(\.?\,?)?\d*', data[36])
			if m != None:
				station['wind_strength_max'] =  float(m.group(0))
			else :
				station['wind_strength_max'] = 'NaN'	

			#wind_direction_max
			m = re.search('(\d+)?((N?S?O?W?E?n?s?o?w?e?)+)?', data[35])
			if m != None:
				station['wind_dir_max'] =  m.group(0)
			else :
				station['wind_dir_max'] = 'NaN'

			#wind_direction_max_time
			station['wind_max_time'] = DT.strptime(str(data[38]), TParser).strftime("%H:%M")

			#rain
			m = re.search('\d+(\.?\,?)?\d*', data[40])
			if m != None:
				station['rain'] =  float(m.group(0))
			else :
				station['rain'] = 'NaN'	

			#rain_rate
			m = re.search('\d+(\.?\,?)?\d*', data[41])
			if m != None:
				station['rain_rate'] =  float(m.group(0))
			else :
				station['rain_rate'] = 'NaN'	

			#rain_rate_max
			m = re.search('\d+(\.?\,?)?\d*', data[42])
			if m != None:
				station['rain_rate_max'] =  float(m.group(0))
			else :
				station['rain_rate_max'] = 'NaN'		

			#rain_rate_max_time
			station['rain_rate_max_time'] = DT.strptime(str(data[43]), TParser).strftime("%H:%M")

			#rain_month
			m = re.search('\d+(\.?\,?)?\d*', data[44])
			if m != None:
				station['rain_month'] =  float(m.group(0))
			else :
				station['rain_month'] = 'NaN'	

			#rain_year
			m = re.search('\d+(\.?\,?)?\d*', data[45])
			if m != None:
				station['rain_year'] =  float(m.group(0))
			else :
				station['rain_year'] = 'NaN'
			
			print "fetched"
	
			
		else:
			station['fetch_ok'] = False
			print "not fetched"

		return station
	except url.HTTPError, e:
		print "HTTP Error: %r" %e
		station['fetch_ok'] = False
	except url.URLError, e:
		print "URL Error: %r" %e
		station['fetch_ok'] = False
	except ValueError, e:
		print "Parsing Error: %r" %e
		station['fetch_ok'] = False
	except Exception, e:
		print "Generale error: %r" %e
		station['fetch_ok'] = False

