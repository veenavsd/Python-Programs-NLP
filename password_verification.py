def pass_verify(password):
    if password.isalnum() and len(password) >= 8:

        if re.findall(r'\D{3,}', password) or re.findall(r'\d{3,}', password):
            return('Password is valid'+'\n'+'weak')
        else:
            return('Password is valid'+'\n'+'strong')
    else:
        return('Password is not valid!')
import re
password=input('enter a string:')
print(pass_verify(password))