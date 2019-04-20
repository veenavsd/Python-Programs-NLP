from operator import itemgetter
import re
file=open('new_small.txt','r',encoding='utf-8')
def replacefn(text):
    text=text.lower()
    
    spec_char=[',','/',':',';','”','“','’','{','}','[',']','(',')','~','!','\'','@','#','$','%','^','&','*','+','--','"','----','//','?','>','<']
    for char in spec_char:
        if char in text:

            text=text.replace(char,' ')
    return text
content=file.read()
content1=replacefn(content)
words=content1.split(' ')
d={}
for each_word in words:
    if each_word:
        w1=each_word.strip()
        if w1 not in d.keys():
            d[w1]=1
        else:
            d[w1]+=1

for k, v in sorted(d.items(), key=itemgetter(1)):
    with open('word_count.txt','a',encoding='utf-8') as f:
        f.write(k+':'+str(v))
        f.write('\n')
