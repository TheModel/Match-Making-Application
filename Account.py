#Mainpage.py

from PyQt5.QtWidgets import QMainWindow
from CreateAccount import CreateAccountScreen
from login import LoginScreen
from PyQt5.uic import loadUi
import allimages


class MainScreen(QMainWindow):
    def __init__(self, username=""):
        super(MainScreen, self).__init__()
        loadUi("Mainpage.ui", self)

        ## SETTING THE PROFILE VALUES IN INPUT FIELDS TO THEIR DEFAULT VALUE ENETERED BY THE USER IN THE CREATE ACCOUNT SCREEN ##
        self.Account_username_Input.setText(username)