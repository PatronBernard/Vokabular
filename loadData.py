import csv,sys,openpyxl

def unicode_csv_reader(unicode_csv_data):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data))
    for row in csv_reader:
        yield [cell for cell in row]
        # decode UTF-8 back to Unicode, cell by cell:
        #yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')            
        

filename='testopgave.csv'
dictionary=[]
try:
    with open(filename,mode='rt',encoding='utf-8') as fin:
        reader = csv.reader(fin)
        for row in reader:
            dictionary.append(row)
        print('Successfully loaded {} exercises from {}'.format(len(dictionary),filename))
        print(dictionary[0][0])
except IOError:
    print('No file found. Make sure it exists!')