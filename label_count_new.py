file=open('class_def.txt','r',encoding='utf-8')
op_file=open('label_count_op.txt','w')
d = {}
for each_line in file:
    word = each_line.split()
    word[0] = word[0].strip('{}')
    if word[0] not in d.keys():
        d[word[0]] = 1
    else:
        d[word[0]] = d[word[0]] + 1
file.seek(0,0)
for each_line in file:
    word = each_line.split()
    s=word[0]
    word[0] = word[0].strip('{}')
    if word[0]=='APP':
        op_file.write(s+' '+str( 1/d['APP'])+' '+' '.join(word[1:]))
        op_file.write('\n')
    elif word[0]=='ARTISTS':
        op_file.write(s+' '+str( 1/d['ARTISTS']) + ' ' + ' '.join(word[1:]))
        op_file.write('\n')
    else:
        op_file.write(s +' '+str( 1/d['MOVIE'])+' ' + ' '.join(word[1:]))
        op_file.write('\n')
file.close()
op_file.close()
