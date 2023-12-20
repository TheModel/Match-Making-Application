from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from Mainpage import MainScreen
import sqlite3
from validation import is_username_taken, check_info_format
from database import create_table_if_not_exists, store_user_data

class CreateAccountScreen(QMainWindow):
    def __init__(self, widget):
        super(CreateAccountScreen, self).__init__()
        # ... (existing initialization)

    # ... (other methods)

    def Submit(self):
        username = self.username_LineEdit.text()
        email = self.Email_LineEdit.text()
        password = self.Password_LineEdit.text()
        age = self.Age_LineEdit.text()
        phonenumber = self.PhoneNo_lineEdit.text()
        location = self.Location_LineEdit.text()
        gender = self.Gender_LineEdit.text()

        # Check the information format using functions from validation.py
        error_message = check_info_format(username, email, password, age, phonenumber, location, gender)
        if error_message:
            self.error_label.setText(error_message)
        else:
            if hasattr(self, 'image_path'):
                # Read the image file and convert it to binary
                with open(self.image_path, 'rb') as file:
                    image_binary = file.read()
                # Store user data using functions from database.py
                store_user_data(self.cursor, self.conn, username, email, password, age, phonenumber, location, gender, image_binary)
            else:
                # Store user data using functions from database.py without an image
                store_user_data(self.cursor, self.conn, username, email, password, age, phonenumber, location, gender, None)

            mainpage = MainScreen(username, email, password, age, phonenumber, location, gender)
            mainpage.setUserProfile()
            self.widget.addWidget(mainpage)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
