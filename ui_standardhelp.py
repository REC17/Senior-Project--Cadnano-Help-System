# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standardhelp.ui'
#
# Created: Sat Mar 26 20:43:15 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StandardHelp(object):
    def setupUi(self, StandardHelp):
        StandardHelp.setObjectName(_fromUtf8("StandardHelp"))
        StandardHelp.resize(850, 431)
        self.centralWidget = QtGui.QWidget(StandardHelp)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.homeButton = QtGui.QPushButton(self.centralWidget)
        self.homeButton.setObjectName(_fromUtf8("homeButton"))
        self.horizontalLayout.addWidget(self.homeButton)
        self.backButton = QtGui.QPushButton(self.centralWidget)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        self.forwardButton = QtGui.QPushButton(self.centralWidget)
        self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
        self.horizontalLayout.addWidget(self.forwardButton)
        self.searchEdit = QtGui.QLineEdit(self.centralWidget)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.searchButton = QtGui.QPushButton(self.centralWidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout.addWidget(self.searchButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.treeWidget = QtGui.QTreeWidget(self.splitter)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.treeWidget.setToolTip(_fromUtf8(""))
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.textBrowser = QtGui.QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)
        StandardHelp.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(StandardHelp)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        StandardHelp.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(StandardHelp)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        StandardHelp.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(StandardHelp)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        StandardHelp.setStatusBar(self.statusBar)
        self.actionClose = QtGui.QAction(StandardHelp)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionClose)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(StandardHelp)
        QtCore.QMetaObject.connectSlotsByName(StandardHelp)

    def retranslateUi(self, StandardHelp):
        StandardHelp.setWindowTitle(QtGui.QApplication.translate("StandardHelp", "StandardHelp", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setText(QtGui.QApplication.translate("StandardHelp", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("StandardHelp", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.forwardButton.setText(QtGui.QApplication.translate("StandardHelp", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("StandardHelp", "Search...", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("StandardHelp", "Help Topics", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("StandardHelp", "Oragami Concepts", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("StandardHelp", "Preparation", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("StandardHelp", "Imaging", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(2).setText(0, QtGui.QApplication.translate("StandardHelp", "3D", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(3).setText(0, QtGui.QApplication.translate("StandardHelp", "2D", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("StandardHelp", "Cadnano Layout", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("StandardHelp", "Tree View", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("StandardHelp", "Slice View", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).child(0).setText(0, QtGui.QApplication.translate("StandardHelp", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).child(1).setText(0, QtGui.QApplication.translate("StandardHelp", "Renum", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).child(2).setText(0, QtGui.QApplication.translate("StandardHelp", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).child(3).setText(0, QtGui.QApplication.translate("StandardHelp", "First/Last", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).child(4).setText(0, QtGui.QApplication.translate("StandardHelp", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).setText(0, QtGui.QApplication.translate("StandardHelp", "Path View", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).child(0).setText(0, QtGui.QApplication.translate("StandardHelp", "Staple", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).child(1).setText(0, QtGui.QApplication.translate("StandardHelp", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).child(2).setText(0, QtGui.QApplication.translate("StandardHelp", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).child(3).setText(0, QtGui.QApplication.translate("StandardHelp", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).child(4).setText(0, QtGui.QApplication.translate("StandardHelp", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).child(5).setText(0, QtGui.QApplication.translate("StandardHelp", "Force", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).child(6).setText(0, QtGui.QApplication.translate("StandardHelp", "Erase", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).child(7).setText(0, QtGui.QApplication.translate("StandardHelp", "Break", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).setText(0, QtGui.QApplication.translate("StandardHelp", "Main Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).child(0).setText(0, QtGui.QApplication.translate("StandardHelp", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).child(1).setText(0, QtGui.QApplication.translate("StandardHelp", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).child(2).setText(0, QtGui.QApplication.translate("StandardHelp", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).child(3).setText(0, QtGui.QApplication.translate("StandardHelp", "SVG", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).child(4).setText(0, QtGui.QApplication.translate("StandardHelp", "Honeycomb", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).child(5).setText(0, QtGui.QApplication.translate("StandardHelp", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).setText(0, QtGui.QApplication.translate("StandardHelp", "Design Techniques", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(3).setText(0, QtGui.QApplication.translate("StandardHelp", "Glossary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(QtGui.QApplication.translate("StandardHelp", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("StandardHelp", "Exit", None, QtGui.QApplication.UnicodeUTF8))

