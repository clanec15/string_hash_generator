import hashlib
print('          String Hash generator          ')
from data import string
import time

a = '1'
b = '2'
c = '3'
d = '4'
e = '5'
f = '6'
g = '7'
h = '8'
print('___________________')
print('|1 = MD5 mode     |')
print('|2 = SHA256 mode  |')
print('|3 = SHA1 mode    |')
print('|4 = SHA224 mode  |')
print('|5 = SHA384 mode  |')
print('|6 = SHA512 mode  |')
print('|7 = Blake2b mode |')
print('|8 = Blake2s mode |')
print('-------------------')
m = input('What mode do you want?\n')
print('')


if m == a:
    h = hashlib.md5()
elif m == b:
    h = hashlib.sha256()
elif m == c:
    h = hashlib.sha1()
elif m == d:
    h = hashlib.sha224()
elif m == e:
    h = hashlib.sha384()
elif m == f:
    h = hashlib.sha512()
elif m == g:
    h = hashlib.blake2b()
elif m == h:
    h = hashlib.blake2s()
x = 'y'
y = 'n'

h.update(string.encode('utf-8'))
s = input('Want to save it to a file?\n')
if s == x:
    print('Saving...')
    time.sleep(3)
    f = open("Str_to_hash.txt", "x")
    f = open("Str_to_hash.txt", "w")
    f.write("This is the hash that was created... ")
    f.write(h.hexdigest())
    f.close()

elif s == y:
    print('This is the hash that you were looking for...')
    print(h.hexdigest())
       
print('')
print("Nothing more to do here, Quitting...")
time.sleep(5)
