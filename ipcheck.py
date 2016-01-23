# -*- coding:utf-8 -*-
import urllib2
import tweet



current_ip_val = urllib2.urlopen('http://inet-ip.info/ip').read()

with open('global.ip','r') as recorded_ip:
	recorded_ip_val = recorded_ip.read()

if (current_ip_val != recorded_ip_val):
	with open('global.ip','w') as recorded_ip:
		recorded_ip.write(current_ip_val)
	text = "@youraccount tweet message here\nIP:" + current_ip_val
	tweet.tweet(text)
