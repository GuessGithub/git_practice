# -*- coding:gb2312 -*-

#
import os

# For excel reading
import xlrd

# For word processing
import docx
#from docx.enum.table import WD_TABLE_ALIGNMENT

from docx.oxml.shared import OxmlElement, qn # make the content of cell center

# Bebgin Here


book = xlrd.open_workbook("group_student2.xlsx")

doc = docx.Document('record.docx')
table = doc.tables
tab = table[0]



# Get the number of sheets
#print("The number of worksheets is {0}" .format(book.nsheets))
#print("Worksheet name(s):{0}".format(book.sheet_names()))
#sheet = book.sheet_names()[0]  # Get the sheet name
# Get the type of cell
#print sheet.cell(6,7).ctype                 

sheet = book.sheet_by_index(0)  # Get the sheet reference to use   

#look = sheet.cell(5,5).value.encode('utf-8') # Get the content of cell(row,col)

for i_excel in range(1,26):
    for j_word in range(1,6,2):
        tab.cell(0,j_word).text = sheet.cell(i_excel,j_word+3).value# Get the content of cell(row,col)
        # make the content of cell center
        tc = tab.cell(0,j_word)._tc
        tcPr = tc.get_or_add_tcPr()
        tcVAlign = OxmlElement('w:vAlign')
        tcVAlign.set(qn('w:val'), "center")
        tcPr.append(tcVAlign)
        
    tab.cell(1,1).text=sheet.cell(i_excel,9).value
    tc = tab.cell(1,1)._tc
    tcPr = tc.get_or_add_tcPr()
    tcVAlign = OxmlElement('w:vAlign')
    tcVAlign.set(qn('w:val'), "center")
    tcPr.append(tcVAlign)
    
    for j_word in range(1,4,2):
        tab.cell(2,j_word).text = sheet.cell(i_excel,j_word+9).value# Get the content of cell(row,col)
        tc = tab.cell(2,j_word)._tc
        tcPr = tc.get_or_add_tcPr()
        tcVAlign = OxmlElement('w:vAlign')
        tcVAlign.set(qn('w:val'), "center")
        tcPr.append(tcVAlign)

    tab.cell(2,6).text=sheet.cell(i_excel,14).value
    tc = tab.cell(2,6)._tc
    tcPr = tc.get_or_add_tcPr()
    tcVAlign = OxmlElement('w:vAlign')
    tcVAlign.set(qn('w:val'), "center")
    tcPr.append(tcVAlign)
    
    filename = str(i_excel)+tab.cell(0,1).text + '.docx'
    filename = os.path.join('.\\records\\',filename)
    doc.save(filename)
    print('Saved!')

print('Congratulations!')


