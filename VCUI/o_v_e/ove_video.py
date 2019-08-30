#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:45:52 2019

@author: duzheng
"""

import webbrowser
import requests
import json

from speech_to_text import stt
from text_to_speech import tts
import conf

from ove.ove import Space
from ove import save_file







def ove_launch_video_func(lang):
    if lang.lower() == 'english':
        speak_text = "welcome to launch the video application"
        tts.speak(speak_text=speak_text,language=lang)
        
        url = 'http://localhost:8080/app/videos'
        try:
            webbrowser.open(url)
        except Exception as e:
            print("OVE core open error:",e)  
        
        #update space 
        speak_text = "which space do you choose, local nine or local four"
        tts.speak(speak_text=speak_text,language=lang)
    
    else:
        speak_text = "欢迎使用OVE视频应用"
        tts.speak(speak_text=speak_text,language=lang)
        
        url = 'http://localhost:8080/app/videos'
        try:
            webbrowser.open(url)
        except Exception as e:
            print("OVE core open error:",e)  
        
        #update space 
        speak_text = "请问您想用九屏显示器或者四屏显示器观看"
        tts.speak(speak_text=speak_text,language=lang)
        
        
        
        
        
        
def ove_launch_video_space_func(text,lang):  
    if lang.lower() == 'english':
        if  text.lower() == 'video local 9':
            space = Space(ove_host="localhost", space_name="LocalNine", control_port=8080)
            space.enable_online_mode()
            space.enable_browser_opening()

            video = space.add_section(w=2880, h=1616, x=720, y=404, app_type='videos')
            video.set_url('https://www.youtube.com/watch?v=QJo-VFs1X5c')
            
            speak_text = "please choose which viewer you want to see, zero to eight and choose some operations after loading the video"
            tts.speak(speak_text=speak_text,language=lang)
        
            conf.SPACE = "LocalNine"
            
        elif text.lower() == 'video local 4':
            space = Space(ove_host="localhost", space_name="LocalFour", control_port=8080)
            space.enable_online_mode()
            space.enable_browser_opening()

            video = space.add_section(w=2880, h=1616, x=0, y=0, app_type='videos')
            video.set_url('https://www.youtube.com/watch?v=QJo-VFs1X5c')
            
            speak_text = "please choose which viewer you want to see, zero to three and choose some operations after loading the video"
            tts.speak(speak_text=speak_text,language=lang)
        
            conf.SPACE = "LocalFour"
    
    else:
        if(text == '视频数字9'):
            #send post request to image application
            space = Space(ove_host="localhost", space_name="LocalNine", control_port=8080)
            space.enable_online_mode()
            space.enable_browser_opening()

            video = space.add_section(w=2880, h=1616, x=720, y=404, app_type='videos')
            video.set_url('https://www.youtube.com/watch?v=QJo-VFs1X5c')
        
            speak_text = "请选择您想用哪一个显示器观看，分屏零到分屏八并在下载视频后选择相应操作"
            tts.speak(speak_text=speak_text,language=lang)
        
            conf.SPACE = "LocalNine"
            
        elif(text == '视频数字4'):
            space = Space(ove_host="localhost", space_name="LocalFour", control_port=8080)
            space.enable_online_mode()
            space.enable_browser_opening()

            video = space.add_section(w=2880, h=1616, x=0, y=0, app_type='videos')
            video.set_url('https://www.youtube.com/watch?v=QJo-VFs1X5c')
            
            speak_text = "请选择您想用哪一个显示器观看，分屏零到分屏三并在下载视频后选择相应操作"
            tts.speak(speak_text=speak_text,language=lang)
        
            conf.SPACE = "LocalFour"
    
        else: 
            speak_text = "错误的屏幕选择，请重新选择九屏或者四屏播放视频"
            tts.speak(speak_text=speak_text,language=lang)
            

def ove_launch_video_operation_func(text,lang):    
    if lang.lower() == 'english':
        if  text.lower() == 'play':
            speak_text = "play all videos or choose a section"
            tts.speak(speak_text=speak_text,language=lang)
            
            search_text = stt.stt_func(selected_lang=lang)
            
            if search_text.lower() == 'play all':
                url = "http://localhost:8080/app/videos/operation/play"
                r = requests.post(url)
                speak_text = "play video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://localhost:8080/app/videos/operation/play?loop=true&oveSectionId=" + sectionID
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
                url = "http://localhost:8080/app/videos/operation/pause"
                r = requests.post(url)
                speak_text = "pause video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://localhost:8080/app/videos/operation/pause?loop=true&oveSectionId=" + sectionID
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
                url = "http://localhost:8080/app/videos/operation/mute"
                r = requests.post(url)
                speak_text = "mute video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://localhost:8080/app/videos/operation/mute?loop=true&oveSectionId=" + sectionID
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
                url = "http://localhost:8080/app/videos/operation/stop"
                r = requests.post(url)
                speak_text = "stop video " + search_text.lower() + ", done."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://localhost:8080/app/videos/operation/stop?loop=true&oveSectionId=" + sectionID
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
                url = "http://localhost:8080/app/videos/operation/play"
                r = requests.post(url)
                speak_text = "视频播放 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://localhost:8080/app/videos/operation/play?loop=true&oveSectionId=" + sectionID
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
                url = "http://localhost:8080/app/videos/operation/pause"
                r = requests.post(url)
                speak_text = "视频暂停 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://localhost:8080/app/videos/operation/pause?loop=true&oveSectionId=" + sectionID
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
                url = "http://localhost:8080/app/videos/operation/mute"
                r = requests.post(url)
                speak_text = "视频静音 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://localhost:8080/app/videos/operation/mute?loop=true&oveSectionId=" + sectionID
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
                url = "http://localhost:8080/app/videos/operation/stop"
                r = requests.post(url)
                speak_text = "视频停止 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            elif search_text.isdigit():
                sectionID = search_text
                url = "http://localhost:8080/app/videos/operation/stop?loop=true&oveSectionId=" + sectionID
                r = requests.post(url)
                speak_text = "视频停止 " + search_text.lower() + ",完成."
                tts.speak(speak_text=speak_text,language=lang)
                
            else:
                speak_text = "错误的视频操作，请重新命令"
                tts.speak(speak_text=speak_text,language=lang)
                
            
        
        else:
            speak_text = ""
            
            
            
            
            
            
            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    