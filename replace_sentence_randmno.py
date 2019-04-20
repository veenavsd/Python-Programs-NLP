import xlrd
import xlwt
import random

wb=xlrd.open_workbook('Calculator_UseCases .xlsx')
wb_new=xlwt.Workbook()
for sno in range(wb.nsheets):
    sheet1=wb.sheet_by_index(sno)

    sname=wb.sheet_names()
    sheet_new=wb_new.add_sheet(sname[sno],cell_overwrite_ok=True)

    for j in range(1,sheet1.ncols):
        m=1
        sheet_new.write(0, j - 1, sheet1.cell_value(0, j))
        for l in range(10):
            for i in range(1, sheet1.nrows):
                string_new = ''
                if sheet1.cell_value(i,j)!='':
                    s = sheet1.cell_value(i,j).split(' ')

                    for word in s:
                        if word.isdigit():
                            word1 = random.randint(1, 500)
                            string_new = string_new + ' ' + str(word1)
                        else:
                            string_new = string_new + ' ' + word

                    sheet_new.write(m,j-1,string_new)
                    m=m+1
                else:
                    pass

wb_new.save('random_no_replace.xls')