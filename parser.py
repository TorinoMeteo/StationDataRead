#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import urllib2 as url
from datetime import datetime as DT
from time import strftime
import re
from txtstandard import *

try:
	con = mdb.connect(host='localhost',user='root',db='db_torinometeo')

	cur = con.cursor()
	cur.execute("SELECT id,name,data_url,dateformat,timeformat,data_type_id FROM realtime_station order by id asc")
	output_data = cur.fetchall()
	
	for (sql_id, sql_name, sql_data_url, sql_dateformat, sql_timeformat, sql_data_type_id) in output_data:	
		print "fetching data for "+str(sql_name)+" output id "+str(sql_id)
		print str(sql_data_url)
		
		cur.execute("SELECT datetime FROM realtime_data WHERE station_id = "+str(sql_id)+" order by id desc")
		#last_DT = DT.strptime(str(cur.fetchone()), "%Y-%m-%d %H:%M:%S")
		last_DT = cur.fetchone()
		if last_DT == None:
			last_DT = DT.strptime("01/01/1900 00:01", "%d/%m/%Y %H:%M")
		else:
			last_DT = last_DT[0]
		if sql_data_type_id == 1:
			if sql_dateformat == None:
				sql_dateformat = '%H:%M %d/%m/%y'
			if sql_timeformat == None:
				sql_timeformat = '%H:%M'
			output = gettxtdata(sql_data_url,sql_dateformat,sql_timeformat, last_DT)
			print output['fetch_ok']			
			if output['fetch_ok']:
				cur.execute("INSERT into realtime_data (station_id,datetime,weather,temperature,temperature_max,temperature_max_time,temperature_min,temperature_min_time,relative_humidity,relative_humidity_max,relative_humidity_max_time,relative_humidity_min,relative_humidity_min_time,dewpoint,dewpoint_max,dewpoint_max_time,dewpoint_min,dewpoint_min_time,pressure,pressure_max,pressure_max_time,pressure_min,pressure_min_time,wind_strength,wind_dir,wind_strength_max,wind_dir_max,wind_max_time,rain,rain_rate,rain_rate_max,rain_rate_max_time,rain_month,rain_year) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sql_id,output['datetime'],output['weather'],output['temperature'],output['temperature_max'],output['temperature_max_time'],output['temperature_min'],output['temperature_min_time'],output['relative_humidity'],output['relative_humidity_max'],output['relative_humidity_max_time'],output['relative_humidity_min'],output['relative_humidity_min_time'],output['dewpoint'],output['dewpoint_max'],output['dewpoint_max_time'],output['dewpoint_min'],output['dewpoint_min_time'],output['pressure'],output['pressure_max'],output['pressure_max_time'],output['pressure_min'],output['pressure_min_time'],output['wind_strength'],output['wind_dir'],output['wind_strength_max'],output['wind_dir_max'],output['wind_max_time'],output['rain'],output['rain_rate'],output['rain_rate_max'],output['rain_rate_max_time'],output['rain_month'],output['rain_year']))
				con.commit()
			sys.exit(1) # remove for test on all stations!!!!! now only ID 1 will be fetched


		print ""
except mdb.Error, e:

	print "Error %r" % e
	sys.exit(1)
    
finally:    

	if con:    
		con.close()
