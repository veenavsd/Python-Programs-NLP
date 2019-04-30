def unique_words(content):
    s=set(content)
    print(s)
    return(s)
def consonants(uw):
    con=[]
    print('consonants: '+'\n')
    for each in uw:
        if  u'\u0d15'<=each[-1]<=u'\u0d39' or u'\u0d7a'<=each[-1]<=u'\u0d7f' or each[-1]==u'\u0d4d'or each[-1]==u'\u0d02':
            con.append(each)
    return con
def vowels(uw):
    vow=[]
    print('vowels:'+'\n')
    for each in uw:
        if  u'\u0d05'<=each[-1]<=u'\u0d14'or each[-1]==u'\u0d60' or each[-1]==u'\u0d61' :
            vow.append(each)
    return vow
def matras(uw):
    mat=[]
    print('matras:'+'\n')
    for each in uw:
        if  u'\u0d3e'<=each[-1]<=u'\u0d4c' or each[-1]==u'\u0d57':
            mat.append(each)
    return mat
f=open('new_small.txt','r',encoding='utf-8')
content=f.read().split()
uw=unique_words(content)
con=consonants(uw)
print(con)
vow=vowels(uw)
print(vow)
matra=matras(uw)
print(matra)
