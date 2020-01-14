# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creatorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TextQuestionName = QtWidgets.QLabel(self.centralwidget)
        self.TextQuestionName.setObjectName("TextQuestionName")
        self.horizontalLayout_3.addWidget(self.TextQuestionName)
        self.NameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.NameBox.setObjectName("NameBox")
        self.horizontalLayout_3.addWidget(self.NameBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.ContentSpace = QtWidgets.QTabWidget(self.centralwidget)
        self.ContentSpace.setObjectName("ContentSpace")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.QuestionText = QtWidgets.QTextEdit(self.tab)
        self.QuestionText.setObjectName("QuestionText")
        self.verticalLayout_4.addWidget(self.QuestionText)
        self.ContentSpace.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.ContentSpace.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.ContentSpace)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.ContentSpace.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TextQuestionName.setText(_translate("MainWindow", "Question Name"))
        self.ContentSpace.setTabText(self.ContentSpace.indexOf(self.tab), _translate("MainWindow", "Question Text"))
        self.ContentSpace.setTabText(self.ContentSpace.indexOf(self.tab_2), _translate("MainWindow", "Expected Outputs"))
