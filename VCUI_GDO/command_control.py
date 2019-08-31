import logging

from plugins import speak_time, speak_date, read_email, search_mail, translate, current_weather, google_search
from o_v_e   import ove_control, ove_video, ove_image

from text_to_speech import tts


LOG_FORMAT = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="debug.log",level=logging.DEBUG,format=LOG_FORMAT,filemode="w",)
logger = logging.getLogger(__name__)



def input_parser(commands_list, selected_lang, command, profile_info):
    """
    Find index number of mathing command.
    """
    
    index = None

    # TODO: Make this code less repetitively 
    # Find index number of matching chinese command
    if selected_lang.lower() == 'chinese':
        for cmd in commands_list['chinese']:
            if command in cmd.split(';'):
                index = commands_list['chinese'].index(cmd)
                break
    # Find index number of matching english command
    else:
        for cmd in commands_list['english']:
            if command.lower() in cmd.split(';'):
                print("match")
                index = commands_list['english'].index(cmd)
                break

    # If command are found then search for task by index number           
    if isinstance(index, int):
        no_error = True

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

            if commands_list['task'][index] == 'translate':
                translate.translate_func(lang=selected_lang)

            if commands_list['task'][index] == 'current weather':
                current_weather.current_weather_func(lang=selected_lang)
            
            if commands_list['task'][index] == 'google search':
                google_search.google_search_func(lang=selected_lang)
               
                
            
            #Control of OVE
            if commands_list['task'][index] == 'control ove':
                ove_control.ove_launch_func(lang=selected_lang)
            
            if commands_list['task'][index] == 'mode space':
                ove_control.ove_launch_mode_space_func(text=command,lang=selected_lang)
                
            
                
            # for image application    
            if commands_list['task'][index] == 'control image':
                ove_image.ove_launch_image_func(lang=selected_lang)
            
            if commands_list['task'][index] == 'image operation':
                ove_image.ove_image_operation_func(text=command,lang=selected_lang)
                
                
                
            #for video application
            if commands_list['task'][index] == 'control video':
                ove_video.ove_launch_video_func(lang=selected_lang)
            
            if commands_list['task'][index] == 'video operation':
                ove_video.ove_video_operation_func(text=command,lang=selected_lang)
                
                
                
            
            #for delete operations
            if commands_list['task'][index] == 'delete':
                ove_control.ove_delete_func(lang = selected_lang)
            
            if commands_list['task'][index] == 'delete sections':
                ove_control.ove_delete_sections_func(text=command,lang = selected_lang)
            

            
    else:
        tts.speak(speak_text="Sorry! Wrong command", language='english')

