# -*- coding:utf-8 -*-
import urllib2
import tweet
import os


current_ip_val = urllib2.urlopen('http://inet-ip.info/ip').read()
ip_file = os.path.join(os.path.dirname(__file__), 'global.ip')


with open('ip_file','r') as recorded_ip:
	recorded_ip_val = recorded_ip.read()

if (current_ip_val != recorded_ip_val):
	with open(ip_file,'w') as recorded_ip:
		recorded_ip.write(current_ip_val)
	text = "@youraccount tweet message here\nIP:" + current_ip_val
	tweet.tweet(text)
