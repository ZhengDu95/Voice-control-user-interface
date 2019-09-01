import webbrowser
import requests
import json

from speech_to_text import stt
from text_to_speech import tts

def ove_launch_func(lang):
    if lang.lower() == 'chinese':
        speak_text = "进入OVE 控制并打开"
        
    else:
        speak_text = "Enter the control of OVE and launch"
    
    tts.speak(speak_text=speak_text,language=lang)
        
    url = 'http://localhost:8080'
    try:
        webbrowser.open(url)
    except Exception as e:
        print("OVE core open error:",e)  
        


def ove_launch_image_func(lang):
    space = ''
    Viewsection = ''
    
    if lang.lower() == 'english':
        speak_text = "welcome to launch the image application"
        tts.speak(speak_text=speak_text,language=lang) 
        
        """
        url = 'http://localhost:8080/app/images'
        try:
            webbrowser.open(url)
        except Exception as e:
            print("OVE core open error:",e)  
        """
        
        #update space 
        speak_text = "which space do you choose, localnine or localfour"
        tts.speak(speak_text=speak_text,language=lang)
        
        search_text = stt.stt_func(selected_lang=lang)
        
        while(search_text.lower() != 'local nine' 
              and search_text.lower() != 'local four'):
            speak_text = "can not recognize, speak again, localnine or localfour"
            tts.speak(speak_text=speak_text,language=lang)
            search_text = stt.stt_func(selected_lang=lang)
        
        if(search_text.lower() == 'local nine'):
            space = 'LocalNine'
            #send post request to image application 
            headers = {'Content-Type': 'application/json'}
            payload = {"space": space,"x":"0","y":"0","w":"4320","h":"2424","app":{"url":"http://146.169.220.4:8080/app/images","states":{"load":"Highsmith"}}}
            r = requests.post("http://146.169.220.4:8080/section", data=json.dumps(payload), headers = headers)
            ControlID = json.loads(r.text)
            
            url = 'http://146.169.220.4:8080/app/images/control.html?oveSectionId=' + str(ControlID['id'])
            try:
                webbrowser.open(url)
            except Exception as e:
                print("OVE image controller webpage open error:",e)  
            
            
            # round 2: which section to view
            speak_text = "which view section do you choose"
            tts.speak(speak_text=speak_text,language=lang)
        
            search_text = stt.stt_func(selected_lang=lang)
            while(search_text.lower() != 'zero'
              and search_text.lower() != 'one' 
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
        
            if(search_text.lower() == 'zero'):
                Viewsection = '0'
            elif(search_text.lower() == 'one'):
                Viewsection = '1'
            elif (search_text.lower() == 'two'):
                Viewsection = '2'
            elif (search_text.lower() == 'three'):
                Viewsection = '3'
            elif (search_text.lower() == 'four'):
                Viewsection = '4'
            elif (search_text.lower() == 'five'):
                Viewsection = '5'
            elif (search_text.lower() == 'six'):
                Viewsection = '6'
            elif (search_text.lower() == 'seven'):
                Viewsection = '7'
            else:
                Viewsection = '8'
                
            url = 'http://localhost:8080/view.html?oveViewId=LocalNine-' + Viewsection
            try:
                webbrowser.open(url)
            except Exception as e:
                print("OVE image controller webpage open error:",e)  
        
        
        
        
        
        else:
            space = 'LocalFour'
            headers = {'Content-Type': 'application/json'}
            payload = {"space": space,"x":"0","y":"0","w":"2880","h":"1616","app":{"url":"http://146.169.220.4:8080/app/images","states":{"load":"Highsmith"}}}
            r = requests.post("http://146.169.220.4:8080/section", data=json.dumps(payload), headers = headers)
            ControlID = json.loads(r.text)
            
            url = 'http://146.169.220.4:8080/app/images/control.html?oveSectionId=' + str(ControlID['id'])
            try:
                webbrowser.open(url)
            except Exception as e:
                print("OVE image controller webpage open error:",e)  
            
            
            # round 2: which section to view
            speak_text = "which view section do you choose"
            tts.speak(speak_text=speak_text,language=lang)
        
            search_text = stt.stt_func(selected_lang=lang)
            while(search_text.lower() != 'zero'
              and search_text.lower() != 'one' 
              and search_text.lower() !='two' 
              and search_text.lower() !='three'):
                speak_text = "can not recognize, speak again, which section"
                tts.speak(speak_text=speak_text,language=lang)
                search_text = stt.stt_func(selected_lang=lang)
        
            if(search_text.lower() == 'zero'):
                Viewsection = '0'
            elif(search_text.lower() == 'one'):
                Viewsection = '1'
            elif (search_text.lower() == 'two'):
                Viewsection = '2'
            else:
                Viewsection = '3'
                
            url = 'http://localhost:8080/view.html?oveViewId=LocalFour-' + Viewsection
            try:
                webbrowser.open(url)
            except Exception as e:
                print("OVE image controller webpage open error:",e)  
            
            
            
        
        



