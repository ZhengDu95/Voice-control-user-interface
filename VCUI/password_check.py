from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit

import sql



class PasswordCheckDialog(QWidget):
    """ Take password but input dialog and check it is valid or not """

    def __init__(self):
        super().__init__()
        self.title = 'Password Check'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        collect_password = sql.run_query('select password from user') # return dictionary
        self.password = collect_password['password'][0]
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


    # TODO: InputDialog appear until password match
    # Return True if password match otherwise Fasle
    def check(self):
        password_match = False
        text, okPressed = QInputDialog.getText(self, "Enter your password","Password:", QLineEdit.Password, "")

        if okPressed and text != '':
            print(self.password)
            if self.password == text:
                password_match = True
        else:
            # TODO:if user press cancel button terminate the running command
            # TODO: SHow error message
            print(self.password)
            print("Password not match")
        
        return password_match


    def quit(self):
        self.destroy()
