# -*- coding:utf-8 -*-
import config
import twython

def tweet(current_ip_val):
    text = "@youraccount tweet message here\nIP:" + current_ip_val
    api = twython.Twython(config.CONSUMER_KEY,config.CONSUMER_SECRET,config.ACCESS_KEY,config.ACCESS_SECRET)
	
    try:
	api.update_status(status=text)
    except twython.TwythonError as e:
	print e

