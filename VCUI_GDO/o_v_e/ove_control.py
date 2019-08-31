#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 08:45:36 2019

@author: duzheng
"""
import webbrowser
import requests
import json

from speech_to_text import stt
from text_to_speech import tts
import conf

def ove_launch_func(lang):
    if lang.lower() == 'chinese':
        speak_text = "进入OVE 控制并打开并选择一个模式，DO Cluster 或者 DO Section"
        
    else:
        speak_text = "Enter the control of OVE and launch and choose a mode DO Cluster or DO Section"
    
    tts.speak(speak_text=speak_text,language=lang)
        
    url = 'http://localhost:8080'
    try:
        webbrowser.open(url)
    except Exception as e:
        print("OVE core open error:",e)  




def ove_launch_mode_space_func(text,lang):    
    if lang.lower() == 'english':
        #change the mode to user's choice
        if(text.lower() == 'cluster'):
            #r = request.get("url-for-DOCluster")
            
            conf.SPACE  = "DOCluster"
            #conf.URL = "url-for-DOCluster"
            
            speak_text = "Welcome to use DO Cluster mode, please choose an application to load"
            tts.speak(speak_text=speak_text,language=lang)
            
 
    
        elif(text.lower() == 'section'):
            #r = request.get("url-for-DOSection")
            
            conf.SPACE  = "DOSection"
            #conf.URL = "url-for-DOSection"
            
            speak_text = "Welcome to use DO Section mode, please choose an application to load"
            tts.speak(speak_text=speak_text,language=lang)

        else: 
            speak_text = "Wrong choices, please choose mode again"
            tts.speak(speak_text=speak_text,language=lang)
            

    # chinese version
    else:
        #change the mode to user's choice
        if(text == '模式1'):
            #r = request.get("url-for-DOCluster")
            
            conf.SPACE  = "DOCluster"
            #conf.URL = "url-for-DOCluster"
            
            speak_text = "欢迎来到云屏模式1，请选择加载一个应用"
            tts.speak(speak_text=speak_text,language=lang)
            
 
    
        elif(text == '模式2'):
            #r = request.get("url-for-DOSection")
            
            conf.SPACE  = "DOSection"
            #conf.URL = "url-for-DOSection"
            
            speak_text = "欢迎来到云屏模式2，请选择加载一个应用"
            tts.speak(speak_text=speak_text,language=lang)

        else: 
            speak_text = "错误的选择，请重新选择模式"
            tts.speak(speak_text=speak_text,language=lang)
            
        

   
    

def ove_delete_func(lang):
    if lang.lower() == 'english':
        speak_text = "Do you want to delete all sections or section with i d n"
        tts.speak(speak_text=speak_text,language=lang)
    else:
        speak_text = "您想要删掉全部或者删掉id等于n的部分"
        tts.speak(speak_text=speak_text,language=lang)
    
    url = 'http://localhost:8080'
    try:
        webbrowser.open(url)
    except Exception as e:
        print("OVE core open error:",e)
        
        

def ove_delete_sections_func(text, lang):
    url_delete = "http://" + conf.URL  
    
    if lang.lower() == 'english':
        if text == "delete all":
            headers = {'Content-Type': 'application/json'}
            url = url_delete + "/sections"
            r = requests.delete(url, headers = headers)
            speak_text = "it successfully deletes all sections"
            tts.speak(speak_text=speak_text,language=lang)
            
            conf.SPACE = None
            
        else:
            sectionID = str(text[3])
            headers = {'Content-Type': 'application/json'}
            url = url_delete + "/sections/" + sectionID
            r = requests.delete(url, headers = headers)
            speak_text = "it successfully deletes section with i d " + sectionID
            tts.speak(speak_text=speak_text,language=lang)
            
            conf.SPACE = None
            
    else :
        if text == "全部删除":
            headers = {'Content-Type': 'application/json'}
            url = url_delete + "/sections"
            r = requests.delete(url, headers = headers)
            speak_text = "成功删除所有部分"
            tts.speak(speak_text=speak_text,language=lang)
            
            conf.SPACE = None
            
        else:
            sectionID = str(text[2])
            headers = {'Content-Type': 'application/json'}
            url = url_delete + "/sections/" + sectionID
            r = requests.delete(url, headers = headers)
            speak_text = "成功删除部分" + sectionID
            tts.speak(speak_text=speak_text,language=lang)
            
            conf.SPACE = None
            
        
        
    url1 = 'http://localhost:8080'
    try:
        webbrowser.open(url1)
    except Exception as e:
        print("OVE core open error:",e)     
            
            
            
            
            
            