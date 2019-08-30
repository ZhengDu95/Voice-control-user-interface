##−∗−coding :  utf−8−∗−

from PyQt5.QtWidgets import (QPushButton, QRadioButton,
            QGridLayout, QVBoxLayout, QHBoxLayout,QDialog,
            QLabel, QMessageBox, QInputDialog, QLineEdit,QTableWidget, QTableWidgetItem)

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

#import sql
import conf
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


        #self.table.cellDoubleClicked.connect(self.c_current)

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



       

    def quit(self):
        self.destroy()
