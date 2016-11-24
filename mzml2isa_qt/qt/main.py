# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/graphics/assets/graphics/ebi_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input.setEnabled(True)
        self.lineEdit_input.setGeometry(QtCore.QRect(10, 140, 620, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_input.sizePolicy().hasHeightForWidth())
        self.lineEdit_input.setSizePolicy(sizePolicy)
        self.lineEdit_input.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.lineEdit_input.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.lbl_input = QtWidgets.QLabel(self.centralwidget)
        self.lbl_input.setGeometry(QtCore.QRect(20, 162, 180, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_input.sizePolicy().hasHeightForWidth())
        self.lbl_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/Verdana.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_input.setFont(font)
        self.lbl_input.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.lbl_input.setObjectName("lbl_input")
        self.lineEdit_output = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_output.setEnabled(False)
        self.lineEdit_output.setGeometry(QtCore.QRect(10, 200, 620, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_output.sizePolicy().hasHeightForWidth())
        self.lineEdit_output.setSizePolicy(sizePolicy)
        self.lineEdit_output.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.lineEdit_output.setText("")
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.lineEdit_study = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_study.setEnabled(False)
        self.lineEdit_study.setGeometry(QtCore.QRect(10, 260, 620, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_study.sizePolicy().hasHeightForWidth())
        self.lineEdit_study.setSizePolicy(sizePolicy)
        self.lineEdit_study.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.lineEdit_study.setObjectName("lineEdit_study")
        self.lbl_output = QtWidgets.QLabel(self.centralwidget)
        self.lbl_output.setGeometry(QtCore.QRect(20, 222, 180, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_output.sizePolicy().hasHeightForWidth())
        self.lbl_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/Verdana.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_output.setFont(font)
        self.lbl_output.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.lbl_output.setObjectName("lbl_output")
        self.lbl_study = QtWidgets.QLabel(self.centralwidget)
        self.lbl_study.setGeometry(QtCore.QRect(20, 282, 180, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_study.sizePolicy().hasHeightForWidth())
        self.lbl_study.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/Verdana.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_study.setFont(font)
        self.lbl_study.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.lbl_study.setObjectName("lbl_study")
        self.toolButton_input_explore = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_input_explore.setGeometry(QtCore.QRect(530, 162, 90, 25))
        self.toolButton_input_explore.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/graphics/browse_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_input_explore.setIcon(icon1)
        self.toolButton_input_explore.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_input_explore.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolButton_input_explore.setAutoRaise(False)
        self.toolButton_input_explore.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_input_explore.setObjectName("toolButton_input_explore")
        self.toolButton_output_explore = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_output_explore.setEnabled(False)
        self.toolButton_output_explore.setGeometry(QtCore.QRect(530, 222, 90, 25))
        self.toolButton_output_explore.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/graphics/assets/graphics/browse_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_output_explore.setIcon(icon2)
        self.toolButton_output_explore.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_output_explore.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolButton_output_explore.setObjectName("toolButton_output_explore")
        self.cBox_separate = QtWidgets.QCheckBox(self.centralwidget)
        self.cBox_separate.setGeometry(QtCore.QRect(10, 380, 291, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBox_separate.sizePolicy().hasHeightForWidth())
        self.cBox_separate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/Verdana.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cBox_separate.setFont(font)
        self.cBox_separate.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.cBox_separate.setChecked(True)
        self.cBox_separate.setObjectName("cBox_separate")
        self.cBox_multiple = QtWidgets.QCheckBox(self.centralwidget)
        self.cBox_multiple.setGeometry(QtCore.QRect(10, 360, 280, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBox_multiple.sizePolicy().hasHeightForWidth())
        self.cBox_multiple.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/Verdana.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cBox_multiple.setFont(font)
        self.cBox_multiple.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.cBox_multiple.setObjectName("cBox_multiple")
        self.cBox_export = QtWidgets.QCheckBox(self.centralwidget)
        self.cBox_export.setGeometry(QtCore.QRect(10, 400, 340, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBox_export.sizePolicy().hasHeightForWidth())
        self.cBox_export.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/Verdana.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cBox_export.setFont(font)
        self.cBox_export.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.cBox_export.setChecked(True)
        self.cBox_export.setObjectName("cBox_export")
        self.PushBut_convert = QtWidgets.QPushButton(self.centralwidget)
        self.PushBut_convert.setGeometry(QtCore.QRect(530, 370, 90, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushBut_convert.sizePolicy().hasHeightForWidth())
        self.PushBut_convert.setSizePolicy(sizePolicy)
        self.PushBut_convert.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.PushBut_convert.setObjectName("PushBut_convert")
        self.toolButton_help = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_help.setGeometry(QtCore.QRect(330, 370, 90, 25))
        self.toolButton_help.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.toolButton_help.setObjectName("toolButton_help")
        self.lbl_input_error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_input_error.setGeometry(QtCore.QRect(150, 162, 370, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_input_error.sizePolicy().hasHeightForWidth())
        self.lbl_input_error.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/Verdana.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_input_error.setFont(font)
        self.lbl_input_error.setStyleSheet("color: rgb(216, 1, 35);\n"
"font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.lbl_input_error.setText("")
        self.lbl_input_error.setObjectName("lbl_input_error")
        self.lbl_output_error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_output_error.setGeometry(QtCore.QRect(150, 222, 370, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_output_error.sizePolicy().hasHeightForWidth())
        self.lbl_output_error.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/Verdana.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_output_error.setFont(font)
        self.lbl_output_error.setStyleSheet("color: rgb(216, 1, 35);\n"
"font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.lbl_output_error.setText("")
        self.lbl_output_error.setObjectName("lbl_output_error")
        self.lbl_study_error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_study_error.setGeometry(QtCore.QRect(150, 282, 370, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_study_error.sizePolicy().hasHeightForWidth())
        self.lbl_study_error.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/Verdana.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_study_error.setFont(font)
        self.lbl_study_error.setStyleSheet("color: rgb(216, 1, 35);\n"
"font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.lbl_study_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_study_error.setText("")
        self.lbl_study_error.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_study_error.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lbl_study_error.setObjectName("lbl_study_error")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 62))
        self.frame.setStyleSheet("background: rgb(11,123,125);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setGeometry(QtCore.QRect(1, 1, 240, 60))
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/graphics/assets/graphics/ebi-logo.jpg"))
        self.logo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.logo.setObjectName("logo")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(349, 1, 271, 62))
        font = QtGui.QFont()
        font.setFamily(":/fonts/assets/fonts/HelveticaNeue.ttf")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255,255,255);\n"
"font: 24pt url(:/fonts/assets/fonts/HelveticaNeue.ttf);")
        self.title.setObjectName("title")
        self.toolButton_metadata = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_metadata.setEnabled(True)
        self.toolButton_metadata.setGeometry(QtCore.QRect(430, 370, 90, 51))
        self.toolButton_metadata.setCheckable(False)
        self.toolButton_metadata.setAutoRepeatInterval(100)
        self.toolButton_metadata.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_metadata.setAutoRaise(False)
        self.toolButton_metadata.setObjectName("toolButton_metadata")
        self.toolButton_about = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_about.setGeometry(QtCore.QRect(330, 395, 90, 25))
        self.toolButton_about.setStyleSheet("font: 10pt url(:/fonts/assets/fonts/Verdana.ttf);")
        self.toolButton_about.setObjectName("toolButton_about")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mzML to ISA-Tab"))
        self.lbl_input.setText(_translate("MainWindow", "Input folder"))
        self.lbl_output.setText(_translate("MainWindow", "Output folder"))
        self.lbl_study.setText(_translate("MainWindow", "Study name"))
        self.toolButton_input_explore.setText(_translate("MainWindow", "Browse"))
        self.toolButton_output_explore.setText(_translate("MainWindow", "Browse"))
        self.cBox_separate.setText(_translate("MainWindow", "Separate positive and negative assays"))
        self.cBox_multiple.setText(_translate("MainWindow", "Input folder contains several studies"))
        self.cBox_export.setText(_translate("MainWindow", "Export results to directory of each study"))
        self.PushBut_convert.setText(_translate("MainWindow", "Convert"))
        self.toolButton_help.setText(_translate("MainWindow", "Help"))
        self.title.setText(_translate("MainWindow", "mzML to ISA-Tab "))
        self.toolButton_metadata.setText(_translate("MainWindow", "Add \n"
"Metadata"))
        self.toolButton_about.setText(_translate("MainWindow", "About"))

import resources_rc
