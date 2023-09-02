# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTextBrowser, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(277, 563)
        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 281, 571))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 281, 561))
        self.label.setPixmap(QPixmap(u"Static images/2 (2).png"))
        self.label.setScaledContents(True)
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 441, 121, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px solid #FFFFFF;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-20, -20, 321, 581))
        self.label_2.setPixmap(QPixmap(u"Static images/Static Image version 3.2.jpg"))
        self.label_2.setScaledContents(True)
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 410, 31, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
" background-color: #6a99ca;\n"
"  color: white;\n"
"  border: none;\n"
"  padding: 5px;\n"
"  font-size: 35px;\n"
"  height: 130px;\n"
"  width: 130px;\n"
"  box-shadow: 0 2px 4px darkslategray;\n"
"  cursor: pointer;\n"
"  transition: all 0.2s ease;\n"
"border-radius: 5%;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, -1, 281, 571))
        self.label_3.setPixmap(QPixmap(u"Static images/Orange Simple Food Delivery Clean Mobile Prototype-2.png"))
        self.label_3.setScaledContents(True)
        self.plus = QPushButton(self.page_3)
        self.plus.setObjectName(u"plus")
        self.plus.setGeometry(QRect(100, 200, 31, 31))
        self.plus.setStyleSheet(u"QPushButton {\n"
" background-color: #FFFFFF;\n"
"    color: #f2a449;\n"
"    border: none;\n"
"    padding: 10px;\n"
"	font: 15pt \"Arial\";\n"
"    text-align: center;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #F0EEED;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"")
        self.pushButton_3 = QPushButton(self.page_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(230, 200, 31, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
" background-color: #FFFFFF;\n"
"    color: #f2a449;\n"
"    border: none;\n"
"    padding: 10px;\n"
"	font: 15pt \"Arial\";\n"
"    text-align: center;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #F0EEED;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-10, -10, 291, 581))
        self.label_4.setPixmap(QPixmap(u"Static images/2.png"))
        self.label_4.setScaledContents(True)
        self.textBrowser = QTextBrowser(self.page_4)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 210, 249, 141))
        self.textBrowser.setStyleSheet(u"border: none;")
        self.lineEdit = QLineEdit(self.page_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 190, 249, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	font: 9pt \"Microsoft New Tai Lue\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: #d6d7d7;\n"
"    padding: 20px;\n"
"    text-align: center;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.lineEdit_3 = QLineEdit(self.page_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 270, 249, 31))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	font: 9pt \"Microsoft New Tai Lue\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: #d6d7d7;\n"
"    padding: 20px;\n"
"    text-align: center;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.lineEdit_4 = QLineEdit(self.page_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 310, 249, 31))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"	font: 9pt \"Microsoft New Tai Lue\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: #d6d7d7;\n"
"    padding: 20px;\n"
"    text-align: center;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.lineEdit_2 = QLineEdit(self.page_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 230, 249, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	font: 9pt \"Microsoft New Tai Lue\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: #d6d7d7;\n"
"    padding: 20px;\n"
"    text-align: center;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.lineEdit_5 = QLineEdit(self.page_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 370, 251, 31))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"	font: 9pt \"Microsoft New Tai Lue\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: #d6d7d7;\n"
"    padding: 20px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.pushButton_11 = QPushButton(self.page_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(70, 410, 131, 41))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
" background-color: #5a5a5a;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 10px;\n"
"	font: 9pt \"Arial\";\n"
"    text-align: center;\n"
"    border-radius: 5px;\n"
"}rgb(90, 90, 90)")
        self.backsign = QPushButton(self.page_4)
        self.backsign.setObjectName(u"backsign")
        self.backsign.setGeometry(QRect(10, 10, 41, 21))
        self.backsign.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px solid #FFFFFF;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }\n"
"")
        self.stackedWidget.addWidget(self.page_4)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_9 = QLabel(self.page_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, -1, 281, 571))
        self.label_9.setPixmap(QPixmap(u"Static images/1.png"))
        self.label_9.setScaledContents(True)
        self.pushButton_6 = QPushButton(self.page_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(80, 470, 121, 41))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
