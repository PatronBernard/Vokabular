from openpyxl import load_workbook

dictionary=[]
wb=load_workbook('testopgave.xlsx')
ws=wb.active
for row in ws.rows:
    for cell in row:
        print (cell.value)