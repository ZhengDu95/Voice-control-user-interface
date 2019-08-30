import webbrowser

from speech_to_text import stt
from text_to_speech import tts

def google_search_func(lang):
    if lang.lower() == 'chinese':
        speak_text = "您想知道什么"
        
    else:
        speak_text = "What do you want to know"
        
    tts.speak(speak_text=speak_text,language=lang)

    search_text = stt.stt_func(selected_lang=lang)
    
    if search_text.lower() == 'can not recognize':
        speak_text="Check your internet connection and try again"
        tts.speak(speak_text=speak_text,language=lang)
    else:
        link = 'https://www.google.com/search?q={}'.format(search_text)
        try:
            webbrowser.open(link)
        except Exception as e:
            print("google_search error:",e)