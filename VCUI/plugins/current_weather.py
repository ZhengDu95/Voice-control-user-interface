
import requests

from text_to_speech import tts

def current_weather_func(lang):
    api_key = '4e0b3bce5ba5fdc8bd92ef1257460df4'

    current_location_info = requests.get('https://ipinfo.io/json/?token=4361d58fa32061').json()
    region = current_location_info['region']

    link = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}".format(city=region,api_key=api_key)
    weather_data = requests.get(link).json()

    kelvin_to_celsius = lambda x: round(x-273.15)

    temp = kelvin_to_celsius(weather_data['main']['temp'])
    max_temp = weather_data['main']['temp_max']
    description = weather_data['weather'][0]['description']

    if lang.lower() == 'chinese':
        msg = '现在 {} 温度为 {} 摄氏度和 {}'.format(region,temp,description)
    else:
        msg = 'Right now in {} its {} degree celsius and {}'.format(region,temp,description)
    
    print(msg)
    tts.speak(speak_text=msg, language=lang)