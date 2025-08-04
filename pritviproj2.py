import random
des=int(input('Enter the lenght of the desired password:'))
var='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890()*&^%$#@!-=+_{}[]|\:;""''<>,.?/`~'
password=''
for i in range(des):
    ran=random.choice(var)
    password+=ran
print('The password of your desired lenght:',password)
    
