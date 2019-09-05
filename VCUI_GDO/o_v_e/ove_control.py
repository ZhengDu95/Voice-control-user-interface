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
import time

def ove_launch_func(lang):
    if lang.lower() == 'chinese':
        speak_text = "进入OVE 控制并打开并选择一个模式，DO Cluster 或者 DO Section"
        
    else:
        speak_text = "Enter the control of OVE and launch and choose a mode DO Cluster or DO Section"


    url = "http://" + conf.URL
    try:
        webbrowser.open(url)
    except Exception as e:
        print("OVE core open error:",e) 
    
    tts.speak(speak_text=speak_text,language=lang)




def ove_launch_mode_space_func(text,lang):   
    if lang.lower() == 'english':
        #change the mode to user's choice
        if(text.lower() == 'space cluster' or 'choose cluster' or'open cluster'):
            #r = requests.post("")
            
            conf.SPACE  = "DOCluster"
            
            speak_text = "Welcome to use DO Cluster mode, please choose an application to load"
            tts.speak(speak_text=speak_text,language=lang)
            
 
    
        elif(text.lower() == 'space section'or'choose cection' or'open section'):
            #r = requests.post("")
            
            conf.SPACE  = "DOSection"
            
            speak_text = "Welcome to use DO Section mode, please choose an application to load"
            tts.speak(speak_text=speak_text,language=lang)

        else: 
            speak_text = "Wrong choices, please choose mode again"
            tts.speak(speak_text=speak_text,language=lang)
            

    # chinese version
    else:
        #change the mode to user's choice
        if(text == '模式1'or'选择模式1' or'打开模式1'):
            #r = requests.post("")
            
            conf.SPACE  = "DOCluster"
            
            speak_text = "欢迎来到云屏模式1，请选择加载一个应用"
            tts.speak(speak_text=speak_text,language=lang)
            
 
    
        elif(text == '模式2' or '模式二'or'选择模式2' or'打开模式2'):
            #r = requests.post("")
            
            conf.SPACE  = "DOSection"
            
            speak_text = "欢迎来到云屏模式2，请选择加载一个应用"
            tts.speak(speak_text=speak_text,language=lang)

        else: 
            speak_text = "错误的选择，请重新选择模式"
            tts.speak(speak_text=speak_text,language=lang)
            
        

   
    

def ove_delete_func(lang):
    url_delete = "http://" + conf.URL  
    
    if lang.lower() == 'english':
        speak_text = "Do you want to delete all sections or section with id n"
        tts.speak(speak_text=speak_text,language=lang)
        search_text = stt.stt_func(selected_lang=lang)

        if search_text == "delete all":
            headers = {'Content-Type': 'application/json'}
            url = url_delete + "/sections"
            r = requests.delete(url, headers = headers) 
            speak_text = "it successfully deletes all sections"
            tts.speak(speak_text=speak_text,language=lang)
    
        elif search_text.isdigit():
            sectionID = search_text
            headers = {'Content-Type': 'application/json'}
            url = url_delete + "/sections/" + sectionID
            r = requests.delete(url, headers = headers) 
            speak_text = "it successfully deletes section with id " + sectionID
            tts.speak(speak_text=speak_text,language=lang)
        else:
            speak_text = "wrong delete operations; try agian."
            tts.speak(speak_text=speak_text,language=lang)
            
            
            
    else:
        speak_text = "您想要删掉全部或者删掉id等于n的部分"
        tts.speak(speak_text=speak_text,language=lang)
        search_text = stt.stt_func(selected_lang=lang)
        if search_text == "全部删除":
            headers = {'Content-Type': 'application/json'}
            url = url_delete + "/sections"
            r = requests.delete(url, headers = headers)
            speak_text = "成功删除所有部分"
            tts.speak(speak_text=speak_text,language=lang)
        
        elif search_text.isdigit():
            sectionID = search_text
            headers = {'Content-Type': 'application/json'}
            url = url_delete + "/sections/" + sectionID
            r = requests.delete(url, headers = headers) 
            speak_text = "成功删除部分" + sectionID
            tts.speak(speak_text=speak_text,language=lang)
            
            #conf.SPACE = None
            
        else:
            speak_text = "错误的删除操作" + sectionID
            tts.speak(speak_text=speak_text,language=lang)
              
        
        
        
        
    url1 = url = "http://" + conf.URL
    try:
        webbrowser.open(url1)
    except Exception as e:
        print("OVE core open error:",e)     

           

