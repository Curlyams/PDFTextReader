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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(527, 300)
        font = QFont()
        font.setPointSize(7)
        MainWindow.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"document-open"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgba(39,39,39, 230);\n"
"QMainWindow {\n"
"    border: none;\n"
"}")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: rgba(39,39,39, 245);\n"
"color: rgb(255, 255, 255);")
        self.folder_path = QLineEdit(self.centralwidget)
        self.folder_path.setObjectName(u"folder_path")
        self.folder_path.setGeometry(QRect(40, 69, 341, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.folder_path.setFont(font1)
        self.output_dir = QLineEdit(self.centralwidget)
        self.output_dir.setObjectName(u"output_dir")
        self.output_dir.setGeometry(QRect(40, 140, 341, 31))
        self.output_dir.setFont(font1)
        self.input_browse_button = QPushButton(self.centralwidget)
        self.input_browse_button.setObjectName(u"input_browse_button")
        self.input_browse_button.setGeometry(QRect(420, 70, 80, 31))
        self.input_browse_button.setFont(font1)
        self.input_browse_button.setAutoDefault(False)
        self.input_browse_button.setFlat(False)
        self.output_browse_button = QPushButton(self.centralwidget)
        self.output_browse_button.setObjectName(u"output_browse_button")
        self.output_browse_button.setGeometry(QRect(420, 140, 80, 31))
        self.output_browse_button.setFont(font1)
        self.run_button = QPushButton(self.centralwidget)
        self.run_button.setObjectName(u"run_button")
        self.run_button.setGeometry(QRect(430, 240, 80, 31))
        self.run_button.setFont(font1)
        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(-10, -20, 541, 331))
        self.logo_label.setAutoFillBackground(False)
        self.logo_label.setStyleSheet(u"background-color: rgba(39,39,39, 200)")
        self.logo_label.setFrameShape(QFrame.Panel)
        self.logo_label.setFrameShadow(QFrame.Plain)
        self.logo_label.setPixmap(QPixmap(u"../../../OneDrive/Pictures/rc_logo.svg"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 491, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(21)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(0, 133, 63);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.logo_label.raise_()
        self.folder_path.raise_()
        self.output_dir.raise_()
        self.input_browse_button.raise_()
        self.output_browse_button.raise_()
        self.run_button.raise_()
        self.label.raise_()

        self.retranslateUi(MainWindow)
        self.input_browse_button.clicked.connect(self.folder_path.clear)
        self.output_browse_button.clicked.connect(self.output_dir.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.folder_path.setText(QCoreApplication.translate("MainWindow", u"Input Path To Folder With PDFs", None))
        self.output_dir.setText(QCoreApplication.translate("MainWindow", u"Input Path To Output Folder", None))
        self.input_browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.output_browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.logo_label.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PDF Reader", None))
    # retranslateUi

