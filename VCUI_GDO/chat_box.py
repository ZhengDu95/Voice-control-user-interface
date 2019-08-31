##−∗−coding :  utf−8−∗−

import sys
import json

from PyQt5.QtGui import QIcon, QFont,QPixmap
import PyQt5.QtCore
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow,
                            QGridLayout, QVBoxLayout, QHBoxLayout,QDialog,
                            QLabel, QMessageBox, QComboBox, QFrame, QSizePolicy,
                            QLineEdit, QTextEdit, QAction, QMenuBar, QPlainTextEdit,
                            QTableWidget, QTableWidgetItem)

#self-defined 
from speech_to_text import stt
from commands_table import TableWindow

import sql
import command_control
import conf

import logging

LOG_FORMAT = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="debug.log",level=logging.DEBUG,format=LOG_FORMAT,filemode="w")
logger = logging.getLogger(__name__)



class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Voice Control User Interface'
        self.left = 20
        self.top = 20
        self.width = 800
        self.height = 480

        self.frame = None
        self.text = ''

        self.initUI()
        
        


    def initUI(self):
        
        try:
            with open('config.local.json') as f:
                conf.JSON_DATA = json.load(f)
        except FileNotFoundError:
            with open('config.json') as f:
                conf.JSON_DATA = json.load(f)

        # {'task': [...], 'english': [....], 'chinese': [....], 'security': [....], 'custom': [....]}
        self.all_commands = sql.run_query(query='SELECT * FROM COMMANDS')
        self.profile_info =  sql.run_query(query="SELECT * from USER")
        
        conf.USER_NAME = self.profile_info['name'][0]
        
        languages = ["english", "chinese"]
        query_result = sql.run_query(query="select language from user") # Return type: Dictionary
        print (query_result)
        
        selected_lang = query_result['language'][0]
        index_no = languages.index(selected_lang.lower()) # Raise : Valuerror unless item is found


        """ ------------------- Design Main Window -------------------- """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        """ ------------------- Combo Box -------------------- """
        self.combo = QComboBox()
        self.combo.addItems(languages)
        self.combo.setCurrentIndex(index_no)


        """ ------------------- Label -------------------- """    
        self.language_label = QLabel('Dialog Box', self)
        self.language_label.setGeometry(50,50,900,100)
        pixmap = QPixmap("/Users/duzheng/Desktop/VCUI/icons/voice1.png").scaled(self.language_label.width(), self.language_label.height())
        self.language_label.setPixmap(pixmap)


        """ ------------------- Text -------------------- """
        # Create Chat Box
        self.chat = QPlainTextEdit()
        self.chat.setFixedSize(600,300)
        self.chat.setReadOnly(True)


        """ ---------------- Button ---------------------- """
        # voice_btn not triggered when enter key pressed
        self.voice_btn = QPushButton(default=False, autoDefault=False)
        self.voice_btn.setFixedSize(80,80)
        self.voice_btn.setStyleSheet("background-color:#3399FF;")
        
        pixmap2 = QPixmap("/Users/duzheng/Desktop/VCUI/icons/voice2.jpg")
        self.voice_btn.setIcon(QIcon(pixmap2))
        self.voice_btn.setIconSize(PyQt5.QtCore.QSize(75, 75));
        

        self.commands_btn = QPushButton('Commands', default=False, autoDefault=False)
        


        """ -------------------- Layout -------------------------- """
        # Add vertical layout
        self.v_layout = QVBoxLayout()  
        self.setLayout(self.v_layout)
        
        self.dia_h_layout = QHBoxLayout()
        self.dia_h_layout.addWidget(self.language_label)
        
        # Add horizontal layout
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.chat)
        self.h_layout.addWidget(self.voice_btn)

        # Tools horizontal layout
        self.tools_h_layout = QHBoxLayout()
        self.tools_h_layout.addWidget(self.combo)
        self.tools_h_layout.addWidget(self.commands_btn)


        self.v_layout.addLayout(self.dia_h_layout)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addLayout(self.tools_h_layout)


        """ ------------------ triggered button ---------------"""
        self.voice_btn.clicked.connect(self.voice_text)
        self.commands_btn.clicked.connect(self.show_table)

        self.show()


    @pyqtSlot()
    def voice_text(self):
        """ Convert voice to text and appear the text into chatbox """
        
        current_lang = self.combo.currentText() # collect selected language from combo box

        if conf.NEW_COMMAND:
            update_commands = sql.run_query(query='SELECT * FROM COMMANDS')
            self.all_commands = update_commands
            conf.NEW_COMMAND = False

        self.text = stt.stt_func(selected_lang=current_lang) 

        self.text_append(self.text)

        self.send_to_command(current_lang)


    def send_to_command(self, current_lang):

        command_control.input_parser(
            commands_list = self.all_commands,
            selected_lang = current_lang,
            command = self.text,
            profile_info = self.profile_info,
            )

        self.text = ''

    
    def text_append(self, text):
        """ Show USER speech_to_text into window """

        textFormatted='<b>{}: </b><span style=" font-size:12pt; font-weight:600; color:#33c4ff;">{}</span>'.format(conf.USER_NAME.capitalize(),text)
        self.chat.appendHtml(textFormatted)
        # Make pulic of chat object so that we can use this object from other file by conf.CHAT_OBJ
        conf.CHAT_OBJ = self.chat 
        


    @pyqtSlot()
    def show_table(self):
        """ Show all command list into table """
        
        if conf.NEW_COMMAND:
            update_commands = sql.run_query(query='SELECT * FROM COMMANDS')
            self.all_commands = update_commands
            conf.NEW_COMMAND = False

        column_names = tuple(self.all_commands.keys())
        row_values = tuple(self.all_commands.values())
        col_size = len(column_names)
        row_size = len((row_values)[0])

        ab = TableWindow(row_values, column_names, row_size, col_size)
        if ab.exec_():
            ab.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
