#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import urllib2 as url
from datetime import datetime as DT
from time import strftime
import re
from txtstandard import *


station = {'id': None, 'datetime': None, 'weather': None, 'temperature': None, 'temperature_max': None, 'temperature_max_time': None, 'temperature_min': None, 'temperature_min_time': None, 'relative_humidity': None, 'relative_humidity_max': None, 'relative_humidity_max_time': None, 'relative_humidity_min': None, 'relative_humidity_min_time': None, 'dewpoint': None, 'dewpoint_max': None, 'dewpoint_max_time': None, 'dewpoint_min': None, 'dewpoint_min_time': None, 'pressure': None, 'pressure_max': None, 'pressure_max_time': None, 'pressure_min': None, 'pressure_min_time': None, 'wind_strength': None, 'wind_dir': None, 'wind_strength_max': None, 'wind_dir_max': None, 'wind_max_time': None, 'rain': None, 'rain_rate': None, 'rain_rate_max': None, 'rain_rate_max_time': None, 'rain_month': None, 'rain_year':None}


try:
	con = mdb.connect(host='localhost',user='root',db='db_torinometeo')

	cur = con.cursor()
	cur.execute("SELECT id,name,data_url,dateformat,timeformat,data_type_id FROM realtime_station order by id asc")


	station_data = cur.fetchall()
	station_data = station_data
	for (sql_id, sql_name, sql_data_url, sql_dateformat, sql_timeformat, sql_data_type_id) in station_data:	
		print "fetching data for "+str(sql_name)+" station id "+str(sql_id)
		print str(sql_data_url)
		print DT.now();
		if sql_data_type_id == 1:
			if sql_dateformat == None:
				sql_dateformat = '%H:%M %d/%m/%y'
			if sql_timeformat == None:
				sql_timeformat = '%H:%M'
			gettxtdata(sql_data_url,sql_dateformat,sql_timeformat)
		print DT.now()
		print ""
except mdb.Error, e:

	print "Error"
	sys.exit(1)
    
finally:    

	if con:    
		con.close()
