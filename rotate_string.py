def rotate(st1, st2):
    rot_list = []
    l = st1.split()
    list3 = []
    for i in range(1, len(l) + 1):
        rot_list = l[i:] + l[:i]
        rot_string = " ".join(rot_list)
        list3.append(rot_string)

    if st2 in list3:
        print("true")
    else:
        print("false")
s1='veena'
s2='neva'
check_anagramrotate(s1,s2)