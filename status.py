#!/usr/bin/python
# -*- coding:utf8 -*

import os

print ("Rasp_alarm status\n")

uptime = "uptime:\n" + os.system("uptime")

print(uptime)

print ("bye")
