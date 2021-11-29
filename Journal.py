import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5 import QtCore
import sys
from datetime import datetime

class MainWindow(qtw.QWidget):
	def __init__(self,fileName):
		super().__init__()
		#Add title
		self.setWindowTitle("Journal.py")
		
		#Set Verticle Layout
		self.setLayout(qtw.QVBoxLayout()) 
		
		#Create label
		title = qtw.QLabel("Journal.py")	
		#Change label font size
		title.setFont(qtg.QFont('Helvetica',18))
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
		if(len(sys.argv) == 2):
			file = open(fileName,'r')
			lines = file.readlines()
			
			for index in range(len(entryObjList)):
				try:
					entryObjList[index].changeText(lines[index])
				except: pass

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
			title.setText(entryObjList[0].returnContent())
			print(fileName)
			with open(fileName,'w') as file:
				for index in range(len(entryObjList)):
					file.write(str(entryObjList[index].returnContent()) + '\n')
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
		fileName = date[0] + ".txt"

		mainWindow = MainWindow(fileName)

	app.exec_()	

if __name__ == "__main__":
	main() 

