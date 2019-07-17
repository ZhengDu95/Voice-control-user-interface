##−∗−coding :  utf−8−∗−

from PyQt5.QtWidgets import (QPushButton, QRadioButton,
            QGridLayout, QVBoxLayout, QHBoxLayout,QDialog,
            QLabel, QMessageBox, QInputDialog, QLineEdit,QTableWidget, QTableWidgetItem)

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

import sql
import conf
import password_check
from text_to_speech import tts



class TableWindow(QDialog):
    def __init__(self, row_values, column_names, row_size, col_size):
        super().__init__()
        self.row_values = row_values
        self.column_names = column_names
        self.row = row_size
        self.col = col_size

        self.init_table()


    def init_table(self):
        self.setWindowTitle("Commands Table")

        self.table = QTableWidget()

        # set row count
        self.table.setRowCount(self.row)

        # set column count
        self.table.setColumnCount(self.col)

        # table headline
        self.table.setHorizontalHeaderLabels(self.column_names)

        for r in range(self.row):
            for c in range(self.col):
                if self.column_names[c] in ['task', 'english', 'chinese']:

                    item = QTableWidgetItem(self.row_values[c][r])
                    # execute the line below to every item you need locked
                    item.setFlags(Qt.ItemIsEditable)
                    self.table.setItem(r, c, item)
                else:
                    
                    self.table.setItem(r, c, QTableWidgetItem(self.row_values[c][r]))


        self.table.cellDoubleClicked.connect(self.c_current)

        # Stop scrollbar and hide vertical header because for calculating table size
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.verticalHeader().hide()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        self.v_lay = QVBoxLayout()
        self.setLayout(self.v_lay)

        self.v_lay.addWidget(self.table)

        # Set dialogbox height and width
        dialogWidth = self.table.horizontalHeader().length() + 24
        dialogHeight= self.table.height()
        self.setFixedSize(dialogWidth, dialogHeight )
        self.move(500,100)

        self.show()


    def c_current(self):
        """
        Triggered when cell was double clicked.

        """
        row = self.table.currentRow()
        col = self.table.currentColumn()
        header_name = self.table.takeHorizontalHeaderItem(col).text()

        task_name = self.table.takeItem(row, 0).text()

        value = self.table.item(row, col)
        if value:
            value = value.text()
        else:
            value = ''

        # print("The current cell is ", row, ", ", col)
        # print("In this cell we have: ", value)
        # print("task name:", task_name )
        # print("Column Name:", header_name)

        if header_name.lower() == "custom":
            self.input_for_custom_command(row, col, value, task_name)

        if header_name.lower() == "security":
            match_obj = password_check.PasswordCheckDialog()
            match = match_obj.check()

            if match:
                self.security_change(row, col, value, task_name)
            else:
                tts.speak(speak_text="Incorrect password. Please Try again.", language='english')


    def input_for_custom_command(self, row, col, value, task_name):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your command:', QLineEdit.Normal, value)

        if ok and text.lower().strip() != value.lower():
            self.table.setItem(row,col,QTableWidgetItem(text))

            query = "update commands set custom='{}' where task='{}'".format(text, task_name)
            sql.run_query(query)
            conf.NEW_COMMAND = True
            # BUG: 'Only one custom command add at a time'


    def security_change(self, row, col, value, task_name):
        self.dialog_box = QDialog()

        self.save = QPushButton("Save")
        self.on = QRadioButton("Security On", self.dialog_box)
        self.off = QRadioButton("Security Off", self.dialog_box)

        if value.lower() == 'y':
            self.on.setChecked(True)
        else:
            self.off.setChecked(True)

        # TODO: Bug
        self.save.clicked.connect(lambda: self.btnstate(row,col,task_name))

        self.dialog_box.setWindowModality(Qt.ApplicationModal)

        layout = QVBoxLayout()
        self.dialog_box.setLayout(layout)
        layout.addWidget(self.on)
        layout.addWidget(self.off)
        layout.addWidget(self.save)
        self.dialog_box.exec_()


    # TODO: Change function name
    def btnstate(self, row,col,task_name):

        if self.on.isChecked():
            text = 'Y'

        if self.off.isChecked():
            text = 'N'

        self.table.setItem(row,col,QTableWidgetItem(text))

        query = "update commands set security='{}' where task='{}'".format(text, task_name)
        sql.run_query(query)
        conf.NEW_COMMAND = True
       

    def quit(self):
        self.destroy()
