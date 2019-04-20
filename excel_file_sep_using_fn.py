from xlrd import open_workbook
book = open_workbook(r'Day_&_Month.xlsx', 'r')
sheet = book.sheet_by_index(0)
def f3(n):
    for i in range(n, sheet.nrows):
        if sheet.cell_value(i, j) == '':
            pass
        else:
            fname = sheet.cell_value(0, j)
            with open('{}_month.txt'.format(fname), 'a+', encoding='utf-8') as f2:
                f2.write(sheet.cell_value(i, j))
                f2.write('\n')


for j in range(sheet.ncols):
    for i in range(1,sheet.nrows):
        if sheet.cell_value(i, j)!= '':
            fname = sheet.cell_value(0, j)
            f2 = open('{}_day.txt'.format(fname), 'a+', encoding='utf-8')
            f2.write(sheet.cell_value(i, j))
            f2.write('\n')

        else:
            f3(i)
            break

f2.close()