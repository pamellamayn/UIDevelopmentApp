# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QComboBox, QVBoxLayout, QLabel, QStackedWidget, QWidget, QCheckBox, QProgressBar
#from PySide6 import uic
import sys
from ui_form import Ui_Widget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        #Define Widgets
        self.start= self.findChild(QPushButton, "pushButton")
        self.next= self.findChild(QPushButton, "pushButton_2")
        self.plus= self.findChild(QPushButton, "plus")
        self.stacked= self.findChild(QStackedWidget, "stackedWidget")
        self.page1= self.findChild(QWidget, "page")
        self.page2= self.findChild(QWidget, "page_2")
        self.page3= self.findChild(QWidget, "page_3")
        self.page4= self.findChild(QWidget, "page_4")
        self.page5= self.findChild(QWidget, "page_5")
        self.page6= self.findChild(QWidget, "page_6")
        self.page7= self.findChild(QWidget, "page_7")
        self.page8= self.findChild(QWidget, "page_8")
        self.page9= self.findChild(QWidget, "page_9")
        self.page10= self.findChild(QWidget, "page_10")
        self.page11= self.findChild(QWidget, "page_11")
        self.page12= self.findChild(QWidget, "page_12")
        self.page13= self.findChild(QWidget, "page_13")
        self.login= self.findChild(QPushButton, "pushButton_6")
        self.select= self.findChild(QPushButton, "pushButton_3")
        self.back= self.findChild(QPushButton, "back")
        self.backscreen= self.findChild(QPushButton, "pushButton_4")
        self.register= self.findChild(QPushButton, "pushButton_11")
        self.outfits= self.findChild(QPushButton, "outfits")
        self.outfitsnew= self.findChild(QPushButton, "outfits_5")
        self.backsign= self.findChild(QPushButton, "backsign")
        self.add= self.findChild(QPushButton, "pushButton_14")
        self.outfit1= self.findChild(QPushButton, "pushButton_15")
        self.addnew= self.findChild(QPushButton, "pushButton_16")
        self.purchase= self.findChild(QPushButton, "pushButton_17")
        self.progress= self.findChild(QPushButton, "pushButton_20")
        self.wear= self.findChild(QPushButton, "pushButton_19")
        self.progress2= self.findChild(QPushButton, "pushButton_21")
        self.clothes= self.findChild(QPushButton, "pushButton_25")
        self.logback= self.findChild(QPushButton, "pushButton_22")
        self.backhome= self.findChild(QPushButton, "back_2")
        self.submit= self.findChild(QPushButton, "pushButton_23")
        self.clothesnew= self.findChild(QPushButton, "pushButton_26")

        #whenever certain widget is clicked, page layout changes
        self.start.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page2))
        self.next.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page3))
        self.plus.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page4))
        self.login.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page5))
        self.back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page5))
        self.register.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page9))
        self.outfits.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page6))
        self.backsign.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page3))
        self.purchase.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page11))
        self.progress.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page8))
        self.outfit1.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page10))
        self.wear.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page7))
        self.select.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page4))
        self.progress2.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page8))
        self.backscreen.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page7))
        self.clothes.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page6))
        self.clothesnew.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page13))
        self.add.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page12))
        self.backhome.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page7))
        self.addnew.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page12))
        self.submit.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page7))
        self.logback.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page7))
        self.outfitsnew.clicked.connect(lambda: self.stacked.setCurrentWidget(self.page6))

        #prefill the line edits to have prompts for the users
        self.lineEdit= self.findChild(QLineEdit, "lineEdit")
        self.lineEdit.setPlaceholderText("Email or Phone Number")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)

        self.lineEdit2= self.findChild(QLineEdit, "lineEdit_2")
        self.lineEdit2.setPlaceholderText("Username")
        self.lineEdit2.setEchoMode(QLineEdit.EchoMode.Normal)

        self.lineEdit3= self.findChild(QLineEdit, "lineEdit_3")
        self.lineEdit3.setPlaceholderText("Full Name")
        self.lineEdit3.setEchoMode(QLineEdit.EchoMode.Normal)

        self.lineEdit4= self.findChild(QLineEdit, "lineEdit_4")
        self.lineEdit4.setPlaceholderText("Password")
        self.lineEdit4.setEchoMode(QLineEdit.EchoMode.Normal)

        self.lineEdit5= self.findChild(QLineEdit, "lineEdit_5")
        self.lineEdit5.setPlaceholderText("Confirm Password")
        self.lineEdit5.setEchoMode(QLineEdit.EchoMode.Normal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
