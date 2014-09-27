import ExerciseSession
import sys 
from PyQt4 import QtGui,QtCore

#PyQT Interface 
class MainWindow(QtGui.QWidget):
    #This is the internal logic class

    
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ExSess=ExerciseSession.ExerciseSession()
        self.initUI()
  
  
    def loadData(self,filename):
        if len(filename)!=0:
            self.ExSess.loadExercises(filename)
            if self.ExSess.dataLoaded:
                self.writeToLog('Successfully loaded ' + str(self.ExSess.getDictSize()) + ' words from \" ' + filename + ' \" ')
                self.writeToLog('==============================================')
                self.ExSess.shuffleExercises()
                self.showExercise()
            else:
                self.writeToLog('Failed to load ' + '\"' + filename + '\"')
                self.writeToLog('Please restart the application.')
        else:
            self.writeToLog('No command line input file supplied. Please restart the application.')

            
    def initUI(self):    
        #Main window
        self.setWindowTitle('Vocabulary Exercise') 
        self.setGeometry(300, 300, 400, 300)  
        
        #Log
        self.outputLog = QtGui.QTextEdit()
        self.outputLog.setReadOnly(True)
        
        #User Input Line
        self.lineEdit=QtGui.QLineEdit()
         
        #Submit Button
        self.sButton=QtGui.QPushButton()
        self.sButton.setText('Submit')
        self.sButton.setToolTip('Submit Answer (Enter)')
        self.sButton.clicked.connect(self.sendToInputProcessor)
        
        #VBox
        self.vbox=QtGui.QVBoxLayout(self)
        self.vbox.setGeometry(self.frameGeometry())
        self.vbox.addWidget(self.outputLog)
        self.vbox.addWidget(self.lineEdit)
        self.vbox.addWidget(self.sButton)
        
        #Signal connections
        self.lineEdit.setFocus()
        self.show()
        
        
    def writeToLog(self,istring):
        self.outputLog.append(istring)
        
        
    def getUserInput(self):
        user_input=self.lineEdit.text()
        return user_input
        
        
    def showExercise(self):
        self.writeToLog(self.ExSess.getExercise())
        
        
    def sendToInputProcessor(self):   
        user_input=self.lineEdit.text()
        self.outputLog.append('>'+user_input)
        self.lineEdit.setText('')
        self.lineEdit.setFocus()
        self.inputProcessor(user_input)
    

    def inputProcessor(self,input_str):
        if self.ExSess.dataLoaded:
            if(self.ExSess.checkExercise(input_str)):
                self.writeToLog('Correct! Score: '+ str(self.ExSess.getScore()) + '/' + str(self.ExSess.ex_amount) + '\n')
            else:
                self.writeToLog('Incorrect. Score: '+ str(self.ExSess.getScore()) + '/' + str(self.ExSess.ex_amount) + '\n')
            self.ExSess.nextExercise()
            if self.ExSess.ex_no==(self.ExSess.ex_amount-1):
                self.writeToLog('Done! Resetting score...') 
            self.showExercise()
        
            
    def keyPressEvent(self, e):

        if  e.key() == QtCore.Qt.Key_Escape:
            self.close()   
        elif e.key() == QtCore.Qt.Key_Enter:
            self.sendToInputProcessor()
        elif e.key() == QtCore.Qt.Key_Return:
            self.sendToInputProcessor()

        
    
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    MainW = MainWindow()
    if len(sys.argv)==2:
        MainW.loadData(sys.argv[1])
    else:
        MainW.loadData('testopgave.xlsx')
        print('No command line filename supplied. Reverting to default "testopgave.xlsx"')
        
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()   