def ove_demo_func(text,lang):
    #some urls are not public, please check for authority when use them.
    #English version 
    url = ''
    url1 =  ''

    if lang.lower() == 'english':
        speak_text = 'please choose a demo to load'
        tts.speak(speak_text=speak_text,language=lang)
            
        search_text = stt.stt_func(selected_lang=lang)
            
        if  search_text.lower() == 'blank':
            url = "http://" + url + "/demo/blank"
            r = requests.post(url)
            speak_text = "play demo " + search_text.lower() + ", done."
            tts.speak(speak_text=speak_text,language=lang)             
            
        elif search_text.lower() == 'logo':
            url = "http://" + url + "/demo/logo"
            r = requests.post(url)
            speak_text = "play demo " + search_text.lower() + ", done."
            tts.speak(speak_text=speak_text,language=lang)
            
        elif search_text.lower() == 'london':
            url = "http://" + url + "/demo/londonmap"
            r = requests.post(url)
            speak_text = "play demo " + search_text.lower() + ", done."
            tts.speak(speak_text=speak_text,language=lang)
            
            time.sleep(5)          
            try:
                webbrowser.open(url1)
            except Exception as e:
                print("OVE demos open error:",e) 
            
            
                
        elif search_text.lower() == 'bitcoin':
            url = "http://" + url + "/demo/bitcoin"
            r = requests.post(url)
            speak_text = "play demo " + search_text.lower() + ", done."
            tts.speak(speak_text=speak_text,language=lang)
            
        elif search_text.lower() == 'silk road':
            url = "http://" + url + "/demo/silkroad"
            r = requests.post(url)
            speak_text = "play demo " + search_text.lower() + ", done."
            tts.speak(speak_text=speak_text,language=lang)
            
            time.sleep(5) 
            try:
                webbrowser.open(url1)
            except Exception as e:
                print("OVE demos open error:",e) 
            
        elif search_text.lower() == 'mars':
            url = "http://" + url + "/demo/marsselfie"
            r = requests.post(url)
            speak_text = "play demo " + search_text.lower() + ", done."
            tts.speak(speak_text=speak_text,language=lang)
            
            time.sleep(5) 
            try:
                webbrowser.open(url1)
            except Exception as e:
                print("OVE demos open error:",e) 
            
        elif search_text.lower() == 'introduction':
            url = "http://" + url + "/demo/dsiintro"
            r = requests.post(url)
            speak_text = "play demo " + search_text.lower() + ", done."
            tts.speak(speak_text=speak_text,language=lang)

     
        else:
            speak_text = "wrong demos operations, try again."
            tts.speak(speak_text=speak_text,language=lang)
            
    #Chinese version 
    else:
        speak_text = "请选择一个主题演示"
        tts.speak(speak_text=speak_text,language=lang)
            
        search_text = stt.stt_func(selected_lang=lang)
            
        if  search_text.lower() == '空白':
            url = "http://" + url + "/demo/blank"
            r = requests.post(url)
            speak_text = "播放片段 " + search_text.lower() + ", 完成."
            tts.speak(speak_text=speak_text,language=lang)             
            
        elif search_text.lower() == '标志':
            url = "http://" + url + "/demo/logo"
            r = requests.post(url)
            speak_text = "播放片段 " + search_text.lower() + ", 完成."
            tts.speak(speak_text=speak_text,language=lang)
            
        elif search_text.lower() == '伦敦':
            url = "http://" + url + "/demo/londonmap"
            r = requests.post(url)
            speak_text = "播放片段 " + search_text.lower() + ", 完成."
            tts.speak(speak_text=speak_text,language=lang)
            
            time.sleep(5) 
            try:
                webbrowser.open(url1)
            except Exception as e:
                print("OVE demos open error:",e) 
                
        elif search_text.lower() == '比特币':
            url = "http://" + url + "/demo/bitcoin"
            r = requests.post(url)
            speak_text = "播放片段 " + search_text.lower() + ", 完成."
            tts.speak(speak_text=speak_text,language=lang)
            
        elif search_text.lower() == '丝绸之路':
            url = "http://" + url + "/demo/silkroad"
            r = requests.post(url)
            speak_text = "播放片段 " + search_text.lower() + ", 完成."
            tts.speak(speak_text=speak_text,language=lang)
            
            time.sleep(5) 
            try:
                webbrowser.open(url1)
            except Exception as e:
                print("OVE demos open error:",e) 
            
        elif search_text.lower() == '火星':
            url = "http://" + url + "/demo/marsselfie"
            r = requests.post(url)
            speak_text = "播放片段 " + search_text.lower() + ", 完成."
            tts.speak(speak_text=speak_text,language=lang)
            
            time.sleep(5) 
            try:
                webbrowser.open(url1)
            except Exception as e:
                print("OVE demos open error:",e) 
            
        elif search_text.lower() == '介绍片':
            url = "http://" + url + "/demo/dsiintro"
            r = requests.post(url)
            speak_text = "播放片段 " + search_text.lower() + ", 完成."
            tts.speak(speak_text=speak_text,language=lang)

     
        else:
            speak_text = "错误的演示指令，请重试."
            tts.speak(speak_text=speak_text,language=lang)
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            
            