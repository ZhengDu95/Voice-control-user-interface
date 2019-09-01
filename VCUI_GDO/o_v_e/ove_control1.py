import webbrowser
import requests
import json

from speech_to_text import stt
from text_to_speech import tts
import conf

def ove_launch_func(lang):
    if lang.lower() == 'chinese':
        speak_text = "进入OVE 控制并打开"
        
    else:
        speak_text = "Enter the control of OVE and launch"
    
    tts.speak(speak_text=speak_text,language=lang)
        
    url = 'http://localhost:9080'
    try:
        webbrowser.open(url)
    except Exception as e:
        print("OVE core open error:",e)  
        


def ove_launch_image_func(lang):   
    if lang.lower() == 'english':
        speak_text = "welcome to launch the image application"
        tts.speak(speak_text=speak_text,language=lang)
        
        url = 'http://localhost:9080/app/images'
        try:
            webbrowser.open(url)
        except Exception as e:
            print("OVE core open error:",e)  
        
        #update space 
        speak_text = "which space do you choose, local nine or local four"
        tts.speak(speak_text=speak_text,language=lang)
    
    else:
        speak_text = "欢迎使用OVE图像应用"
        tts.speak(speak_text=speak_text,language=lang)
        
        url = 'http://localhost:9080/app/images'
        try:
            webbrowser.open(url)
        except Exception as e:
            print("OVE core open error:",e)  
        
        #update space 
        speak_text = "请问您想用九屏显示器或者四屏显示器观看"
        tts.speak(speak_text=speak_text,language=lang)
        
      
        
        
def ove_launch_image_space_func(text,lang):  
    space = text
    print(space)
    
    if lang.lower() == 'english':
        if(space.lower() == 'image 9'):
            #send post request to image application
            headers = {'Content-Type': 'application/json'}
            payload = {"space": "DOCluster","x":"0","y":"0","w":"4320","h":"2424","app":{"url":"http://gdo-appsdev.dsi.ic.ac.uk:9080/app/images","states":{"load":"Highsmith"}}}
            r = requests.post("url", data=json.dumps(payload), headers = headers)
            ControlID = json.loads(r.text)
                
            url = 'http://gdo-appsdev.dsi.ic.ac.uk:9080/app/images/control.html?oveSectionId=' + str(ControlID['id'])
            try:
                webbrowser.open(url)
            except Exception as e:
                print("OVE image controller webpage open error:",e)  
        
            speak_text = "please choose which viewer you want to see, zero to eight"
            tts.speak(speak_text=speak_text,language=lang)
        
            #conf.SPACE = "LocalNine"
            
    
        elif(space.lower() == 'image 4'):
            headers = {'Content-Type': 'application/json'}
            payload = {"space":"LocalFour","x":"0","y":"0","w":"2880","h":"1616","app":{"url":"http://gdo-appsdev.dsi.ic.ac.uk:9080/app/images","states":{"load":"Highsmith"}}}
            r = requests.post("http://gdo-appsdev.dsi.ic.ac.uk:9080/section", data=json.dumps(payload), headers = headers)
            ControlID = json.loads(r.text)
            
            url = 'http://gdo-appsdev.dsi.ic.ac.uk:9080/app/images/control.html?oveSectionId=' + str(ControlID['id'])
            try:
                webbrowser.open(url)
            except Exception as e:
                print("OVE image controller webpage open error:",e)  
        
            speak_text = "please choose which viewer you want to see, zero to three"
            tts.speak(speak_text=speak_text,language=lang)
        
            #conf.SPACE = "LocalFour"
    
        else: 
            speak_text = "wrong image space choices, please choose again, local nine or local four"
            tts.speak(speak_text=speak_text,language=lang)

    # chinese version
    else:
        if(space == '屏幕9'):
            #send post request to image application
            headers = {'Content-Type': 'application/json'}
            payload = {"space": "LocalNine","x":"0","y":"0","w":"4320","h":"2424","app":{"url":"http://gdo-appsdev.dsi.ic.ac.uk:9080/app/images","states":{"load":"Highsmith"}}}
            r = requests.post("http://gdo-appsdev.dsi.ic.ac.uk:9080/section", data=json.dumps(payload), headers = headers)
            ControlID = json.loads(r.text)
                
            url = 'http://gdo-appsdev.dsi.ic.ac.uk:9080/app/images/control.html?oveSectionId=' + str(ControlID['id'])
            try:
                webbrowser.open(url)
            except Exception as e:
                print("OVE image controller webpage open error:",e)  
        
            speak_text = "请选择您想用哪一个显示器观看，分屏零到分屏八"
            tts.speak(speak_text=speak_text,language=lang)
        
            conf.SPACE = "LocalNine"
            
    
        elif(space == '屏幕4'):
            headers = {'Content-Type': 'application/json'}
            payload = {"space":"LocalFour","x":"0","y":"0","w":"2880","h":"1616","app":{"url":"http://gdo-appsdev.dsi.ic.ac.uk:9080/app/images","states":{"load":"Highsmith"}}}
            r = requests.post("http://gdo-appsdev.dsi.ic.ac.uk:9080/section", data=json.dumps(payload), headers = headers)
            ControlID = json.loads(r.text)
            
            url = 'http://gdo-appsdev.dsi.ic.ac.uk:9080/app/images/control.html?oveSectionId=' + str(ControlID['id'])
            try:
                webbrowser.open(url)
            except Exception as e:
                print("OVE image controller webpage open error:",e)  
        
            speak_text = "请选择您想用哪一个显示器观看，分屏零到分屏三"
            tts.speak(speak_text=speak_text,language=lang)
        
            conf.SPACE = "LocalFour"
    
        else: 
            speak_text = "错误的屏幕选择，请重新选择，九屏或者四屏"
            tts.speak(speak_text=speak_text,language=lang)
        
        
        
        
