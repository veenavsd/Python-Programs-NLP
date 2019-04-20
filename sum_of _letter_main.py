#Find the sum of V+e+e+n+a?:(Substitute a=1..z=26 , A=27..Z=52)
#input='Veena','veena',output=73,47
input_text =input("enter the string:")
sum=0
for char in input_text:
    asc=ord(char)
    if asc in range(97,123):
        pos=ord(char)-97+1
    elif asc in range(65,91):
        pos=ord(char)-65+1+26
    else:
        pos=0
    sum=sum+pos
print(sum)
# ipstring = input('enter the string:')
# sum = 0
# for char in ipstring:
#     val = ord(char)
#     if char.islower():
#         rep_val = val - 97 + 1
#     elif char.isupper():
#         rep_val = val - 65 + 1 + 26
#     else:
#         rep_val = 0
#     sum = sum + rep_val
# print(sum)
