import os
import xlwt
import speech_recognition as sr

wb = xlwt.Workbook()
i = 0
sheet = wb.add_sheet('sheet1', cell_overwrite_ok=True)
for file in os.listdir(r'C:\Users\Reverie-PC\Desktop\python_programs\nlp'):

    harvard = sr.AudioFile(r'C:\Users\Reverie-PC\Desktop\python_programs\nlp' + '\\' + file)
    with harvard as source:
        audio = r.record(source)
    try:
        sheet.write(i, 0, file)
        sheet.write(i, 1, r.recognize_google(audio))
    except sr.UnknownValueError:
        sheet.write(i, 0, file)
        sheet.write(i, 1, "NULL AUDIO")
    i = i + 1
wb.save('jio3.xls')ss