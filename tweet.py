# -*- coding:utf-8 -*-
import config
import twython

def tweet(current_ip_val):
    text = u"@chamaharun 姫だよ。IPアドレスの変更を検知したよ。\nIP:" + current_ip_val
    api = twython.Twython(config.CONSUMER_KEY,config.CONSUMER_SECRET,config.ACCESS_KEY,config.ACCESS_SECRET)
	
    try:
	api.update_status(status=text)
    except twython.TwythonError as e:
	print e

