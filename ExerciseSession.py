import random,sys
from openpyxl import load_workbook
from PyQt4 import QtCore

class ExerciseSession:
    dictionary  =[]   #Contains each word with its translation
    score       =0         
    ex_amount   =0
    ex_no       =1
    dataLoaded  =False
    
    def __init__(self):
        pass
        
    def LoadExercises(self,filename):
        wb=load_workbook(filename)
        ws=wb.active
        for row in ws.rows:
            self.dictionary.append([row[0].value,row[1].value])
        for word in self.dictionary:
            print(word)
            
        self.dataLoaded = True
    def shuffleExercises(self):
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
            return str(self.dictionary[self.ex_no % len(self.dictionary)][0])

    def checkExercise(self,user_answer):
        if self.dataLoaded:
            self.ex_amount+=1
            if cleanstr(user_answer)==cleanstr(self.dictionary[self.ex_no % len(self.dictionary)][1]):
                self.score+=1
                return True  
            else:
                return False
                
    
    def nextExercise(self):
        #if self.ex_no < self.ex_amount-1:
            self.ex_no+=1
        #else:
            #self.ex_no=0
            #self.resetScore()
            
#Basic method that cleans and decodes strings for easy comparison
def cleanstr(istring):
    if isinstance(istring,str):
        tempstr=istring.lower()
        return tempstr.strip()
    #elif isinstance(istring,QtCore.QString):
    #This will have to do
    else:
        decoded=str(istring.toUtf8(),'utf-8')
        tempstr=decoded.lower()
        return tempstr.strip()
    
   
    