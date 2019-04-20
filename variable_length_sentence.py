string=input('enter the sentence:')
words=string.split(' ')
len_string=len(words)

l = 1
for k in range(len_string, 0, -1):
    for i, j in zip(range(0, l + 1), range(k-2,len_string, 1)):
        print(' '.join(words[i:j + 1]))
    l=l+1

