import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from welcome import WelcomeScreen

##########################################
##  RUNNING THE APPLICATION             ##
##########################################


app = QApplication(sys.argv)
widget = QStackedWidget()
welcomewindow = WelcomeScreen(widget)
widget.addWidget(welcomewindow)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
sys.exit(app.exec_())


#Hello deborah is making a lot of noise