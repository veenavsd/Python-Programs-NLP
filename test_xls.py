import xlrd
import xlwt
wb_ip=xlrd.open_workbook('Product.xlsx')
ip_sheet=wb_ip.sheet_by_index(0)
wb_new=xlwt.Workbook()
sheet_new=wb_new.add_sheet('sheet1')
m=0
n=0
for i in range(ip_sheet.nrows):
    l1 = ip_sheet.cell_value(i, 0).split()
    l2 = ip_sheet.cell_value(i, 1).split()
    if len(l1) == len(l2):
        for k, v in zip(l1, l2):
            sheet_new.write(m, 0, k)
            sheet_new.write(n, 1, v)
            m = m + 1
            n = n + 1
wb_new.save('product_map.xls')
