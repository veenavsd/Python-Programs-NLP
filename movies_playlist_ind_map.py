import xlrd
import csv
wb1=xlrd.open_workbook('Reference_movies_original_hindi.xls')
wb2=xlrd.open_workbook('Reference_playlists_original_hindi.xls')
sheet1=wb1.sheet_by_index(0)
sheet2=wb2.sheet_by_index(0)
f1=open("Reference_movie_wordmap_hindi1.csv", "w",encoding='utf-16')
f2=open('error_movies.txt','w+')
f3=open("Reference_playlist_wordmap_hindi1.csv", "w",encoding='utf-16')
f4=open('error_playlist.txt','w+')
for i in range(sheet1.nrows):
    l1=sheet1.cell_value(i, 0).split()
    l2=sheet1.cell_value(i, 1).split()
    len1=len(l1)
    len2=len(l2)
    if len1!=len2:
        f2.write(str(i))
        f2.write('\n')
    else:
        dict={k:v for k,v in zip(l1,l2)}
        w = csv.writer(f1,delimiter='\t')
        for key, val in dict.items():
            w.writerow([key, val])
f1.close()
f2.close()
for i in range(sheet2.nrows):
     l1 = sheet2.cell_value(i, 0).split()
     l2 = sheet2.cell_value(i, 1).split()
     len1 = len(l1)
     len2 = len(l2)
     if len1 != len2:
         f4.write(str(i))
         f4.write('\n')
     else:
         dict = {k: v for k, v in zip(l1, l2)}
         w = csv.writer(f3, delimiter='\t')
         for key, val in dict.items():
             w.writerow([key, val])



f3.close()
f4.close()