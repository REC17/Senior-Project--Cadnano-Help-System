# The MIT License
#
# Copyright (c) 2011 Wyss Institute at Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php

from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL, QString
from cadnano import app
from idbank import IdBank
from model.document import Document
from model.encoder import encode
from .documentwindow import DocumentWindow
from .pathhelixgroup import PathHelixGroup
from .slicehelixgroup import SliceHelixGroup
from .treecontroller import TreeController
from .webwindow import WebWindow
from .standardwindow import StdWindow


class DocumentController():
    """
    The document controller. Hooks high level (read file/write file, add
    submodel, etc) UI elements to their corresponding actions in the model
    """

    def __init__(self, firstuse):         
        app().documentControllers.add(self)
        self.doc = Document()
        self.idbank = IdBank()
        self.undoStack = QUndoStack()
        app().undoGroup.addStack(self.undoStack)
        self.win = DocumentWindow(docCtrlr=self)
        self.win.show()
        self.stdwin = StdWindow()
        self.webwin = WebWindow()
        self._filename = "untitled.cadnano"
        self.treeController = TreeController(self.win.treeview)
        self.createConnections()
        
        self.recentButton = None
        
        self.win.sliceGraphicsView.mouseMoveEvent = self.sliceViewMouseMove

        if firstuse == True:
            self.win.helplabel.setText(QString("It appears as though this is your first time using CaDNAno 2, would you like to view a tutorial?"))
        else:
            self.win.ignoreButton.hide()
            self.win.showHelpButton.hide()
            self.win.helplabel.hide()

    def sliceViewMouseMove(self, event):
        
        print "hello"
    """
    Roger Additions
    """
    """
    def helpwindow(self):
        #file = open("usagetracker.txt", 'w')
        filename = "C:/Users/Roger Conturie/workspace/Final Cadnano/cadnano2/ui/usagetracker.txt"
        file = open(filename, 'r')
        timesopened = file.readline()
        file.close()
        if timesopened == '0':
            self.webwin.show()
        file = open(filename, 'w')
        file.write(str(int(timesopened) + 1))
        file.close()
    """

    def standardHelpClicked(self):
        self.stdwin.show()
    
    def networkHelpClicked(self):
        import os
        if os.system("ping google.com -n 1") == 1:
            print "no connection"
        else:
            self.webwin.show()
    
    def ignoreClicked(self):
        self.win.ignoreButton.hide()
        self.win.showHelpButton.hide()
        self.win.helplabel.hide()
        
    def showHelpClicked(self):
        self.stdwin.show()
    """
    End Roger Additions
    """
    
    def filename(self):
        return self._filename

    def setFilename(self, proposedFName):
        if self._filename == proposedFName:
            return True
        self._filename = proposedFName
        self.setDirty(True)
        return True

    def createConnections(self):
        """
        Organizational method to collect signal/slot connectors.
        """
        self.win.actionNewHoneycombPart.triggered.connect(self.hcombClicked)

        self.win.actionNewSquarePart.triggered.connect(self.squareClicked)
        self.win.actionNew.triggered.connect(app().newDocument)
        self.win.actionOpen.triggered.connect(self.openClicked)
        self.win.actionClose.triggered.connect(self.closeClicked)
        self.win.actionSave.triggered.connect(self.saveClicked)
        self.win.actionSVG.triggered.connect(self.svgClicked)
        
        self.win.actionStandard_Help.triggered.connect(self.standardHelpClicked)
        self.win.actionNetwork_Help.triggered.connect(self.networkHelpClicked)
        self.win.ignoreButton.pressed.connect(self.ignoreClicked)
        self.win.showHelpButton.pressed.connect(self.showHelpClicked)
        # self.win.actionSave_As.triggered.connect(self.saveAsClicked)
        # self.win.actionQuit.triggered.connect(self.closeClicked)
        # self.win.actionAdd.triggered.connect(self.addClicked)
        # self.win.actionDelete.triggered.connect(self.deleteClicked)
        # self.win.actionCut.triggered.connect(self.cutClicked)
        # self.win.actionPaste.triggered.connect(self.pasteClicked)
        # self.win.actionMoveUp.triggered.connect(self.moveUpClicked)
        # self.win.actionMoveDown.triggered.connect(self.moveDownClicked)
        # self.win.actionPromote.triggered.connect(self.promoteClicked)
        # self.win.actionDemote.triggered.connect(self.demoteClicked)
    # end def

        
    def setDirty(self, dirty=True):
        self.win.setWindowModified(dirty)
    #end def

    def newClicked(self):
        """docstring for newClicked"""
        print "new clicked"
        self.recentButton = "new"
    # end def
    def openClicked(self):
        """docstring for openClicked"""
        print "open clicked"
        self.recentButton = "open"
    # end def        
    def closeClicked(self):
        """docstring for closeClicked"""
        print "close clicked"
        self.recentButton = "close"
    # end def

    def saveClicked(self):
        """docstring for saveClicked"""
        try:
            f = open(self.filename())
            f.write(encode(self.doc))
            f.close()
        except Exception:
            print "Save "
        return True
        self.recentButton = "save"
        
    def saveAsClicked():
        filename = self.filename()
        if filename == None:
            directory = "."
        else:
            directory = QFileInfo(filename).path()
        filename = QFileDialog.getSaveFileName(self.win,\
                            "%s - Save As" % QApplication.applicationName(),\
                            directory,\
                            "%s (*.cadnano)" % QApplication.applicationName())
        if filename.isEmpty():
            return False
        if not filename.toLower().endswith(".cadnano"):
            filename += ".cadnano"
        self.setFilename(filename)
        self.recentButton = "saveAs"
        return self.saveClicked()

    def svgClicked(self):
        """docstring for svgClicked"""
        print "svg clicked"
        self.recentButton = "svg"

    # end def

    def hcombClicked(self):
        """docstring for hcombClicked"""
        print "+honeycomb clicked"
        self.addHoneycombHelixGroup()
        self.recentButton = "hcomb"

    # end def

    def squareClicked(self):
        """docstring for squareClicked"""
        print "+square clicked"
        self.recentButton = "square"
    # end def

    def addHoneycombHelixGroup(self, nrows=20, ncolumns=20):
        """docstring for addHoneycombHelixGroup"""
        # Create a new DNA part
        objId = self.idbank.get()
        instId = objId#self.idbank.get()
        dnaPartInst = self.doc.addDnaPart(objId, instId,\
                                          crossSectionType='honeycomb')
        # Add the part to the Tree view
        name = "Part.%d" % objId 
        self.treeController.addPartNode(name, dnaPartInst)

        # Create a Slice view of part
        shg = SliceHelixGroup(dnaPartInst, nrows, ncolumns,\
                              scene=self.win.slicescene,\
                              controller=self.win.sliceController)
        self.win.slicescene.addItem(shg)

        # Create a Path view of the part
        phg = PathHelixGroup(dnaPartInst, scene=self.win.pathscene,\
                             controller=self.win.pathController)
        self.win.pathscene.addItem(phg)

        # Connect the slice
        shg.helixAdded.connect(phg.handleHelixAdded)
        shg.sliceHelixClicked.connect(phg.handleSliceHelixClick)
        dnaPartInst.partselected.connect(shg.bringToFront)
        dnaPartInst.partselected.connect(phg.bringToFront)
        self.recentButton = "addHoneycombHelixGroup"

    # end def

    def deleteClicked(self):
        index = self.win.treeview.currentIndex()
        if not index.isValid():
            return
        name = self.treemodel.data(index).toString()
        rows = self.treemodel.rowCount(index)
        if rows == 0:
            message = "<p>Delete '%s'" % name
        # end if
        elif rows == 1:
            message = "<p>Delete '%s' and its child (and " +\
                         "grandchildren etc.)" % name
        # end elif
        elif rows > 1:
            message = "<p>Delete '%s' and its %d children (and " +\
                         "grandchildren etc.)" % (name, rows)

        # end elif
        if not self.okToDelete(this, QString("Delete"), QString(message)):
            return
        self.treemodel.removeRow(index.row(), index.parent())
        self.setDirty(True)
        self.updateUi()
        self.recentButton = "addHoneycombHelixGroup"

    # end def

    def okToDelete(self, parent, title, text, detailedText):
        """
        """
        messageBox = QMessageBox(parent)
        if parent:
            messageBox.setWindowModality(Qt.WindowModal)
        # end if
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setWindowTitle(\
            QString("%1 - %2").arg(QApplication.applicationName()).arg(title))
        messageBox.setText(text)
        if not detailedText.isEmpty():
            messageBox.setInformativeText(detailedText)
        # end if
        deleteButton = messageBox.addButton(QString("&Delete"),\
                                            QMessageBox.AcceptRole)
        messageBox.addButton(QString("Do &Not Delete"),\
                             QMessageBox.RejectRole)
        messageBox.setDefaultButton(deleteButton)
        messageBox.exec_()
        return messageBox.clickedButton() == deleteButton
    # end def

    def okToClear(self, savedata, parent, title, text, detailedText):
        """
        savedata is a function pointer
        """
        assert savedata and parent
        messageBox = QMessageBox(parent)
        if parent:
            messageBox.setWindowModality(Qt.WindowModal)
        # end if
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setWindowTitle(\
          QString("%1 - %2").arg(QApplication.applicationName()).arg(title))
        messageBox.setText(text)
        if not detailedText.isEmpty():
            messageBox.setInformativeText(detailedText)
        # end if

        saveButton = messageBox.addButton(QMessageBox.Save)
        messageBox.addButton(QMessageBox.Save)
        messageBox.addButton(QMessageBox.Discard)
        messageBox.addButton(QMessageBox.Cancel)
        messageBox.setDefaultButton(saveButton)
        messageBox.exec_()
        if messageBox.clickedButton() == messageBox.button(QMessageBox.Cancel):
            return False
        if messageBox.clickedButton() == messageBox.button(QMessageBox.Save):
            return parent.savedata()  # how to return the function (lambda?)
        return True
    # end def

    def createAction(self, icon, text, parent, shortcutkey):
        """
        returns a QAction object
        """
        action = QAction(QIcon(icon), text, parent)
        if not shorcutkey.isEmpty():
            action.setShortcut(shortcutkey)
        # end if
        return action
    # end def

    def updateUi(self):
        """
        """
        #self.win.actionSave.setEnabled(self.win.isWindowModified())

        rows = self.treemodel.rowCount()

        #self.win.actionSave_As.setEnabled(self.win.isWindowModified() or rows)
        #self.win.actionHideOrShowItems.setEnabled(rows)
        enable = self.win.treeview.currentIndex().isValid()

        # actions = [self.win.actionDelete,\
        #            self.win.actionMoveUp,\
        #            self.win.actionMoveDown,\
        #            self.win.actionCut,\
        #            self.win.actionPromote,\
        #            self.win.actionDemote]
        # for action in actions:
        #     action.setEnabled(enable)
        # # end for
        # self.win.actionStartOrStop.setEnabled(rows);
        # self.win.actionPaste.setEnabled(self.treemodel.hasCutItem())
    #end def

    def cutClicked(self):
        """"""
        self.win.actionPaste.setEnabled(self.treeController.cut())
    # end def

    def pasteClicked(self):
        """"""
        self.treeController.paste()
    # end def

    def moveUpClicked(self):
        """"""
        self.treeController.moveUp()
    # end def

    def moveDownClicked(self):
        """"""
        self.treeController.moveDown()
    # end def

    def promoteClicked(self):
        """"""
        self.treeController.promote()
    #end def

    def demoteClicked(self):
        """"""
        self.treeController.demote()
    #end def

    def hideOrShowNode(self, hide, index):
        """"""
        self.treeController.hideOrShowNode()
    # end def
# end class