" background-color: #5a5a5a;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 10px;\n"
"	font: 9pt \"Arial\";\n"
"    text-align: center;\n"
"    border-radius: 5px;\n"
"}rgb(90, 90, 90)")
        self.stackedWidget.addWidget(self.page_9)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-20, -20, 321, 601))
        self.label_5.setPixmap(QPixmap(u"Static images/1 (1).png"))
        self.label_5.setScaledContents(True)
        self.outfits = QPushButton(self.page_5)
        self.outfits.setObjectName(u"outfits")
        self.outfits.setGeometry(QRect(150, 510, 51, 51))
        self.outfits.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.pushButton_12 = QPushButton(self.page_5)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(220, 510, 51, 51))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.pushButton_13 = QPushButton(self.page_5)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(70, 510, 71, 51))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.pushButton_21 = QPushButton(self.page_5)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(20, 360, 101, 91))
        self.pushButton_21.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px solid #FFFFFF;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_6 = QLabel(self.page_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 291, 571))
        self.label_6.setPixmap(QPixmap(u"Static images/Cream Illustrated Saving Money Mobile Prototype.png"))
        self.label_6.setScaledContents(True)
        self.pushButton_14 = QPushButton(self.page_6)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(80, 510, 71, 51))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.outfits_2 = QPushButton(self.page_6)
        self.outfits_2.setObjectName(u"outfits_2")
        self.outfits_2.setGeometry(QRect(220, 510, 51, 51))
        self.outfits_2.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.back = QPushButton(self.page_6)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(20, 510, 51, 51))
        self.back.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.pushButton_15 = QPushButton(self.page_6)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(30, 220, 101, 101))
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px solid #FFFFFF;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.pushButton_26 = QPushButton(self.page_6)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(130, 470, 31, 31))
        self.pushButton_26.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.stackedWidget.addWidget(self.page_6)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.label_13 = QLabel(self.page_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, -11, 281, 581))
        self.label_13.setPixmap(QPixmap(u"Static images/Cream Illustrated Saving Money Mobile Prototype (2).png"))
        self.label_13.setScaledContents(True)
        self.pushButton_25 = QPushButton(self.page_13)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(130, 460, 21, 31))
        self.pushButton_25.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.back_2 = QPushButton(self.page_13)
        self.back_2.setObjectName(u"back_2")
        self.back_2.setGeometry(QRect(20, 510, 51, 51))
        self.back_2.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.back_3 = QPushButton(self.page_13)
        self.back_3.setObjectName(u"back_3")
        self.back_3.setGeometry(QRect(80, 510, 61, 51))
        self.back_3.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.back_4 = QPushButton(self.page_13)
        self.back_4.setObjectName(u"back_4")
        self.back_4.setGeometry(QRect(210, 510, 51, 51))
        self.back_4.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.stackedWidget.addWidget(self.page_13)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_10 = QLabel(self.page_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 281, 571))
        self.label_10.setPixmap(QPixmap(u"Static images/Cream Illustrated Saving Money Mobile Prototype-2 (1).png"))
        self.label_10.setScaledContents(True)
        self.pushButton_17 = QPushButton(self.page_10)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(80, 430, 121, 20))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_11 = QLabel(self.page_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(2, -1, 281, 571))
        self.label_11.setPixmap(QPixmap(u"Static images/Cream Illustrated Saving Money Mobile Prototype-3 (1).png"))
        self.label_11.setScaledContents(True)
        self.pushButton_18 = QPushButton(self.page_11)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(220, 360, 121, 20))
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.pushButton_19 = QPushButton(self.page_11)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(80, 430, 121, 20))
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.stackedWidget.addWidget(self.page_11)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_7 = QLabel(self.page_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-10, -10, 291, 591))
        self.label_7.setPixmap(QPixmap(u"Static images/2 (1).png"))
        self.label_7.setScaledContents(True)
        self.pushButton_16 = QPushButton(self.page_7)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(70, 510, 71, 51))
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.outfits_4 = QPushButton(self.page_7)
        self.outfits_4.setObjectName(u"outfits_4")
        self.outfits_4.setGeometry(QRect(210, 510, 51, 51))
        self.outfits_4.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.outfits_5 = QPushButton(self.page_7)
        self.outfits_5.setObjectName(u"outfits_5")
        self.outfits_5.setGeometry(QRect(150, 510, 51, 51))
        self.outfits_5.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.pushButton_20 = QPushButton(self.page_7)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(30, 370, 91, 91))
        self.pushButton_20.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px solid #FFFFFF;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_8 = QLabel(self.page_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 281, 571))
        self.label_8.setPixmap(QPixmap(u"Static images/Colorful Activity Tracker App Mobile Prototype-3.png"))
        self.label_8.setScaledContents(True)
        self.pushButton_4 = QPushButton(self.page_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 10, 93, 29))
        self.stackedWidget.addWidget(self.page_8)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_12 = QLabel(self.page_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 281, 571))
        self.label_12.setStyleSheet(u"font: 9pt \"Arial\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: black;\n"
"")
        self.label_12.setPixmap(QPixmap(u"Static images/Purple Illustrated Home, Dashboard, Upgrade Premium, and Join Classroom Screens Minimalist Mobile Prototype-2.png"))
        self.label_12.setScaledContents(True)
        self.dateEdit = QDateEdit(self.page_12)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(110, 140, 110, 25))
        self.dateEdit.setStyleSheet(u"font: 9pt \"Arial\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: black;\n"
"")
        self.comboBox = QComboBox(self.page_12)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 180, 111, 31))
        self.comboBox.setStyleSheet(u"font: 9pt \"Arial\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: black;\n"
"")
        self.lineEdit_6 = QLineEdit(self.page_12)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(100, 220, 81, 31))
        self.lineEdit_6.setStyleSheet(u"font: 9pt \"Arial\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: black;\n"
"")
        self.lineEdit_7 = QLineEdit(self.page_12)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(130, 260, 81, 21))
        self.lineEdit_7.setStyleSheet(u"font: 9pt \"Arial\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: black;\n"
"")
        self.lineEdit_8 = QLineEdit(self.page_12)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(130, 290, 81, 21))
        self.lineEdit_8.setStyleSheet(u"font: 9pt \"Arial\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: black;\n"
"")
        self.lineEdit_9 = QLineEdit(self.page_12)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(130, 320, 81, 21))
        self.lineEdit_9.setStyleSheet(u"font: 9pt \"Arial\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: black;\n"
"")
        self.textEdit_2 = QTextEdit(self.page_12)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(50, 370, 181, 71))
        self.textEdit_2.setStyleSheet(u"font: 9pt \"Arial\";\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: black;\n"
"")
        self.pushButton_22 = QPushButton(self.page_12)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(60, 450, 61, 20))
        self.pushButton_22.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.pushButton_23 = QPushButton(self.page_12)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(160, 450, 61, 20))
        self.pushButton_23.setStyleSheet(u"QPushButton {\n"
"        cursor: pointer;\n"
"        border: 1px #37b3fb;\n"
"        background-color: transparent;\n"
"        height: 50px;\n"
"        width: 200px;\n"
"        color: #3498db;\n"
"        font-size: 1.5em;\n"
"        box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);\n"
"    }")
        self.stackedWidget.addWidget(self.page_12)

        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.label_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u">", None))
        self.label_3.setText("")
        self.plus.setText(QCoreApplication.translate("Widget", u"+", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"+", None))
        self.label_4.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("Widget", u"Register", None))
        self.backsign.setText("")
        self.label_9.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"Log in", None))
        self.label_5.setText("")
        self.outfits.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_21.setText("")
        self.label_6.setText("")
        self.pushButton_14.setText("")
        self.outfits_2.setText("")
        self.back.setText("")
        self.pushButton_15.setText("")
        self.pushButton_26.setText("")
        self.label_13.setText("")
        self.pushButton_25.setText("")
        self.back_2.setText("")
        self.back_3.setText("")
        self.back_4.setText("")
        self.label_10.setText("")
        self.pushButton_17.setText("")
        self.label_11.setText("")
        self.pushButton_18.setText("")
        self.pushButton_19.setText("")
        self.label_7.setText("")
        self.pushButton_16.setText("")
        self.outfits_4.setText("")
        self.outfits_5.setText("")
        self.pushButton_20.setText("")
        self.label_8.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Back", None))
        self.label_12.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Type", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"Weightlifting", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"Yoga", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Widget", u"Cardio", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Widget", u"Run", None))

        self.pushButton_22.setText("")
        self.pushButton_23.setText("")
    # retranslateUi

