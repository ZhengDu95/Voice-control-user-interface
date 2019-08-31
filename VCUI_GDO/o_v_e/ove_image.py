#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:03:55 2019

@author: duzheng
"""
import webbrowser
import requests
import json

from speech_to_text import stt
from text_to_speech import tts
import conf


def ove_launch_image_func(lang):   
    if lang.lower() == 'english':
        speak_text = "welcome to launch the image application"
        
    else:
        speak_text = "欢迎使用OVE图像应用"
        
        
    tts.speak(speak_text=speak_text,language=lang)
        
    #send post request to image application
    space = conf.SPACE
    url = "http://" + conf.URL + "/app/images"
    url_post = "http://" + conf.URL + "/section"
        
        
    headers = {'Content-Type': 'application/json'}
    payload = {"space": space,"x":"0","y":"0","w":"4320","h":"2424","app":{"url":url,"states":{"load":"Highsmith"}}}
    r = requests.post(url_post, data=json.dumps(payload), headers = headers)
    ControlID = json.loads(r.text)
                
    url_web = 'http://' + conf.URL+ '/app/images/control.html?oveSectionId=' + str(ControlID['id'])
    try:
        webbrowser.open(url_web)
    except Exception as e:
        print("OVE image controller webpage open error:",e) 
        
        
def ove_image_operation_func(text,lang):
    url = conf.URL
    
    if lang.lower() == 'english':
        if  text.lower() == 'zoom in':
            speak_text = "which one do you want to zoom in, choose an id"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
                
            if search_text.isdigit():
                sectionID = search_text
                headers = {'Content-Type': 'application/json',
                           'accept': 'application/json'}
                
                payload = { 'zoom': '2', 'pan': { 'x': '0', 'y': '0' }}
                
                url_post = "http://" + conf.URL + "/app/images/instances/" + sectionID + "/state/transform"
                r = requests.post(url_post , data=json.dumps(payload), headers = headers)

                url = 'http://' + conf.URL + '/app/images/control.html?oveSectionId=' + sectionID
                webbrowser.open(url)
                
                
                speak_text = "zoom in imgae " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "wrong image id, try again."
                tts.speak(speak_text=speak_text,language=lang)


        
        elif  text.lower() == 'zoom out':
            speak_text = "which one do you want to zoom out, choose an id"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
                
            if search_text.isdigit():
                sectionID = search_text
                headers = {'Content-Type': 'application/json',
                           'accept': 'application/json'}
                
                payload = { 'zoom': '0.5', 'pan': { 'x': '0', 'y': '0' }}
                
                url_post = "http://" + conf.URL + "/app/images/instances/" + sectionID + "/state/transform"
                r = requests.post(url_post , data=json.dumps(payload), headers = headers)

                url = 'http://' + conf.URL + '/app/images/control.html?oveSectionId=' + sectionID
                webbrowser.open(url)
                
                
                speak_text = "zoom out imgae " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "wrong image id, try again."
                tts.speak(speak_text=speak_text,language=lang)
        
        else:
            speak_text = "wrong image operations, try again."
            tts.speak(speak_text=speak_text,language=lang)
            

    else:
        if  text == '放大':
            speak_text = "您想要放大哪个id控制区"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
                
            if search_text.isdigit():
                sectionID = search_text
                headers = {'Content-Type': 'application/json',
                           'accept': 'application/json'}
                
                payload = { 'zoom': '2', 'pan': { 'x': '0', 'y': '0' }}
                
                url_post = "http://" + conf.URL + "/app/images/instances/" + sectionID + "/state/transform"
                r = requests.post(url_post , data=json.dumps(payload), headers = headers)

                url = 'http://' + conf.URL + '/app/images/control.html?oveSectionId=' + sectionID
                webbrowser.open(url)
                
                
                speak_text = "放大图像 id " + search_text + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "错误的图像id， 请重试"
                tts.speak(speak_text=speak_text,language=lang)


        
        elif  text == '缩小':
            speak_text = "您想要缩小哪个id控制区"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
                
            if search_text.isdigit():
                sectionID = search_text
                headers = {'Content-Type': 'application/json',
                           'accept': 'application/json'}
                
                payload = { 'zoom': '0.5', 'pan': { 'x': '0', 'y': '0' }}
                
                url_post = "http://" + conf.URL + "/app/images/instances/" + sectionID + "/state/transform"
                r = requests.post(url_post , data=json.dumps(payload), headers = headers)

                url = 'http://' + conf.URL + '/app/images/control.html?oveSectionId=' + sectionID
                webbrowser.open(url)
                
                
                speak_text = "缩小图像 id " + search_text.lower() + ", 完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "错误的图像id， 请重试"
                tts.speak(speak_text=speak_text,language=lang)
        
        else:
            speak_text = "错误的图像操作， 请重试"
            tts.speak(speak_text=speak_text,language=lang)
        
                
                















