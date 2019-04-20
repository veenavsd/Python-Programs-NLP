import time
start=time.time()
file1=open(r"new_small.txt","r",encoding="utf-8")
file2=open("dictoutput.txt","w+",encoding="utf-8")

#replace puctuations with space
def replacefn(text):
    text=text.lower()
    spec_char=[',','.','/',':',';','”','“','’','{','}','[',']','(',')','~','!','\'','@','#','$','%','^','&','*','+','--','"','----','//','?','>','<']
    for char in spec_char:
        if char in text:
            text=text.replace(char,' ')
    return text
#generate ngrams fn
def generate_ngrams(text, n):
    words = text.split()
    d={}

    for i in range(len(words)-n+1):
        list1=words[i:i+n]
        key=' '.join(list1)   #creating n gram
        #creating unique ngram using dict
        if key in d.keys():
            d[key]+=1
        else:
            d[key]=1
    l1=len(d.keys())
    count.append(l1)
    file2.write('\n')
    for item in d.keys():
        file2.write('\n'+item+'\n')

content=file1.read()
t=replacefn(content)

count=[]    #used to store the count of unique ngram
file2.write('\n unigram starts\n')
generate_ngrams(t,1)
file2.write('unigram ends\n')
file2.write('bigram starts\n')
generate_ngrams(t,2)
file2.write('bigram ends\n')
file2.write('trigram starts\n')
generate_ngrams(t,3)
file2.write('triigram ends\n')
with open("dictoutput.txt","r+",encoding="utf-8") as f:
        content=f.read()
        f.seek(0,0)
        f.write("\nunigram="+str(count[0]))
        f.write("\nbigram="+str(count[1]))
        f.write("\ntrigram="+str(count[2]))
        f.write(content)

file1.close()
file2.close()
f.close()
end=time.time()
print(end-start)