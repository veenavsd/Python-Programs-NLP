# write a code to verify whether a string is a valid pan card no or not
# Pan Card No format is 5Alphabets 4Digits 1Alphabet
import re
def validate_pan_number(pan):
    if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan):
        return 'Pan Number is valid'
    else:
        return 'Pan Number is Not Valid'

print(validate_pan_number(input('enter the string:')))