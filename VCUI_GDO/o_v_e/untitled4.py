#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:07:25 2019

@author: duzheng
"""

if lang.lower() == 'english':
        if text.lower() == 'play all':
            url = "http://localhost:8080/app/videos/operation/play"
            r = requests.post(url)
            
        if text.lower() == 'play 0':
            sectionID = text[5]
            url = "http://localhost:8080/app/videos/operation/play?loop=true&oveSectionId=" + sectionID
            r = requests.post(url)
                
        if text.lower() == 'play 1':
            sectionID = text[5]
            url = "http://localhost:8080/app/videos/operation/play?loop=true&oveSectionId=" + sectionID
            r = requests.post(url)
                    
        if text.lower() == 'play 2':
            sectionID = text[5]
            url = "http://localhost:8080/app/videos/operation/play?loop=true&oveSectionId=" + sectionID
            r = requests.post(url)
            
        
                       
        elif text.lower() == 'pause all':
            url = "http://localhost:8080/app/videos/operation/pause"
            r = requests.post(url)
            
            
        elif text.lower() == 'mute all':
            url = "http://localhost:8080/app/videos/operation/mute"
            r = requests.post(url)

            
        elif text.lower() == 'stop all':
            url = "http://localhost:8080/app/videos/operation/stop"
            r = requests.post(url)

        
        else:
            speak_text = ""
 




       
        speak_text = "it " + text + "video successfully!"
        tts.speak(speak_text=speak_text,language=lang) 
    












    else:
        if text.lower() == '全部播放':
            url = "http://localhost:8080/app/videos/operation/play"
            r = requests.post(url)
            speak_text = "it plays all videos"
            tts.speak(speak_text=speak_text,language=lang)
                       
        elif text.lower() == '全部暂停':
            url = "http://localhost:8080/app/videos/operation/pause"
            r = requests.post(url)
            speak_text = "it pauses all videos"
            tts.speak(speak_text=speak_text,language=lang)
            
        elif text.lower() == '全部无声':
            url = "http://localhost:8080/app/videos/operation/mute"
            r = requests.post(url)
            speak_text = "it mutes all videos"
            tts.speak(speak_text=speak_text,language=lang)
            
        elif text.lower() == '全部停止':
            url = "http://localhost:8080/app/videos/operation/stop"
            r = requests.post(url)
            speak_text = "it stops all videos"
            tts.speak(speak_text=speak_text,language=lang)
        
        else:
            speak_text = "错误操作"
            tts.speak(speak_text=speak_text,language=lang)