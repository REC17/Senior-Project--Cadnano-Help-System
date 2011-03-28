from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_standardhelp, os

class StdWindow(QMainWindow, ui_standardhelp.Ui_StandardHelp):
    def __init__(self, parent=None):
        super(StdWindow, self).__init__(parent)
        self.setupUi(self)
        self.triggeronce = True
     #   self.textBrowser.setSource(QUrl.fromLocalFile("ui/helpdocs/Slice View.html"))
        self.connect(self.treeWidget, SIGNAL("itemActivated(QTreeWidgetItem*, int)"), self.displayContent)
        
      #  print self.treeWidget.currentColumn()
        self.enterSearch = False
        self.searchEdit.focusInEvent = self.searchFocusIn
        self.searchEdit.focusOutEvent = self.searchFocusOut
        
    def searchFocusIn(self, event):
        self.enterSearch = True
    
    def searchFocusOut(self, event):
        self.enterSearch = False
    
    def keyPressEvent(self, event):
        if event.key() == 16777220 and self.enterSearch == True:
            self.executeSearch()
    
    def displayContent(self):
        if self.treeWidget.currentItem().parent()!= None:
            if self.treeWidget.currentItem().parent().text(0) == "Slice View":
                url = ""
                for letter in str(self.treeWidget.currentItem().text(0)):
                    if letter == "/":
                        url = url
                    else:
                        url = url + letter
                url = "Slice"+url+".html"
                self.textBrowser.setSource(QUrl.fromLocalFile("ui/helpdocs/"+url))
    
    def on_searchButton_pressed(self):
        self.executeSearch()
        
    def executeSearch(self):
        searchstring = str(self.searchEdit.text())
        helpdoclist = os.listdir("ui/helpdocs")
  #      matchlist = []
        matchdict = {}
        for doc in helpdoclist:
            with open("ui/helpdocs/"+doc, 'r') as opendoc:
                lines = opendoc.readlines()
                searchcount = 0
                for line in range(len(lines)):
                    if lines[line][0] == '<':
                        pass
                    else:
                     #   try:
                   #     lines[line].index(searchstring)
                        searchcount = searchcount+lines[line].lower().count(searchstring.lower(), 0, len(lines[line]))
                        if searchcount > 0:
                            matchdict.update({doc:searchcount})
   #     print matchdict
        try:
            matchdict.__delitem__('SearchResults.html')
        except:
            pass
        
        with open("ui/helpdocs/SearchResults.html", 'r') as SR:
            searchresults = SR.readlines()
        with open("ui/helpdocs/SearchResults.html", 'w') as SR:
            for line in range(len(searchresults)):
                if line == 3 and len(matchdict) > 0:
                    matchrank = []
                    for item in matchdict:
                        matchrank.append(matchdict[item])
                    matchrank.sort()
                    matchrank.reverse()
                    for rank in matchrank:
                        for duplicate in range(matchrank.count(rank)-1):
                            matchrank.remove(rank)
                    results = []
                    for rank in matchrank:
                        for item in matchdict:
                            if matchdict[item] == rank:
                                results.append(item)
                    resultcount = 0
                    for item in results:
                        resultcount = resultcount + 1
                        with open("ui/helpdocs/"+item, 'r') as opendoc:
                            doclines = opendoc.readlines()
                            for line in doclines:
                                try:
                                    line.index('<H2>')
                                    line = line.strip('<H2>')
                                    line = line.rstrip('</H2>\n')
                                    break
                                except:
                                    pass
                        SR.write("%s.) "%str(resultcount))
                        SR.write('<a href="'+item+'">%s</a><p>'%line)
           #             SR.write(str(item))
                    SR.write("\n")
                elif line == 3:
                    SR.write("Search Completed: No Results Found\n")

                else:
                    SR.write(searchresults[line])

        self.textBrowser.setSource(QUrl.fromLocalFile("ui/helpdocs/SearchResults.html"))

    def on_actionClose_triggered(self):
        if self.triggeronce == True:
            self.close()
        self.triggeronce = not(self.triggeronce)
