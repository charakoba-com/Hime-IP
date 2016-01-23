# -*- coding:utf-8 -*-
import config
import twython

def tweet(text):
    api = twython.Twython(config.CONSUMER_KEY,config.CONSUMER_SECRET,config.ACCESS_KEY,config.ACCESS_SECRET)
	
    try:
	api.update_status(status=text)
    except twython.TwythonError as e:
	print e

