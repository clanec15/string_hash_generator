import hashlib
import time

print('¡WARNING! - if you have an outdated version of hashlib, blake modes will not work , so beware!')
#This was before in data.py but i finally integrated both... yay
input('Press enter to continue\n')
print('          String Hash generator          ')
global string
string = input("Enter the string you want the hash generated\n")
print('Do you want to add a salt? y/n')
k = input("")
if k == ("y"):
   q = input('Enter salt...\n')
   print("The string you entered was " +string)
   print("With the salt " +q)
   string = (string) + (q)
   
else:
    print("The string you entered was " +string)
#all variables used in the first lines of code (I could have used a database or a funcion or another file but it seem easier this way
a = '1'
b = '2'
c = '3'
d = '4'
e = '5'
f = '6'
g = '7'
h = '8'
i = '9'
j = '10'
k = '11'
l = '12'

#cute and relativly small menu for command prompt
print('_________________________')
print('|1  = MD5 mode          |')
print('|2  = SHA256 mode       |')
print('|3  = SHA1 mode         |')
print('|4  = SHA224 mode       |')
print('|5  = SHA384 mode       |')
print('|6  = SHA512 mode       |')
print('|7  = Blake2b mode      |')
print('|8  = Blake2s mode      |')
print('|9  = SHA3 224 mode     |')
print('|10 = SHA3 256 mode     |')
print('|11 = SHA3 384 mode     |')
print('|12 = SHA3 512 mode     |')
print('-------------------------')
m = input('What mode do you want?\n')
print('')
#all modes in multiple elif statements (Its horrible i know but i lack caffein and donuts)
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
elif m == i:
    h = hashlib.sha3_224()
elif m == j:
    h = hashlib.sha3_256()
elif m == k:
    h = hashlib.sha3_384()
elif m == l:
    h = hashlib.sha3_512()

#Both options of yes and no, i dont know how to make the variable recognice Y, yes, Yes or N and No
x = 'y'
y = 'n'

h.update(string.encode('utf-8'))
s = input('Want to save it to a file?\n')
#saving the hash to a file, for the moment i cant make the program to change the name
if s == x:
    try:
        print('Saving...')
        time.sleep(3)
        f = open("Str_to_hash.txt", "x")
        f = open("Str_to_hash.txt", "w")
        f.write("This is the hash that was created... ")
        f.write("")
        f.write(h.hexdigest())
        f.close()
        print('file saved!')
#Excepcion Handling, the worst way possible (i think)
    except FileExistsError:
        print('')
        print('File already exists please delete or rename the previous text file')
	
               
elif s == y:
    print('This is the hash that you were looking for...')
    print(h.hexdigest())

print('')
#Small nod to KMSpico
print("Nothing more to do here, Quitting...")
time.sleep(10)


