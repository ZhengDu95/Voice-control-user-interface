import sys
import re

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QDialogButtonBox,
                QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, 
                QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout)
 
import sql

import logging

LOG_FORMAT = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="debug.log",level=logging.DEBUG,format=LOG_FORMAT,filemode="w")
logger = logging.getLogger(__name__)

 

class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4
    
    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.data_save)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("Registration")
    
 
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Registration Form")
        layout = QFormLayout()

        self.user_name =  QLineEdit()

        self.email = QLineEdit()
        self.email.setPlaceholderText = "foo@example.com"

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)

        self.language_combo  = QComboBox()
        self.language_combo.addItem('Chinese')
        self.language_combo.addItem('English')

        layout.addRow(QLabel("Name:"), self.user_name)
        layout.addRow(QLabel("Email:"), self.email)
        layout.addRow(QLabel("Password:"), self.password)
        layout.addRow(QLabel("Confirm Password:"), self.confirm_password)
        layout.addRow(QLabel("Language:"), self.language_combo)
        
        self.formGroupBox.setLayout(layout)

    
    def data_save(self):
        logger.debug("User name: {}\
                        Password: {}\
                        Confirm Password: {}\
                        Language: {}"
                        .format(self.user_name.text(),self.password.text(),self.confirm_password.text(),self.language_combo.currentText()))
        
        error = False

        # TODO: Error message show
        if self.user_name.text() == '':
            error = True
            print("User name can't be empty")

        if self.email.text() == '' and valid_email(self.email.text()) == False:
            error = True
            print("Not valid email address")

        if self.password.text() == '':
            error = True
            print("Password field can't be empty")

        if self.confirm_password.text() == '':
            error = True
            print("Confirm Password field can't be empty")

        if self.password.text() != self.confirm_password.text():
            error = True
            print("Password and Confirm Password didn't match")

        if not error:
            query = "insert into USER (id,name,password,email,language) values (1,'{}','{}','{}','{}')".format(self.user_name.text(),self.password.text(),self.email.text(),self.language_combo.currentText())
            d = sql.run_query(query=query)
            self.quit()

    def quit(self):
        self.destroy()



def valid_email(email_address):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_address)
    
    if match == None:
        return False
    else:
        return True


    
