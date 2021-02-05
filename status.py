#!/usr/bin/python
# -*- coding:utf8 -*

"""
Raspberry watchdog

Send a periodic notification to insure the system is up and running

can be put in a cron job

sudo crontab -e

add the following line

0 13 * * * /home/pi/pushover/status.py
"""

import os
import httplib, urllib

conn = httplib.HTTPSConnection("api.pushover.net:443")
title = "Forest Raspberry status"

msg = "uptime:\n" + os.popen("uptime").read()

conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "a7re182g2r6791e5m98whgteyowo7h",
    "user": "uye7fbag6sqp4ax8oo4itzhosdrnf1",
    "title": title,
    "message": msg,
    "sound": "alien",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
