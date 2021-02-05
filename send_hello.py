import httplib, urllib
conn = httplib.HTTPSConnection("api.pushover.net:443")
title = "Alerte intrusion Forest"
msg = """
Porte veranda ouverte depuis 10 minutes
detection prsence chambre
"""
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "a7re182g2r6791e5m98whgteyowo7h",
    "user": "uye7fbag6sqp4ax8oo4itzhosdrnf1",
    "title": title,
    "message": msg,
    "sound": "alien",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
