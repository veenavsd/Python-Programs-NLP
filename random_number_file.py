import random
f=open('random.txt','w+')
x=random.randint(0,10000)
y=random.randint(0,10000)
f.write("add {} to {}".format(x,y))
f.write('\n')
f.write("what is the sum of {} and {}".format(x,y))