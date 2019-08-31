import datetime

from text_to_speech import tts

chinese_weekday_name = ["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]

def date_format(datetime_obj,lang):
    if lang == 'chinese':
        today = chinese_weekday_name[datetime_obj.weekday()] + str(datetime_obj.strftime( '%d, %B %Y'))
    else:
        today = str(datetime_obj.strftime('it is %A, %d, %B %Y'))
    return today


def date_func(text, lang):
    now = datetime.datetime.now()
    today_date = date_format(now, lang)
    tts.speak(speak_text=today_date, language=lang)


"""
TODO:
tell whats the day.
"""
