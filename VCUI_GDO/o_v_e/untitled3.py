#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:50:29 2019

@author: duzheng
"""
#暂存
if lang.lower() == 'chinese':
        speak_text = "控制并打开图像应用"
        
    else:
        speak_text = "control of OVE and launch the image application"
    
    tts.speak(speak_text=speak_text,language=lang) 
    
    #send post request to image application 
    headers = {'Content-Type': 'application/json'}

    payload = {"space":"LocalNine","x":"0","y":"0","w":"4320","h":"2424","app":{"url":"http://146.169.220.4:8080/app/images","states":{"load":"Highsmith"}}}

    r = requests.post("http://146.169.220.4:8080/section", data=json.dumps(payload), headers = headers)
    
    #jump to image website 
    url2 = 'http://localhost:8080/app/images'
    
    try:
        webbrowser.open(url2)
    except Exception as e:
        print("OVE image webpage open error:",e)  
        
    
    #Second round of conversation
    if lang.lower() == 'chinese':
        speak_text = "您想要打开图像控制器或显示屏"
        
    
    
    else:
        speak_text = "Do you want to open controller or viewer of image application"
        tts.speak(speak_text=speak_text,language=lang) 
    
        search_text = stt.stt_func(selected_lang=lang)
        if search_text.lower() == 'controller':
            
        elif search_text.lower() == 'viewer':
        
        else 


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#update section
        speak_text = "which section do you choose, zero to eight"
        tts.speak(speak_text=speak_text,language=lang)
        
        search_text = stt.stt_func(selected_lang=lang)
        
        while(search_text.lower() != 'one' 
              and search_text.lower() !='two' 
              and search_text.lower() !='three' 
              and search_text.lower() !='four' 
              and search_text.lower() !='five' 
              and search_text.lower() !='six' 
              and search_text.lower() !='seven' 
              and search_text.lower() !='eight'):
            speak_text = "can not recognize, speak again, which section"
            tts.speak(speak_text=speak_text,language=lang)
            search_text = stt.stt_func(selected_lang=lang)
        
        if(search_text.lower() == 'one'):
            section = '1'
        elif (search_text.lower() == 'two'):
            section = '2'
        elif (search_text.lower() == 'three'):
            section = '3'
        elif (search_text.lower() == 'four'):
            section = '4'
        elif (search_text.lower() == 'five'):
            section = '5'
        elif (search_text.lower() == 'six'):
            section = '6'
        elif (search_text.lower() == 'seven'):
            section = '7'
        else:
            section = '8'
            
        #choose controller or viewer
        