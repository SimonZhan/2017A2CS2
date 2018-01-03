# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_main import Ui_MainWindow
from soundProcessing import calculateValue


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main Class
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.guitarString=None
        self.buttons=[self.buttonA,self.buttonB, self.buttonD, self.buttonE1,self.buttonE2, self.buttonG]
        self.labels=[self.labelA, self.labelB, self.labelD, self.labelE1, self.labelE2, self.labelG]
        for i in self.labels:
            i.hide()
        self.setUpProgressBar()
        self.connectCallBack()
        self.animationThread()
        self.value=0
    
    def buttonClicked(self):
        sender=self.sender()
        if self.guitarString!=sender.objectName()[6:]:
            self.guitarString=sender.objectName()[6:]
            for i in self.buttons:
                if i!=sender and i.isChecked():
                    i.setChecked(False)
            for i in self.labels:
                if i.objectName()[5:]==sender.objectName()[6:]:
                    i.show()
                else:
                    i.hide()
        else:
            self.guitarString=None
            for i in self.labels:
                i.hide()
    
    def connectCallBack(self):
        for i in self.buttons:
            i.clicked.connect(self.buttonClicked)
            i.setCheckable(True)

    def animationThread(self):
        t1 = threading.Thread(target=self.animation)
        t1.setDaemon(True)
        t1.start()

    def getValue(self):
        time.sleep(1)
        while 1:
            time.sleep(0.1)
            value=calculateValue(self.guitarString)
            self.lcdNumber.setProperty("intValue", value)
            time.sleep(0.1)
            for i in range(29,0, -1):                
                self.progressBars[i].setValue(self.progressBars[i-1].value())
            self.progressBars[0].setValue(value)
            print(self.progressBars[0].value())
            
    def setUpProgressBar(self):
        self.progressBars=[]
        for i in range(30):
            progressBar = QtWidgets.QProgressBar(self.centralWidget)
            progressBar.setGeometry(QtCore.QRect(0, i*6, 440, 6))
            progressBar.setMinimum(-500)
            progressBar.setMaximum(500)
            progressBar.setValue(0)
            progressBar.setTextVisible(False)
            progressBar.lower()
            self.progressBars.append(progressBar)
    
    def animation(self):
        self.setUpProgressBar()
        self.getValue()
        print(True)

    
if __name__=="__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
