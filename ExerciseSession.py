import csv,random,sys

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
            print('Successfully loaded {} exercises from {}'.format(self.ex_amount,filename))
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
            print(cleanstr(user_answer)==cleanstr(self.dictionary[self.ex_no % len(self.dictionary)][1]))
            #Check the answer and go to next exercise
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
            
#Basic method that cleans strings for easy comparison
def cleanstr(istring):
    tempstr=istring.lower()
    return tempstr.strip()