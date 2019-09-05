#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 08:51:23 2019

@author: duzheng
"""
import webbrowser
import requests
import json

from speech_to_text import stt
from text_to_speech import tts
import conf
import time

#from ove.ove import Space
#from ove import save_file

def ove_launch_video_func(lang):
    if lang.lower() == 'english':
        speak_text = "welcome to launch the video application and choose some operations after loading the video"
        
    else:
        speak_text = "欢迎使用OVE视频应用,并在下载视频后选择相应操作"
        
        
    tts.speak(speak_text=speak_text,language=lang)
        
    #send post request to video application
    space = conf.SPACE
    url = "http://" + conf.URL + "/app/videos"
    url_post = "http://" + conf.URL + "/section"
        
        
    headers = {'Content-Type': 'application/json'}
    
    if space == "DOCluster":
        payload = {"space": space,"x":7680,"y":0,"w":15360,"h":4320,"app":{"url":url,"states":{"load":"DSIIntro"}}}
    elif space == "DOSection":
        payload = {"space": space,"x":5760,"y":0,"w":19200,"h":4320,"app":{"url":url,"states":{"load":"DSIIntro"}}}
        
    r = requests.post(url_post, data=json.dumps(payload), headers = headers)
    ControlID = json.loads(r.text)
                
    url_web = 'http://' + conf.URL+ '/app/videos/control.html?oveSectionId=' + str(ControlID['id'])
    try:
        webbrowser.open(url_web)
    except Exception as e:
        print("OVE video controller webpage open error:",e)  

def ove_video_operation_func(text,lang):
    url = conf.URL 
    
    if lang.lower() == 'english':
        if  text.lower() == 'play':
            speak_text = "play all videos or choose a section"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
            if search_text.lower() == 'play all':             
                url = "http://" + url + "/app/videos/operation/play"
                r = requests.post(url)
                speak_text = "play video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://" + url + "/app/videos/operation/play?loop=true&oveSectionId=" + sectionID
                r = requests.post(url)
                speak_text = "play video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "wrong video operations, try again."
                tts.speak(speak_text=speak_text,language=lang)
                
            
                
            
            
        elif text.lower() == 'pause':
            speak_text = "pause all videos or choose a section"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
            if search_text.lower() == 'pause all':
                
                url = "http://" + url + "/app/videos/operation/pause"
                r = requests.post(url)
                speak_text = "pause video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                
                sectionID = search_text
                url = "http://" + url + "/app/videos/operation/pause?loop=true&oveSectionId=" + sectionID
                r = requests.post(url)
                speak_text = "pause video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "wrong video operations, try again."
                tts.speak(speak_text=speak_text,language=lang)
            
            
            
            

        elif text.lower() == 'mute':
            speak_text = "mute all videos or choose a section"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
            if search_text.lower() == 'mute all':
                
                url = "http://" + url + "/app/videos/operation/mute"
                r = requests.post(url)
                speak_text = "mute video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                
                sectionID = search_text
                url = "http://" + url + "/app/videos/operation/mute?loop=true&oveSectionId=" + sectionID
                r = requests.post(url)
                speak_text = "mute video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "wrong video operations, try again."
                tts.speak(speak_text=speak_text,language=lang)
            
            
            

            
        elif text.lower() == 'stop':
            speak_text = "stop all videos or choose a section"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
            if search_text.lower() == 'stop all':
                
                url = "http://" + url + "/app/videos/operation/stop"
                r = requests.post(url)
                speak_text = "stop video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                
                sectionID = search_text
                url = "http://" + url + "/app/videos/operation/stop?loop=true&oveSectionId=" + sectionID
                r = requests.post(url)
                speak_text = "stop video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "wrong video operations, try again."
                tts.speak(speak_text=speak_text,language=lang)
                
            
        
        else:
            speak_text = ''
            
            
    else:
        if text == '播放':
            speak_text = "播放所有视频或者选择某个部分播放"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
            if search_text == '全部播放':
                url = "http://" + url + "/app/videos/operation/play"
                r = requests.post(url)
                speak_text = "视频播放 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://" + url + "/app/videos/operation/play?loop=true&oveSectionId=" + sectionID
                r = requests.post(url)
                speak_text = "视频播放 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "错误的视频操作，请重新命令"
                tts.speak(speak_text=speak_text,language=lang)
                
            
                
            
            
        elif text == '暂停':
            speak_text = "暂停所有视频或者选择某个部分播放"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
            if search_text == '全部暂停':
                url = "http://" + url + "/app/videos/operation/pause"
                r = requests.post(url)
                speak_text = "视频暂停 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://" + url + "/app/videos/operation/pause?loop=true&oveSectionId=" + sectionID
                r = requests.post(url)
                speak_text = "视频暂停 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "错误的视频操作，请重新命令"
                tts.speak(speak_text=speak_text,language=lang)
                
            
            
            

        elif text == '静音':
            speak_text = "静音所有视频或者选择某个部分播放"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
            if search_text == '全部静音':
                url = "http://" + url + "/app/videos/operation/mute"
                r = requests.post(url)
                speak_text = "视频静音 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://" + url + "/app/videos/operation/mute?loop=true&oveSectionId=" + sectionID
                r = requests.post(url)
                speak_text = "视频静音 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "错误的视频操作，请重新命令"
                tts.speak(speak_text=speak_text,language=lang)
                
            
            

            
        elif text == '停止':
            speak_text = "停止所有视频或者选择某个部分播放"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
            if search_text == '全部停止':
                url = "http://" + url + "/app/videos/operation/stop"
                r = requests.post(url)
                speak_text = "视频停止 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://" + url + "/app/videos/operation/stop?loop=true&oveSectionId=" + sectionID
                r = requests.post(url)
                speak_text = "视频停止 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "错误的视频操作，请重新命令"
                tts.speak(speak_text=speak_text,language=lang)
                
            
        
        else:
            speak_text = ""
    
        

