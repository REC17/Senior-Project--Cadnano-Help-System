from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import ui_webwindow, os, getpass, re

global user
user = str(getpass.getuser())

class HistoryList(QDialog):
    def __init__(self, webwindow, parent = None):
        super(HistoryList, self).__init__(parent)
        self.webwindow = webwindow
        self.textbox = QListWidget()
        with open("C:/Users/"+user+"/.cadnano/history.txt", 'r') as history:
            fileList = history.readlines()
        for i in range(len(fileList)):
            if fileList[i] != "about:blank":
                repeattotal = len(self.textbox.findItems(QString(fileList[i].rstrip('\n')), Qt.MatchExactly))
                if len(self.textbox.findItems(QString(fileList[i].rstrip('\n')), Qt.MatchExactly)) > 0:
                    for j in range(repeattotal):
                        self.textbox.removeItemWidget(self.textbox.findItems(QString(fileList[i].rstrip('\n')), Qt.MatchExactly)[j])
                else:
                    self.textbox.addItem(QString(fileList[i].rstrip('\n')))
        self.connect(self.textbox, SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.itemclicked)
        boxLayout = QHBoxLayout()
        boxLayout.addWidget(self.textbox)
        layout = QGridLayout() 
        layout.addLayout(boxLayout, 1,0)
        self.setLayout(layout)
        self.setWindowTitle("History")
                
    def itemclicked(self):
        url = self.textbox.currentItem().text()
        self.webwindow.webView.load(QUrl(url))
        self.webwindow.webView.show() 
        
class WebWindow(QMainWindow, ui_webwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(WebWindow, self).__init__(parent)
        self.setupUi(self)
        self.page = QWebPage()
        self.connect(self.webView, SIGNAL("loadFinished(bool)"), self.historytracker)
        self.triggeronce = True
        self.histlist = []
        self.historyindex = -1
        self.buttonnav = False
        
    def on_homeButton_pressed(self):
        self.webView.load(QUrl("http://www.google.com/"))
        self.webView.show() 

    def on_backButton_pressed(self):
        if self.historyindex > 0:
            self.historyindex = self.historyindex - 1
            self.webView.load(QUrl(self.histlist[self.historyindex]))
        self.buttonnav = True
        print self.histlist
        
    def on_forwardButton_pressed(self):
        if self.historyindex + 1 < len(self.histlist):
            self.historyindex = self.historyindex + 1            
            self.webView.load(QUrl(self.histlist[self.historyindex]))            
            self.buttonnav = True        
        self.buttonnav = True
        print self.histlist
        
    def on_actionHome_triggered(self):
        if self.triggeronce == True:
            self.webView.load(QUrl("http://www.google.com/"))
            self.webView.show() 
        self.triggeronce = not(self.triggeronce)

    def on_actionView_Complete_History_triggered(self):
        if self.triggeronce == True:
            histdialog = HistoryList(self, self)
            histdialog.show()
        self.triggeronce = not(self.triggeronce)
        
    def on_actionClear_History_triggered(self):
        with open("C:/Users/"+user+"/.cadnano/history.txt", 'r') as history:
            fileList = history.readlines()
        with open("C:/Users/"+user+"/.cadnano/history.txt", 'w') as history:
            for i in range(len(fileList)):
                history.write("")
        
    def historytracker(self):
        #repeat = False
        if self.buttonnav == False:
            self.history = self.webView.history().currentItem()
            with open("C:/Users/"+user+"/.cadnano/history.txt", 'r') as history:
                fileList = history.readlines()
            with open("C:/Users/"+user+"/.cadnano/history.txt", 'w') as history:
                for i in range(len(fileList)):
                    if i < (len(fileList)):
                        history.write(fileList[i])
                url = ""
                urlperm = False
                for i in str(self.history.url()):
                    if i == "'":
                        urlperm = not(urlperm)
                    elif urlperm == True:
                        url = url+i
                history.write(url+'\n')
                self.historyindex = self.historyindex + 1
                print len(self.histlist) - self.historyindex
                for i in range(len(self.histlist) - self.historyindex):
                    self.histlist.pop()
                #, self.historyindex
                self.histlist.append(url)
        self.buttonnav = False
        
