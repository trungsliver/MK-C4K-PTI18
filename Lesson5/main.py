import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic
import oop, data_io

# xử lý
app = QApplication(sys.argv)
dtb = oop.UserDatabase()

class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui//signup.ui", self)
        self.pushButton_signup.clicked.connect(self.check_signup)