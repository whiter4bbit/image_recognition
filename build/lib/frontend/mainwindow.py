# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Dec 22 20:37:47 2009
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 548)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagesListWidget = QtGui.QListWidget(self.centralwidget)
        self.imagesListWidget.setGeometry(QtCore.QRect(0, 20, 321, 291))
        self.imagesListWidget.setObjectName("imagesListWidget")
        self.ImageListLabel = QtGui.QLabel(self.centralwidget)
        self.ImageListLabel.setGeometry(QtCore.QRect(330, 20, 271, 291))
        self.ImageListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageListLabel.setMargin(0)
        self.ImageListLabel.setObjectName("ImageListLabel")
        self.trainButton = QtGui.QPushButton(self.centralwidget)
        self.trainButton.setGeometry(QtCore.QRect(490, 310, 114, 26))
        self.trainButton.setObjectName("trainButton")
        self.recognizeImageLabel = QtGui.QLabel(self.centralwidget)
        self.recognizeImageLabel.setGeometry(QtCore.QRect(10, 350, 281, 151))
        self.recognizeImageLabel.setObjectName("recognizeImageLabel")
        self.recognizeImageLabel_2 = QtGui.QLabel(self.centralwidget)
        self.recognizeImageLabel_2.setGeometry(QtCore.QRect(300, 340, 301, 151))
        self.recognizeImageLabel_2.setObjectName("recognizeImageLabel_2")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 330, 131, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 330, 131, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 131, 17))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 23))
        self.menubar.setObjectName("menubar")
        self.menuFigures = QtGui.QMenu(self.menubar)
        self.menuFigures.setObjectName("menuFigures")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_figure = QtGui.QAction(MainWindow)
        self.actionAdd_figure.setObjectName("actionAdd_figure")
        self.actionRecognize_figure = QtGui.QAction(MainWindow)
        self.actionRecognize_figure.setObjectName("actionRecognize_figure")
        self.menuFigures.addAction(self.actionAdd_figure)
        self.menuFigures.addAction(self.actionRecognize_figure)
        self.menubar.addAction(self.menuFigures.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.trainButton.setText(QtGui.QApplication.translate("MainWindow", "Train", None, QtGui.QApplication.UnicodeUTF8))
        self.recognizeImageLabel.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.recognizeImageLabel_2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "To recognize", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Recognized:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Trained images:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFigures.setTitle(QtGui.QApplication.translate("MainWindow", "Figures", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_figure.setText(QtGui.QApplication.translate("MainWindow", "Add figure", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecognize_figure.setText(QtGui.QApplication.translate("MainWindow", "Recognize figure", None, QtGui.QApplication.UnicodeUTF8))

