def generate_trigrams(text, n):
    line=text
    words = text.split()
    line_trigrams = []
    for i in range(len(words) - n + 1):
        list1 = words[i:i + n]
        key = ' '.join(list1)
        if key in d.keys():
            d[key] += 1
            line_trigrams.append(0)
        else:
            d[key] = 1
            line_trigrams.append(1)
    if sum(line_trigrams)>=1:
        fop1.write(line)
    if sum(line_trigrams)>=2:
        fop2.write(line)
    if sum(line_trigrams)==3:
        fop3.write(line)


f = open('calc_en.num.txt', 'r')
fop1 = open('calc_one_unique.txt', 'w')
fop2 = open('calc_two_unique.txt', 'w')
fop3 = open('calc_three_unique.txt', 'w')

d = {}
for line in f:
        generate_trigrams(line, 3)
f.close()
fop1.close()
fop2.close()
fop3.close()



