from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

import ui_webwindow

class WebWindow(QMainWindow, ui_webwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(WebWindow, self).__init__(parent)
        self.setupUi(self)
        self.page = QWebPage()

    def on_pushButton_released(self):
        self.webView.load(QUrl("http://www.facebook.com/"))
        self.webView.show()
        
def main():
    app = QApplication(sys.argv)
    window = WebWindow()
    window.show()
    app.exec_()

main()



