import time

password = input('Enter the password: ')
start = time.time()
chars = 'abcdefghijklmnopqrstuvwxyz'
guess =  [ ]
for val in range(5):
    a =  [i for i in chars]
    for y in range(val):
        a =  [x+i for i in chars for x in a]
    guess = guess+a 
    if password in guess:
        break
end = time.time()
clock = str(end-start)

print('Password is: '+password)
print('time taken: ' + clock)