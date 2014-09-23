import csv,random,sys

class ExerciseSession:
    dictionary  =[]   #Contains each word with its translation
    score       =0         
    ex_amount   =0
    ex_no       =0
    dataLoaded  =False
    
    def __init__(self):
        pass
        
    def LoadExercises(self,filename):
        try:
            with open(filename,'rt') as fin:
                reader = csv.reader(fin)
                for row in reader:
                    self.dictionary.append(row)
            print('Successfully loaded {} exercises from {}'.format(self.ex_amount,filename))
            self.dataLoaded=True
        except FileNotFoundError:
            print('LoadExercises: No file found. Make sure it exists!')
        self.ex_amount=len(self.dictionary)
        self.ex_no=0 
    def ShuffleExercises(self):
        if self.dataLoaded:
            random.shuffle(self.dictionary)
        else:
            print('ShuffleExercises: Dictionary is empty!')
                
    def getScore(self):
        return self.score
        
    def resetScore(self):
        self.score=0
        
    def getDictSize(self):
        return len(self.dictionary)
        
    def getExercise(self):
        print(self.ex_no)
        if self.dataLoaded:
            return str(self.dictionary[self.ex_no][0])
        
    def checkExercise(self,user_answer):
        if self.dataLoaded:
            print(cleanstr(user_answer)==cleanstr(self.dictionary[self.ex_no][1]))
            #Check the answer and go to next exercise
            if cleanstr(user_answer)==cleanstr(self.dictionary[self.ex_no][1]):
                self.score+=1
                return True  
            else:
                return False
    
    def nextExercise(self):
        if self.ex_no < self.ex_amount-1:
            self.ex_no+=1
        else:
            self.ex_no=0
            self.resetScore()
            
#Basic method that cleans strings for easy comparison
def cleanstr(istring):
    tempstr=istring.lower()
    return tempstr.strip()
    

from PyQt4 import QtGui,QtCore
#PyQT Interface 
class MainWindow(QtGui.QWidget):
    #Logic object
    ExSess=ExerciseSession()
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def loadData(self,filename):
        if len(filename)!=0:
            self.ExSess.LoadExercises(filename)
            if self.ExSess.dataLoaded:
                self.writeToLog('Successfully loaded ' + str(self.ExSess.getDictSize()) + ' words from \" ' + filename + ' \" ')
                self.writeToLog('========================================')
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
        sButton.clicked.connect(self.processUserInput)
        
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
        
    #Better split this into gathering and processing the input!
    def processUserInput(self):
        if self.ExSess.ex_no==(self.ExSess.ex_amount-1):
            self.writeToLog('Done! Resetting score...')    
        user_input=str(self.lineEdit.text())
        self.outputLog.append(user_input)
        self.lineEdit.setText('')
        self.lineEdit.setFocus()
        if self.ExSess.dataLoaded:
            if(self.ExSess.checkExercise(user_input)):
                self.writeToLog('Correct! Score: '+ str(self.ExSess.getScore()) + '/' + str(self.ExSess.getDictSize()) + '\n')
            else:
                self.writeToLog('Incorrect. Score: '+ str(self.ExSess.getScore()) + '/' + str(self.ExSess.getDictSize()) + '\n')
            self.ExSess.nextExercise()
            self.showExercise()

            
    def keyPressEvent(self, e):

        if  e.key() == QtCore.Qt.Key_Escape:
            self.close()   
        elif e.key() == QtCore.Qt.Key_Enter:
            self.processUserInput()
        elif e.key() == QtCore.Qt.Key_Return:
            self.processUserInput()

        
        
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
