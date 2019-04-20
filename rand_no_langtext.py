import xlrd
wb=xlrd.open_workbook('random_no_replace.xls')
hn=open('hindi.txt','a+',encoding='utf-8')
mr=open('marathi.txt','a+',encoding='utf-8')
asm=open('assamese.txt','a+',encoding='utf-8')
bn=open('bengali.txt','a+',encoding='utf-8')
pn=open('Punjabi.txt','a+',encoding='utf-8')
gu=open('Gujarati.txt','a+',encoding='utf-8')
od=open('Odia.txt','a+',encoding='utf-8')
tm=open('Tamil.txt','a+',encoding='utf-8')
tl=open('Telugu.txt','a+',encoding='utf-8')
kn=open('Kannada.txt','a+',encoding='utf-8')
ml=open('Malayalam.txt','a+',encoding='utf-8')
for sno in range(wb.nsheets-1):
    sheet1=wb.sheet_by_index(sno)
    for i in range(1,sheet1.nrows):
        if sheet1.cell_value(i, 0) != '':
            hn.write(sheet1.cell_value(i, 0)+ '\n')
        if sheet1.cell_value(i, 1) != '':
            mr.write(sheet1.cell_value(i, 1) + '\n')
        if sheet1.cell_value(i, 2) != '':
            asm.write(sheet1.cell_value(i, 2) + '\n')
        if sheet1.cell_value(i, 3) != '':
            bn.write(sheet1.cell_value(i, 3) + '\n')
        if sheet1.cell_value(i, 4) != '':
            pn.write(sheet1.cell_value(i, 4) + '\n')
        if sheet1.cell_value(i, 5) != '':
            gu.write(sheet1.cell_value(i, 5) + '\n')
        if sheet1.cell_value(i, 6) != '':
            od.write(sheet1.cell_value(i, 6) + '\n')
        if sheet1.cell_value(i, 7) != '':
            tm.write(sheet1.cell_value(i, 7) + '\n')
        if sheet1.cell_value(i, 8) != '':
            tl.write(sheet1.cell_value(i, 8) + '\n')
        if sheet1.cell_value(i, 9) != '':
            kn.write(sheet1.cell_value(i, 9) + '\n')
        if sheet1.cell_value(i, 10) != '':
            ml.write(sheet1.cell_value(i, 10) + '\n')

