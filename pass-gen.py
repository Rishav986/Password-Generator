import string
import random

# digits, lowercase, upper, symbols

digits = string.digits
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
symbols = string.punctuation

total = digits + lowercase + uppercase + symbols

temp = ''

temp+=random.choice(digits)
temp+=random.choice(lowercase)
temp+=random.choice(uppercase)
temp+=random.choice(symbols)


length = int(input("Enter the length of password: "))

if length <4:
    print("Length must be equal to or greater than 4")
        

else:
    
    for i in range(length-4):
        temp += random.choice(total)
    
    temp = list(temp)
    random.shuffle(temp)    
    
    password = ''
    for i in temp:
        password+=i
    
    print(password)
