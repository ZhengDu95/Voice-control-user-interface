import sys
import os

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (QApplication,QPushButton, QRadioButton,
            QGridLayout, QVBoxLayout, QHBoxLayout,QDialog, QGroupBox,QFormLayout,QDialogButtonBox,
            QLabel, QMessageBox, QInputDialog, QLineEdit,QTableWidget, QTableWidgetItem)

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

import sql
import password_check


class TableWindow(QDialog):
    def __init__(self):
        super().__init__()

        data = sql.run_query("select * from Folders")

        self.setWindowTitle("Show Table")

        self.v_lay = QVBoxLayout()
        self.setLayout(self.v_lay)

        self.add_btn = QPushButton('Add', default=False, autoDefault=False)
        self.add_btn.clicked.connect(self.add_dialog)
        self.v_lay.addWidget(self.add_btn)

        if data:
            self.row_values = list(data.values())
            self.column_names = list(data.keys())
            self.row = len(self.row_values[0])
            self.col = len(self.column_names)

            self.init_table()
            self.v_lay.addWidget(self.table)

        else:
            message = QLabel("Click on ADD button")
            message.setFont(QFont("Times", 12, QFont.Bold,))
            message.setStyleSheet("background-color:#f531ba;text-align:center;")
            self.v_lay.addWidget(message)

        self.show()


    def init_table(self):

        self.table = QTableWidget()

        # set row count
        self.table.setRowCount(self.row)

        # set column count
        self.table.setColumnCount(self.col+1) # Because for edit button column

        # table headline
        self.table.setHorizontalHeaderLabels(self.column_names)

        for r in range(self.row):
            for c in range(self.col):
                item = QTableWidgetItem(self.row_values[c][r])
                item.setFlags(Qt.ItemIsEditable)
                self.table.setItem(r, c, item)
            self.delete_btn = QPushButton('Delete', default=False, autoDefault=False)
            self.delete_btn.clicked.connect(self.delete_data_func)
            self.table.setCellWidget(r,c+1,self.delete_btn)

        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.verticalHeader().hide()
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        dialogWidth = self.table.horizontalHeader().length() + 24
        dialogHeight= self.table.height()
        self.setFixedSize(dialogWidth, dialogHeight )


    def delete_data_func(self):
        row = self.table.currentRow()
        col = self.table.currentColumn()

        folder_path_value = self.table.item(row, col-1).text()

        # TODO: show confirmation dialog to delete data
        # TODO: refresh or trigger that data change
        query = "delete from Folders where path='{}'".format(folder_path_value)
        sql.run_query(query)


    def add_dialog(self):
        AddDialog().exec_()


    def quit(self):
        self.destroy()


class AddDialog(QDialog):
    def __init__(self):
        super(AddDialog,self).__init__()

        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Save)
        buttonBox.accepted.connect(self.data_save)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Add")

    def createFormGroupBox(self):

        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()

        self.folder_name =  QLineEdit()
        self.folder_name.setPlaceholderText = "Enter folder name"

        self.folder_path = QLineEdit()
        self.folder_path.setPlaceholderText = "Enter full path of folder"

        layout.addRow(QLabel("Folder Name:"), self.folder_name )
        layout.addRow(QLabel("Folder Path:"), self.folder_path)

        self.formGroupBox.setLayout(layout)


    def data_save(self):
        name = self.folder_name.text()
        path =  self.folder_path.text()

        if not valid_folder_name(name):
            print("Folder name can't be empty")
        elif not valid_folder_path(path):
            print("Insert valid path")
        else:
            query = "insert into Folders values('{}','{}')".format(name.lower(),path)
            sql.run_query(query) # TODO: update table
            self.close()


def valid_folder_path(path):
    if path and os.path.exists(path):
        return True

def valid_folder_name(name):
    if name:
        return True


def main():
    ab = TableWindow()
    if ab.exec_():
        ab.quit()
