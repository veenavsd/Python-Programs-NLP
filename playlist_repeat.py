inf=open('playlist_test.txt','r',encoding='utf-8')
content=inf.read().split('\n')
d={}
for item in content:
    ind_sent = item.split('\t')
    l1 = ind_sent[0].split(' ')
    l2 = ind_sent[1].split(' ')

    if len(l1) == len(l2):
        for i in range(len(l1)):
            if l1[i] not in d.keys():
                d[l1[i]]={}
                d[l1[i]]['hw']=[]
                d[l1[i]]['hw'].append(l2[i])
                d[l1[i]]['count'] = 1
                with open ('playlist_test_repetition.txt','a+',encoding='utf-8') as out_file:
                    out_file.write(l1[i] + "\t" + l2[i])
                    out_file.write('\n')
            else:
                if l2[i] not in d[l1[i]]['hw']:

                    d[l1[i]]['hw'].append(l2[i])
                    d[l1[i]]['count'] =d[l1[i]]['count']+1
                    with open('playlist_test_repetition.txt', 'a+', encoding='utf-8') as out_file:
                        out_file.write(l1[i] + '[' + str(d[l1[i]]['count']) + ']' + ' ' + l2[i])
                        out_file.write('\n')

                else:
                    break

out_file.close()
inf.close()


