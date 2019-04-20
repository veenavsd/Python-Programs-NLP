import xlrd
import xlwt

wb=xlrd.open_workbook('Movie+Palylist.xlsx')
sheet0=wb.sheet_by_index(0)
sheet1=wb.sheet_by_index(1)
sheet2=wb.sheet_by_index(2)
sheet3=wb.sheet_by_index(3)

wb_new=xlwt.Workbook()
sheet_new=wb_new.add_sheet('sheet1',cell_overwrite_ok=True)
wb1_new=xlwt.Workbook()
sheet1_new=wb1_new.add_sheet('sheet1',cell_overwrite_ok=True)
#movies_hindi
j = 0
for i in range(sheet1.nrows):
    string = ''
    es = sheet1.cell_value(i, 0)
    l1 = es.split()
    for item in l1:
        for i in range(sheet0.nrows):
            if item == sheet0.cell_value(i, 0):
                value = sheet0.cell_value(i, 1)

                string = string + ' ' + value
    sheet_new.write(j, 0, es)
    sheet_new.write(j, 1, string)
    j = j + 1
wb_new.save('Reference_movie_original_hindi.xls')

#playlist_hindi
j = 0
for i in range(sheet3.nrows):
    string1 = ''
    es1 = sheet3.cell_value(i, 0)
    l2 = es1.split()
    for item in l2:
        for i in range(sheet2.nrows):
            if item == sheet2.cell_value(i, 0):
                value = sheet2.cell_value(i, 1)

                string1 = string1 + ' ' + value

    sheet1_new.write(j, 0, es1)
    sheet1_new.write(j, 1, string1)
    j = j + 1
wb1_new.save('Reference_playlist_original_hindi.xls')

