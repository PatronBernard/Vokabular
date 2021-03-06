import random,sys
from openpyxl import load_workbook,exceptions
from PyQt4 import QtCore

class ExerciseSession:
    
    def __init__(self):
        self.vocabularium= []   #Contains each word with its translation
        self.score       = 0         
        self.ex_amount   = 1    #Total amount of exercises performed
        self.ex_no       = 1    #Counter that is used to fetch the next exercise
        self.dataLoaded  = False
        self.attemptNo   = 1
        
    def loadExercises(self,filename):
        try: 
            wb=load_workbook(filename)
            ws=wb.active
            for row in ws.rows:
                self.vocabularium.append([row[0].value,row[1].value])
            self.dataLoaded = True
        except:
            pass
            #print('No such file found. Please restart the application.')
            
        
    def shuffleExercises(self):
        if self.dataLoaded:
            random.shuffle(self.vocabularium)
        else:
            pass
            #print('ShuffleExercises: vocabularium is empty!')
                
    def getScore(self):
        return self.score
        
    def resetScore(self):
        self.score=0
        self.ex_amount=1
        
    def getDictSize(self):
        return len(self.vocabularium)
        
    def getExercise(self):
        #print(self.ex_no)
        if self.dataLoaded:
            return str(self.vocabularium[self.ex_no % len(self.vocabularium)][0])

    def checkExercise(self,user_answer):
        if self.dataLoaded:
            if cleanstr(user_answer)==cleanstr(self.vocabularium[self.ex_no % len(self.vocabularium)][1]):
                self.score+=1
                self.attemptNo=1
                return True  
            else:
                return False

    def getRightAnswer(self,question):
        for i,item in enumerate(self.vocabularium):
            if cleanstr(question)==item[0]:
                return item[1]
                
    
    def nextExercise(self):
            self.ex_no+=1
            self.attemptNo=1
            self.ex_amount+=1

    def getScoreStr(self):
        return 'Score: '+ str(self.score) +'/'+str(self.ex_amount) + '\n'
            
#Basic method that cleans and decodes strings for easy comparison.
def cleanstr(istring):
    if isinstance(istring,str):
        tempstr=istring.lower()
        return tempstr.strip()
    #This will have to do, the app will shit itself if istring is not a QString...
    else:
        decoded=str(istring.toUtf8(),'utf-8')
        tempstr=decoded.lower()
        return tempstr.strip()