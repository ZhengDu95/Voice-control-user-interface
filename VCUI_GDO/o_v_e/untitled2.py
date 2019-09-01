#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:45:32 2019

@author: duzheng
"""

import webbrowser
import requests
import json
from ove.ove import Space
from ove import save_file

"""
space = "LocalNine"

headers = {'Content-Type': 'application/json'}

payload = {"space": space,"x":"0","y":"0","w":"4320","h":"2424","app":{"url":"http://146.169.220.4:8080/app/images","states":{"load":"Highsmith"}}}

r = requests.post("http://146.169.220.4:8080/section", data=json.dumps(payload), headers = headers)

ControlID = json.loads(r.text)
print(ControlID['id'])

url = 'http://146.169.220.4:8080/app/images/control.html?oveSectionId=' + str(ControlID['id'])

try:
    webbrowser.open(url)
except Exception as e:
    print("OVE image controller webpage open error:",e)  
"""




"""
space = "LocalFour"

headers = {'Content-Type': 'application/json'}

payload = {"space": space,"x":"0","y":"0","w":"2880","h":"1616","app":{"url":"http://146.169.220.4:8080/app/images","states":{"load":"Highsmith"}}}

r = requests.post("http://146.169.220.4:8080/section", data=json.dumps(payload), headers = headers)

ControlID = json.loads(r.text)
print(ControlID['id'])

url = 'http://146.169.220.4:8080/app/images/control.html?oveSectionId=' + str(ControlID['id'])

try:
    webbrowser.open(url)
except Exception as e:
    print("OVE image controller webpage open error:",e)  
"""  

"""
headers = {'Content-Type': 'application/json'}
url = "http://146.169.220.4:8080/sections/" + "3"
r = requests.delete(url, headers = headers)
"""

"""
headers = {'Content-Type': 'application/json'}
url = "http://146.169.220.4:8080/sections"
r = requests.get(url, headers = headers)
ControlID = json.loads(r.text)
print(ControlID)
"""

"""
cid = "id 0"
print(cid[0])
print(str(cid[3]))
"""


# practice for vedio application 
"""
space = "LocalNine"

headers = {'Content-Type': 'application/json'}

payload = {"space": space,"x":"0","y":"0","w":"4320","h":"2424","app":{"url":"http://146.169.220.4:8080/app/videos","states":{"load":"DSIIntro", "url": "http://www.youtube.com/embed/XY3NP4JHXZ4"}}}

r = requests.post("http://146.169.220.4:8080/section", data=json.dumps(payload), headers = headers)

ControlID = json.loads(r.text)
print(ControlID['id'])

url = 'http://146.169.220.4:8080/app/videos/control.html?oveSectionId=' + str(ControlID['id'])

try:
    webbrowser.open(url)
except Exception as e:
    print("OVE image controller webpage open error:",e)  
"""

"""
space = Space(ove_host="localhost", space_name="LocalNine", control_port=8080)

space.delete_sections()


video = space.add_section(w=2880, h=1616, x=720, y=404, app_type='videos')
video.set_url('https://www.youtube.com/watch?v=QJo-VFs1X5c')

video2 = space.add_section_by_grid(r=1, c=1, w=1, h=1, app_type='videos')
video2.set_url("https://www.youtube.com/watch?v=XY3NP4JHXZ4")

video.play()
video2.play()
video.pause()
video2.pause()
"""

"""
space = Space(ove_host="localhost", space_name="LocalFour", control_port=8080)
space.delete_sections()
space.enable_online_mode()
space.enable_browser_opening()

video = space.add_section(w=2880, h=1616, x=0, y=0, app_type='videos')
video.set_url('https://www.youtube.com/watch?v=QJo-VFs1X5c')
"""           


"""
headers = {'accept': 'application/json'}
url = "http://localhost:8080/app/videos/operation/play?loop=true&oveSectionId=2"
r = requests.post(url)
"""


#curl -X POST "http://localhost:8080/app/images/instances/0/state/transform" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"zoom\": 2, \"pan\": { \"x\": 0, \"y\": 0 }}"

headers = {'Content-Type': 'application/json',
           'accept': 'application/json'}

payload = { 'zoom': '2', 'pan': { 'x': '0', 'y': '0' }}

r = requests.post("http://146.169.209.206:8080/app/images/instances/0/state/transform", data=json.dumps(payload), headers = headers)


url = 'http://146.169.209.206:8080/app/images/control.html?oveSectionId=0'

webbrowser.open(url)













