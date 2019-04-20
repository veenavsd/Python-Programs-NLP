import random,string
f=open('state_codes.txt','r')
f1=open('driving_license.txt','w')
f2=open('vehicle_plate_no.txt','w')
d={}
for line in f:
    word=line.split()
    d[' '.join(word[:len(word)-1])]=word[-1]
for i in range(1000):
    for key,value in d.items():
        x1 = value+''.join(random.choice(string.digits) for _ in range(2))+str(random.randint(1900,2019))+''.join(random.choice(string.digits) for _ in range(9))
        f1.write(x1)
        f1.write('\n')
for i in range(1000):
    for key,value in d.items():
        x1 = value+" "+''.join(random.choice(string.digits) for _ in range(2))+" "+''.join(random.choice(string.ascii_uppercase) for _ in range(2))+" "+''.join(random.choice(string.digits) for _ in range(4))
        f2.write(x1)
        f2.write('\n')
f.close()
f1.close()
f2.close()
