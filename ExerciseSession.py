import csv,random,sys
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
        try:
            with open(filename,'rt') as fin:
                reader = csv.reader(fin)
                for row in reader:
                    self.dictionary.append(row)
            print('Successfully loaded {} exercises from {}'.format(len(self.dictionary),filename))
            self.dataLoaded=True
        except FileNotFoundError:
            print('LoadExercises: No file found. Make sure it exists!')
            
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
            print("Checking equality")
            type(cleanstr(user_answer))
            type(cleanstr(self.dictionary[self.ex_no % len(self.dictionary)][1]))
            cleanstr(user_answer)==cleanstr(self.dictionary[self.ex_no % len(self.dictionary)][1])
            print("=======")
            #Check the answer and go to next exercise
            print type(self.dictionary[self.ex_no % len(self.dictionary)][1])
            if True: #cleanstr(user_answer)==cleanstr(self.dictionary[self.ex_no % len(self.dictionary)][1]):
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
    elif isinstance(istring,QtCore.QString):
        decoded=unicode(istring.toUtf8(),'utf-8')
        tempstr=decoded.lower()
        return tempstr.strip()
    
   
    