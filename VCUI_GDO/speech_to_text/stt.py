##−∗−coding :  utf−8−∗−
import speech_recognition as sr
import os
import logging
import time
from text_to_speech import tts


LogFormat = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="test.log", filemode="w", level=logging.DEBUG, format=LogFormat)
logger = logging.getLogger(__name__)

def stt_func(selected_lang):
    
    r = sr.Recognizer()
    text = None

    with sr.Microphone() as source:
        r.pause_threshold = 0.5   
        r.adjust_for_ambient_noise(source, duration=1)

        #tts.speak(speak_text = "Please Say Something.", language = selected_lang)
        print("Please Say Something.")
        
        #calculate time 
        start = time.time()
        
        r.energy_threshold += 2000 #before is 2000
        audio = r.listen(source)
        print("Over! Starting recognize.....")

    try:
        
        if selected_lang.lower() == 'chinese':
            speech_text = r.recognize_google(audio, language='zh')
            logger.debug(str(speech_text.encode()))

            text_into_byte = speech_text.encode('utf-8')


            normalized_text_byte = text_into_byte.replace(b'\xe0\xa6\xaf\xe0\xa6\xbc', b'\xe0\xa7\x9f')
            text = normalized_text_byte.decode('utf-8')
            
        elif selected_lang.lower() == 'english':
            text = r.recognize_google(audio, language='en')
        
        else:
            pass     
        
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))

    if text:
        print("Google Cloud Speech thinks you said: " + text)  
        end = time.time()
        differ = end - start
        print(differ)
        
    else:
        text = "Can not Recognize."
        print(text)

    return text
