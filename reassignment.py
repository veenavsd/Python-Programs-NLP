main_file=open(r"C:\Users\Reverie-PC\Desktop\Untitled Folder\Untitled Folder\temperature_en.txt","r+",encoding="utf-8")
x_file=open(r"C:\Users\Reverie-PC\Desktop\Untitled Folder\Untitled Folder\places_en.txt","r+",encoding="utf-8")
y1_file=open(r"C:\Users\Reverie-PC\Desktop\Untitled Folder\Untitled Folder\days_en.txt","r+",encoding="utf-8")
y2_file=open(r"C:\Users\Reverie-PC\Desktop\Untitled Folder\Untitled Folder\months_en.txt","r+",encoding="utf-8")
y3_file=open(r"C:\Users\Reverie-PC\Desktop\Untitled Folder\Untitled Folder\dates_en.txt","r+",encoding="utf-8")
z_file=open(r"C:\Users\Reverie-PC\Desktop\Untitled Folder\Untitled Folder\numbers_en.txt","r+",encoding="utf-8")
output=open('outpt_en5.txt','a+',encoding="utf-8")
content_main=main_file.read().split('\n')
content_x=x_file.read().split('\n')
content_y1=y1_file.read().split('\n')
content_y2=y2_file.read().split('\n')
content_y3=y3_file.read().split('\n')
content_z=z_file.read().split('\n')
import re
for line in content_main:
    if line != ' ':
        for places in content_x:
            if places != '':
                line2 = re.sub(r'\bx\b',places, line)
                if 'z' in line:
                    for num in content_z:
                        if num != '':
                            line3 = re.sub(r'\bz\b',num, line2)
                            if line2 != line3:
                                output.write(line3)
                                output.write('\n')
                else:

                    if 'y' in line:
                        for day in content_y1:
                            if day != '':
                                line4 = re.sub(r'\by\b',day, line2)
                                if line2 != line4:
                                    output.write(line4)
                                    output.write('\n')
                        for mon in content_y2:
                            if mon in['JANUARY','MARCH','MAY','JULY','AUGUST','OCTOBER','DECEMBER']:
                                for date in content_y3:
                                    if date != '' :
                                        line5 = re.sub(r'\by\b', date +" " +mon, line2)
                                        if line5 != line2:
                                            output.write(line5)
                                            output.write('\n')
                            elif mon in['APRIL','JUNE' ,'SEPTEMBER','NOVEMBER']:
                                for date in content_y3:
                                    if date == '' or date == 'THIRTY FIRST':
                                        break
                                    else:
                                        line5 = re.sub(r'\by\b', date +" " +mon, line2)
                                        if line5 != line2:
                                            output.write(line5)
                                            output.write('\n')

                            else:
                                if mon!='':
                                    for date in content_y3:
                                        if date == '' or date == 'TWENTY NINTH' or date == 'THIRTY' or date == 'THIRTY FIRST' :
                                            break
                                        else:
                                            line5 = re.sub(r'\by\b', date +" " +mon, line2)
                                            if line5 != line2:
                                                output.write(line5)
                                                output.write('\n')



                    else:
                        output.write(line2)
                        output.write('\n')

