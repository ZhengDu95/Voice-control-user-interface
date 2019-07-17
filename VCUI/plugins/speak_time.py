import datetime

from text_to_speech import tts

def time_format(datetime_obj):
    return str(datetime_obj.strftime("%I:%M%p"))


def time_func(text, lang):
    now = datetime.datetime.now()

    text = time_format(now) # TODO: Show this into chat box
   
    tts.speak(speak_text=text, language=lang)
