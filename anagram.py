def check_anagram(st1, st2):

    l1 = list(st1)
    l2 = list(st2)
    if len(l1)!=len(l2):
        print('Not anagram')
    else:
        s1=l1.sort()
        s2=l2.sort()

        if s1==s2:
            print('anagram')
        else:
            print('not anagram')
s1='veena'
s2='asdfr'
check_anagram(s1,s2)