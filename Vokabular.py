import ExerciseSession
import sys 
from PyQt4 import QtGui,QtCore

#PyQT Interface 
class MainWindow(QtGui.QWidget):
    
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
            self.writeToLog('No command line input file supplied.')
            arg_file=open('default.txt','r')
            filename=arg_file.readline()
            self.loadData(filename)
            arg_file.close()


            
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
                self.writeToLog(self.ExSess.getScoreStr())
                self.ExSess.nextExercise()
            elif self.ExSess.attemptNo % 3 != 0:
                #Adjust log message to plural/singular
                if 3-self.ExSess.attemptNo == 1:
                    plural = ' '
                else:
                    plural = 's '
                
                self.writeToLog(    'Incorrect. ' +
                                    str(3-self.ExSess.attemptNo) + 
                                    ' attempt'+
                                    plural +
                                    'remaining. \n')
                self.ExSess.attemptNo+=1
            else:
                self.writeToLog(    'Incorrect. The right answer was: ' + 
                                    self.ExSess.getRightAnswer(self.ExSess.getExercise()) + 
                                    '\n Score: '+ str(self.ExSess.getScore()) + 
                                    '/' + 
                                    str(self.ExSess.ex_amount) + '\n')
                self.ExSess.nextExercise()
                self.ExSess.attemptNo=1
            if self.ExSess.ex_no==(len(self.ExSess.vocabularium)+1):
                self.writeToLog('Done! Resetting score...') 
                self.ExSess.resetScore()
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
        MainW.loadData('')
        #print('No command line filename supplied. Reverting to default "testopgave.xlsx"')
        
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()   
