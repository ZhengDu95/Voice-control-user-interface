import sys
import logging

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

from plugins import speak_time, speak_date, read_email, search_mail, open_folder, translate, current_weather, google_search
from text_to_speech import tts
import password_check


LOG_FORMAT = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="debug.log",level=logging.DEBUG,format=LOG_FORMAT,filemode="w",)
logger = logging.getLogger(__name__)



def input_parser(commands_list, selected_lang, command, profile_info):
    """
    Find index number of mathing command.
    """
    
    index = None

    # TODO: Make this code less repetitively 
    # Find index number of matching bengali command
    if selected_lang.lower() == 'chinese':
        # Custom  bengali commands
        for cus_cmd in commands_list['custom']:
            if command == cus_cmd:
                index = commands_list['custom'].index(cus_cmd)
                break
        else:
            for cmd in commands_list['chinese']:
                if command in cmd.split(';'):
                    index = commands_list['chinese'].index(cmd)
                    break
    # Find index number of matching english command
    else:
        for cus_cmd in commands_list['custom']:
            if command.lower() == cus_cmd:
                index = commands_list['custom'].index(cus_cmd)
                break
        else:
            for cmd in commands_list['english']:
                if command.lower() in cmd.split(';'):
                    print("match")
                    index = commands_list['english'].index(cmd)
                    break

    # If command are found then search for task by index number           
    if isinstance(index, int):
        no_error = True
        # print('index:',index)
        # print(commands_list['task'][index])

        if commands_list['security'][index].lower() == 'y':
            
            match_obj = password_check.PasswordCheckDialog()
            match = match_obj.check()
            # print('password Match:',match)
            if not match:
                no_error = False
                tts.speak(speak_text="Incorrect password. Please Try again.", language='english')
            # TODO: If password not match then ask password again
        

        if no_error:
            if commands_list['task'][index] == 'greeting':
                greetings.greeting_func(text=command,lang=selected_lang)

            if commands_list['task'][index] == 'time':
                speak_time.time_func(text=command,lang=selected_lang)
            
            if commands_list['task'][index] == 'date':
                speak_date.date_func(text=command,lang=selected_lang)
            
            if commands_list['task'][index] == 'email':
                read_email.main(text=command,lang=selected_lang)

            if commands_list['task'][index] == 'search email':
                search_mail.main(text=command,lang=selected_lang)

            if commands_list['task'][index] == 'open folder':
                open_folder.main(text=command,lang=selected_lang)

            if commands_list['task'][index] == 'translate':
                translate.translate_func(lang=selected_lang)

            if commands_list['task'][index] == 'current weather':
                current_weather.current_weather_func(lang=selected_lang)
            
            if commands_list['task'][index] == 'google search':
                google_search.google_search_func(lang=selected_lang)

            
    else:
        tts.speak(speak_text="Sorry! Wrong command", language='english')

