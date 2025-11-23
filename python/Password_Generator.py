
import random

chars = (
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    '0','1','2','3','4','5','6','7','8','9',
    '!', '?', ':', ';', ',', '.', '(', ')', '[', ']', '{', '}', 
    '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', 
    '/', '\\', '|', '~', '<', '>'
)

length = int(input('Insert the length of the password: '))

i = 0
passowrdholder = []
for i in range(length):
    rand = random.randrange(0, 64)
    password = chars[rand]
    passowrdholder.append(password)

print(''.join(passowrdholder)) #added by AI
    

    
