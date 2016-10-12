# -*- coding:utf-8 -*-
import config
import requests
import json


def post(current_ip_val):


    attachments = []
    post = {
            "attachments": attachments
            }
    fields = []
    attachment = {
            "color": "#36a64f",
            "title": "IPアドレス変更検知",
            "fields": fields
            }
    region = {
            "title": "リージョン",
            "value": config.REGION,
            "short": False
            }
    ip = {
            "title": "IPアドレス",
            "value": current_ip_val,
            "short": False
            }

    attachments.append(attachment)
    fields.append(region)
    fields.append(ip)
    
    
    payload = json.dumps(post) 
    res = requests.post(config.SLACK_URL,data=payload)
