f1=open(r'C:\Users\Reverie-PC\Desktop\Untitled Folder\w3\nonascii.eng.txt',"r",encoding='utf-8')
f2=open("asciiop.txt","w+",encoding='utf-8')
f3=open("nonasciiop.txt","w+",encoding='utf-8')
content=f1.read()
content=content.lower().split('\n')


def ascii_lines(text):
    f=0
    for line in text:
        if all((ord(ch) in range(97,123)) or ord(ch)==38 or ord(ch)==32 for ch in line):
            f2.write(line)
            f2.write('\n')
        else:
            f3.write(line)
            f3.write('\n')
ascii_lines(content)
f1.close()
f2.close()
f3.close()


