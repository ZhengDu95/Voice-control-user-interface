##−∗−coding :  utf−8−∗−
import speech_recognition as sr
import os
import logging

LogFormat = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="test.log", filemode="w", level=logging.DEBUG, format=LogFormat)
logger = logging.getLogger(__name__)

def stt_func(selected_lang):
    
    r = sr.Recognizer()
    text = None

    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1   
        r.adjust_for_ambient_noise(source, duration=1)
        print(r.energy_threshold)
        os.system("beep.mp3") #play the notification sound
        print("Please Say Something.")
        r.energy_threshold += 280
        audio = r.listen(source)
        print("Over! Starting recognize.....")

    try:
        
        if selected_lang.lower() == 'chinese':
            speech_text = r.recognize_google(audio, language='zh')
            logger.debug(str(speech_text.encode()))

            text_into_byte = speech_text.encode('utf-8')

            # b'\xe0\xa7\x9f' = য়  ???
            normalized_text_byte = text_into_byte.replace(b'\xe0\xa6\xaf\xe0\xa6\xbc', b'\xe0\xa7\x9f')
            text = normalized_text_byte.decode('utf-8')
            
        elif selected_lang.lower() == 'english':
            text = r.recognize_google(audio, language='en-US')
        
        else:
            pass
       
        #with open('output.txt','w') as f:
        #    print("convertor:{}\n{}".format(en_text,bn_text), file=f)  
        #print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language='bn-BD'))
        
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))

    if text:
        print("Google Cloud Speech thinks you said: " + text)  
    else:
        text = "Can not Recognize."
        print(text)

    return text
