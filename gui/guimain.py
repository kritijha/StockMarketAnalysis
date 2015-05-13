from __future__ import division
import project
import sys
from PyQt4.QtGui import *
from project import Ui_Form
from PyQt4 import QtCore
import numpy as np
import matplotlib.pyplot as plt


class project(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.plotgraph)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self.predictstock)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL('clicked()'),self.lets_do_it)
        self.ui.label_3.hide()
        self.ui.label_2.hide()
        self.ui.pushButton_3.hide()
        self.ui.lineEdit_2.hide()  
        
        
    def plotgraph(self):
        s=self.ui.lineEdit.text()
        arr=[]
	arr2=[]
	for line in open('out.txt'):
		line=line.strip()
		list=line.split(',')
		if list[0]==s:
			arr.append(float(list[1]))
			arr2.append(float(list[2]))
	arr.sort()
	plt.plot(arr,arr2,'bo')
	plt.title("CUMULATIVE DISTRIBUTIVE FUNCTION")
	plt.ylabel("CDF")
	plt.xlabel("% CHANGE")
	plt.show()
        
 
    def predictstock(self):
        self.ui.label_3.show()
        
        self.ui.pushButton_3.show()
        self.ui.lineEdit_2.show() 
        
    def lets_do_it(self):
        self.ui.label_2.show()
        tmp=self.ui.lineEdit_2.text()
        t=self.ui.lineEdit.text()
        
        count=0
        
        for line in open('out.txt'):
            line = line.strip()
            list = line.split(',')
            if list[0]==t:
                if list[1]>=tmp:
                    count+=1
           
                    
        p=count/240
        self.ui.label_2.setNum(p)   
        
 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = project()
    myapp.show()
    sys.exit(app.exec_())
