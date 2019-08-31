
import pickle
import os.path
from pathlib import Path
from collections import OrderedDict

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QRadioButton,
            QGridLayout, QVBoxLayout, QHBoxLayout,QDialog, QLabel, QMessageBox,
            QInputDialog, QLineEdit,QTableWidget, QTableWidgetItem)


from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot 

from text_to_speech import tts
from speech_to_text import stt
import conf



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main(text,lang):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """

    search_email = InputSearchEmailkDialog().input_email()
    print("Return class",search_email)
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            file_path = os.getcwd()+'/plugins/client_id.json' # clieent_id.json download from gmail api account
            flow = InstalledAppFlow.from_client_secrets_file(
                file_path, SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    # category_personal =  service.user().labels.get(userId='me',labelIds='')
    category_personal = service.users().messages().list(userId='me', includeSpamTrash=False, labelIds = ['CATEGORY_PERSONAL'], q='from:{} is:unread'.format(search_email)).execute()
    category_personal_messages_id = category_personal.get('messages', [])
   

    # if there have not any unread message
    if not category_personal_messages_id:
        if lang.lower() == 'chinese':
            speak_text = '已无未读信息'
        else:
            speak_text = "There are no unread message"
        
        tts.speak(speak_text=speak_text, language=lang)

    else:
        total_unread_msg = len(category_personal_messages_id)

        if lang.lower() == 'chinese':
            speak_text = "全部未读信息".format(total_unread_msg)
            asking_text = "如果您想查阅未读信息请说是不然说否"
        else:
            speak_text = "Total unread message:{}".format(total_unread_msg)
            asking_text = "If you want to see unread message then say yes otherwise say no"
        
        tts.speak(speak_text=speak_text, language=lang)
        tts.speak(speak_text=asking_text, language=lang)

        response =  stt.stt_func(selected_lang=lang)

        if response in ['yes','是']:
            personal_message_info = OrderedDict()

            personal_message_info['snippet'] = []
            personal_message_info['from'] = []
            personal_message_info['date'] = []
            personal_message_info['link'] = []
    

            for msg_id in category_personal_messages_id:
                msg = service.users().messages().get(userId='me', id=msg_id['id']).execute()
                msg_headers = msg['payload']['headers']
                personal_message_info['snippet'].append(msg['snippet'])

                from_email = [header['value'] for header in msg_headers if header['name']=='From']
                personal_message_info['from'].append(from_email[0])

                msg_date = [header['value'] for header in msg_headers if header['name']=='Date']
                personal_message_info['date'].append(msg_date[0])

                msg_link = 'https://mail.google.com/mail/u/0/#inbox/'+msg_id['id']
                personal_message_info['link'].append(msg_link)

            col_size = len(personal_message_info)
            row_size = len(personal_message_info['snippet'])
            column_names = list(personal_message_info.keys())
            row_values = list(personal_message_info.values())
            
            table_obj = TableWindow(row_values, column_names, row_size, col_size)
            if table_obj.exec_():
                table_obj.quit()


class TableWindow(QDialog):
    def __init__(self, row_values, column_names, row_size, col_size):
        """ 
        Initiate table properties
        
        row_values(list): example [[1,2,3],[2,3,4].....]
        column_names(list): all column names into list
        row_size(int): total row
        col_size(int): total column
        """
        super().__init__()
        self.row_values = row_values
        self.column_names = column_names
        self.row = row_size
        self.col = col_size
        
        self.init_table()

    def init_table(self):
        self.setWindowTitle("Show Table")
        self.setGeometry(50, 10, 600, 600) # TODO: make responsive table

        self.table = QTableWidget()

        # set row count
        self.table.setRowCount(self.row)
        
        # set column count
        self.table.setColumnCount(self.col)

        
        # table headline
        self.table.setHorizontalHeaderLabels(self.column_names)


        for r in range(self.row):
            for c in range(self.col):
                
                item = QTableWidgetItem(self.row_values[c][r])
                # if column_names[j] == 'security': print("security",row_values[j][i] )
                self.table.setItem(r, c, QTableWidgetItem(self.row_values[c][r]))
                    
       

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        
        self.v_lay = QVBoxLayout()
        self.setLayout(self.v_lay)

        self.v_lay.addWidget(self.table)

        self.show()




class InputSearchEmailkDialog(QWidget):
    """ Take search email in input dialog and check it is valid or not """

    def __init__(self):
        super().__init__()
        self.title = 'Insert person email'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    # TODO: ensure that user enter valid email address
    def input_email(self):
        
        text, okPressed = QInputDialog.getText(self, "Enter the person email","email:", QLineEdit.Normal, "")
        
        if okPressed and text != '':
            print(text)
        
        return text

    def quit(self):
        self.destroy()
