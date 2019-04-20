from xlrd import open_workbook
book = open_workbook(r'C:\Users\Reverie-PC\Desktop\Untitled Folder\Day_&_Month.xlsx', 'r')
sheet = book.sheet_by_index(0)
for j in range(0,12):
    for i in range(1,9):
        fname=sheet.cell_value(0,j)
        f2=open('{}_day.txt'.format(fname),'a+',encoding='utf-8')
        f2.write(sheet.cell_value(i,j))
        f2.write('\n')
f2.close()
for j in range(0,12):
    for i in range(11,23):
        fname=sheet.cell_value(0,j)
        f2=open('{}_month.txt'.format(fname),'a+',encoding='utf-8')
        f2.write(sheet.cell_value(i,j))
        f2.write('\n')
f2.close()