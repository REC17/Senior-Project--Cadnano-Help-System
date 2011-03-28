# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webwindow.ui'
#
# Created: Sat Mar 05 15:41:58 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(860, 584)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.webView = QtWebKit.QWebView(self.centralWidget)
        self.webView.setGeometry(QtCore.QRect(10, 40, 841, 491))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.homeButton = QtGui.QPushButton(self.centralWidget)
        self.homeButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.homeButton.setObjectName(_fromUtf8("homeButton"))
        self.backButton = QtGui.QPushButton(self.centralWidget)
        self.backButton.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.forwardButton = QtGui.QPushButton(self.centralWidget)
        self.forwardButton.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
        self.searchButton = QtGui.QPushButton(self.centralWidget)
        self.searchButton.setGeometry(QtCore.QRect(770, 10, 75, 23))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.searchEdit = QtGui.QLineEdit(self.centralWidget)
        self.searchEdit.setGeometry(QtCore.QRect(482, 10, 281, 20))
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 860, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHistory = QtGui.QMenu(self.menuBar)
        self.menuHistory.setObjectName(_fromUtf8("menuHistory"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionHome = QtGui.QAction(MainWindow)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionView_Complete_History = QtGui.QAction(MainWindow)
        self.actionView_Complete_History.setObjectName(_fromUtf8("actionView_Complete_History"))
        self.actionClear_History = QtGui.QAction(MainWindow)
        self.actionClear_History.setObjectName(_fromUtf8("actionClear_History"))
        self.menuFile.addAction(self.actionHome)
        self.menuFile.addAction(self.actionSearch)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuHistory.addAction(self.actionView_Complete_History)
        self.menuHistory.addAction(self.actionClear_History)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHistory.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setText(QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.forwardButton.setText(QtGui.QApplication.translate("MainWindow", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHistory.setTitle(QtGui.QApplication.translate("MainWindow", "&History", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setText(QtGui.QApplication.translate("MainWindow", "&Search...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHome.setText(QtGui.QApplication.translate("MainWindow", "&Home", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Complete_History.setText(QtGui.QApplication.translate("MainWindow", "&View Complete History", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_History.setText(QtGui.QApplication.translate("MainWindow", "&Clear History", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
