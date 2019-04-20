from datetime import datetime
input_text=input('enter the string:')
day={'first':1,'second':2,'third':3,'fourth':4,'fifth':5,'sixth':6,'seventh':7,'eighth':8,'ninth':9,'tenth':10,'eleventh':11,'twelveth':12,
  'thirteenth':13,'fourteenth':14,'fifteenth':15,'sixteenth':16,'sevteenth':17,'eighteenth':18,'ninteenth':19,'twentieth':20,
   'twenty first':21,'twenty second':22,'twenty third':23,'twenty fourth':24,'twenty fifth':25,'twenty sixth':26,'twenty seventh':27,
   'twenty eighth':28,'twenty ninth':29,'thirtieth':30,'thirty first':31}
Mon={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}

def yeartonum(text):
    l = []
    ones = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
            "nine": 9,"ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
            "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,"hundred":100,'thousand':1000}
    t = text.split()
    for item in t:
        item=item.lower().strip()
        if item in ones.keys():

            l.append(ones[item])


    return(l)


input_text = input_text.lower()
l = []
print(input_text)
for key in Mon.keys():
    if key in input_text:
        month = key
        ind = input_text.index(key)
        p = input_text.partition(key)
        p = list(p)
        d1 = p[0].strip()
        l.append(day[d1])
        l.append(Mon[p[1]])
        s = yeartonum(p[2])
        if int(s[0]) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            t = s[0] * s[1] + s[2]
            l.append(t)
        else:
            len_s = len(s)
            if len_s == 3:
                if s[1] != 100:
                    t = s[0] * 100 + s[1] + s[2]
                    l.append(t)
                else:
                    t = s[0] * 100 + s[2]
                    l.append(t)

            else:
                if s[1] != 100:
                    t = s[0] * 100 + s[1]
                    l.append(t)
                else:
                    t = s[0] * 100
                    l.append(t)

s = map(str, l)
s = "-".join(s)
datetime_object = datetime.strptime(s, '%d-%m-%Y')
print(datetime_object.strftime('%d-%m-%Y'))