def ove_launch_view_section_func(text,lang):
    Viewsection = text
    print(Viewsection)
    
    if lang.lower() == 'english':
        speak_text = "you are using the viewer " + Viewsection + ", enjoy"
        tts.speak(speak_text=speak_text,language=lang)
    else:
        speak_text = "您正在使用显示器" + Viewsection + ", 观影愉快"
        tts.speak(speak_text=speak_text,language=lang)
    
    
    if(conf.SPACE == "LocalNine"):
        url = 'http://localhost:9080/view.html?oveViewId=LocalNine-' + Viewsection
        try:
            webbrowser.open(url)
        except Exception as e:
            print("OVE controller webpage open error:",e)  
            
            
    elif(conf.SPACE == "LocalFour"):
        url = 'http://localhost:9080/view.html?oveViewId=LocalFour-' + Viewsection
        try:
            webbrowser.open(url)
        except Exception as e:
            print("OVE controller webpage open error:",e)  
           
    else:        
        speak_text = "wrong viewer section choices"
        tts.speak(speak_text=speak_text,language=lang)
        
    
def ove_delete_func(lang):
    if lang.lower() == 'english':
        speak_text = "Do you want to delete all sections or section with i d n"
        tts.speak(speak_text=speak_text,language=lang)
    else:
        speak_text = "您想要删掉全部或者删掉id等于n的部分"
        tts.speak(speak_text=speak_text,language=lang)
    
    url = 'http://localhost:9080'
    try:
        webbrowser.open(url)
    except Exception as e:
        print("OVE core open error:",e)

def ove_delete_sections_func(text, lang):
    if lang.lower() == 'english':
        if text == "delete all":
            headers = {'Content-Type': 'application/json'}
            url = "http://gdo-appsdev.dsi.ic.ac.uk:9080/sections"
            r = requests.delete(url, headers = headers)
            speak_text = "it successfully deletes all sections"
            tts.speak(speak_text=speak_text,language=lang)
            
            conf.SPACE = ''
            
        else:
            sectionID = str(text[3])
            headers = {'Content-Type': 'application/json'}
            url = "http://gdo-appsdev.dsi.ic.ac.uk:9080/sections/" + sectionID
            r = requests.delete(url, headers = headers)
            speak_text = "it successfully deletes section with i d " + sectionID
            tts.speak(speak_text=speak_text,language=lang)
            
            conf.SPACE = ''
            
    else :
        if text == "全部删除":
            headers = {'Content-Type': 'application/json'}
            url = "http://gdo-appsdev.dsi.ic.ac.uk:9080/sections"
            r = requests.delete(url, headers = headers)
            speak_text = "成功删除所有部分"
            tts.speak(speak_text=speak_text,language=lang)
            
            conf.SPACE = ''
            
        else:
            sectionID = str(text[2])
            headers = {'Content-Type': 'application/json'}
            url = "http://gdo-appsdev.dsi.ic.ac.uk:9080/sections/" + sectionID
            r = requests.delete(url, headers = headers)
            speak_text = "成功删除部分" + sectionID
            tts.speak(speak_text=speak_text,language=lang)
            
            conf.SPACE = ''
        
        
        
    url1 = 'http://localhost:9080'
    try:
        webbrowser.open(url1)
    except Exception as e:
        print("OVE core open error:",e)
        
            
    
            
        
        



