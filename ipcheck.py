# -*- coding:utf-8 -*-
import requests
import tweet
import slack
import gehirn
import os


current_ip_val = requests.get('http://ifconfig.moe/').text.strip()
ip_file = os.path.join(os.path.dirname(__file__), 'global.ip')


with open(ip_file,'r') as recorded_ip:
	recorded_ip_val = recorded_ip.read()

if (current_ip_val != recorded_ip_val):
	with open(ip_file,'w') as recorded_ip:
		recorded_ip.write(current_ip_val)
	tweet.tweet(current_ip_val)
	slack.post(current_ip_val)
	gehirn.update(current_ip_val)
