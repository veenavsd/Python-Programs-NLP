from xlrd import open_workbook
import csv
f1=open("output.txt", "w",encoding='utf-16')
f2=open('error.txt','w+')
book = open_workbook(r'C:\Users\Reverie-PC\Desktop\Untitled Folder\w2\Product_List_Test.xlsx', 'r')
sheet = book.sheet_by_index(0)
for i in range(sheet.nrows):
    l1 = sheet.cell_value(i, 0).split()
    l2 = sheet.cell_value(i, 1).split()
    len1 = len(sheet.cell_value(i, 0).split())
    len2 = len(sheet.cell_value(i, 1).split())
    if len1 == len2:
        dict = {k: v for k, v in zip(l1, l2)}
        w = csv.writer(f1)
        for key, val in dict.items():
            w.writerow([key, val])
    else:
        f2.write(str(i))
        f2.write('\n')
f1.close()
f2.close()