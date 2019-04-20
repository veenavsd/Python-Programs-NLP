#input = "Sprite 200ML",hello 2 2.5ml
#output = "Sprite 200 ML"
import re
string=input("enter the string")
output=[]
words=string.split()
for item in words:
    if item.isalpha():
        output.append(item)
    elif item.isdigit():

        output.append(item)
    else:
        item = " ".join(re.findall(r'[A-Za-z]+|\d*\.?\d*',item)).strip()

        output.append(item)
output = " ".join(output)
print(output)


