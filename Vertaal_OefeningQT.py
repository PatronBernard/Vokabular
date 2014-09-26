import ExerciseSession
import sys 
from PyQt4 import QtGui,QtCore

#PyQT Interface 
class MainWindow(QtGui.QWidget):
    #Logic object
    ExSess=ExerciseSession.ExerciseSession()
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def loadData(self,filename):
        if len(filename)!=0:
            self.ExSess.LoadExercises(filename)
            if self.ExSess.dataLoaded:
                self.writeToLog('Successfully loaded ' + str(self.ExSess.getDictSize()) + ' words from \" ' + filename + ' \" ')
                self.writeToLog('========================================')
                self.ExSess.shuffleExercises()
                self.showExercise()
            else:
                self.writeToLog('Failed to load ' + '\"' + filename + '\"')
        else:
            self.writeToLog('No command line input file supplied. Please restart the application.')

            
                
        
    def initUI(self):    
        #Main window
        self.setWindowTitle('Vocabulary Exercise') 
        self.setGeometry(300, 300, 400, 300)  
        
        #Log
        #!!! WHY SELF? WHY HERE??!!!
        self.outputLog = QtGui.QTextEdit()
        self.outputLog.setReadOnly(True)
        
        #User Input Line
        self.lineEdit=QtGui.QLineEdit()
        
        
        #Submit Button
        sButton=QtGui.QPushButton()
        sButton.setText('Submit')
        sButton.setToolTip('Submit Answer (Enter)')
        sButton.clicked.connect(self.sendToInputProcessor)
        
        #VBox
        vbox=QtGui.QVBoxLayout(self)
        vbox.setGeometry(self.frameGeometry())
        vbox.addWidget(self.outputLog)
        vbox.addWidget(self.lineEdit)
        vbox.addWidget(sButton)
        
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
        
    #Rewrite this whole thing!
    def sendToInputProcessor(self):   
        user_input=self.lineEdit.text()
        self.outputLog.append(user_input)
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
    #Testing the ExerciseSession object
    MainW = MainWindow()
    if len(sys.argv)==2:
        MainW.loadData(sys.argv[1])
    else:
        MainW.loadData('')
        print('No command line filename supplied.')
        
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()   
