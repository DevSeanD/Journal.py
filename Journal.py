"""
Developer: DevSeanD
Description: Journal.py is a simple Journaling application that uses PyQt5 as a front end
File Name: Journal.py

TODO:
	Add a function that will create the dir Logs if it does not exist already
"""
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5 import QtCore
import sys
import os
from datetime import datetime
import os.path

class MainWindow(qtw.QWidget):
	def __init__(self,fileName):
		super().__init__()
		#Add title
		self.setWindowTitle("Journal.py")
		self.setGeometry(100, 60, 400, 200)
		
		#Set Verticle Layout
		self.setLayout(qtw.QVBoxLayout()) 
		
		#Create label
		title = qtw.QLabel("Journal.py")	
		#Change label font size
		title.setFont(qtg.QFont('Helvetica',25))
		#Add to layout
		self.layout().addWidget(title)

		# If the user request an existing file
		if(len(sys.argv) == 2):
			fileName = sys.argv[1]	
		
		#Create entry box
		"""
		entry = qtw.QLineEdit()
		entry.setObjectName("field0")
		#Add to layout
		self.layout().addWidget(entry)
		"""
		entryObjList = []
		
		for index in range(9):
			entryObjList.append(entryBox("field0"))
			self.layout().addWidget(entryObjList[index].returnObj())
		try:
			file = open(fileName,'r')
			lines = file.readlines()
			
			for index in range(len(entryObjList)):
				try:
					if(lines[index][0] == "\n"):
						entryObjList[index].changeText(lines[index][1:])
					else:
						entryObjList[index].changeText(lines[index])
				except: 
					pass
		except:
			file = open(fileName,'w')
			for index in range(9):
				file.write('\n')
			file.close()
			print("Created new file {}".format(fileName))	

		#Create a button
		button = qtw.QPushButton("Save",clicked=lambda: save())
		#Add to layout
		self.layout().addWidget(button)

		#Create checkbox
		"""	
		checkObj = checkBox()
		#Add to layout
		self.layout().addWidget(checkObj.returnObj())
		"""
		
		#Show app
		self.show()

		def loadContent():
			with open(fileName,'r') as file:
				for line in file:
					print(line)

		def save():
			with open(fileName,'w') as file:
				for index in range(len(entryObjList)):
					print(str(entryObjList[index].returnContent()))
					if(str(entryObjList[index].returnContent()).count("\n") >= 1):
						file.write(str(entryObjList[index].returnContent()))
					else:
						file.write(str(entryObjList[index].returnContent()) + "\n")
				file.close()

class entryBox():
	def __init__(self,entryName):
		self.entry = qtw.QLineEdit()
		self.entry.setObjectName(entryName)

	def changeText(self,newText):
		self.entry.setText(newText)

	def returnContent(self):		
		return self.entry.text()

	def returnObj(self):
		return self.entry	

class checkBox():
	def __init__(self):
		self.checkBox = qtw.QCheckBox()

	def returnObj(self):
		return self.checkBox

def main():	
	app = qtw.QApplication([])
	
	# If the user request an existing file
	if(len(sys.argv) == 2):
		mainWindow = MainWindow(sys.argv[1])
	else:
		date = datetime.now()
		date = str(date).split()
		fileName = "Logs/" + date[0] + ".txt"
		mainWindow = MainWindow(fileName)

	app.exec_()	

if __name__ == "__main__":
	main()
 
