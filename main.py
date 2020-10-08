import time
import hashlib
#Warning that i dont know if it will be read or not
print('¡WARNING! - if you have an outdated version of hashlib, blake modes will not work , so beware!')
#This was before in data.py but i finally integrated both... yay
input('Press enter to continue\n')
print('          String Hash generator          ')
s = input("Enter the string you want the hash generated:\n> ")
print(f"The string you entered was {s}")
#all variables used in the first lines of code (I could have used a database or a funcion or another file but it seem easier this way
algorithms = {
    "1": hashlib.md5,
    "2": hashlib.sha256,
    "3": hashlib.sha1,
    "4": hashlib.sha224,
    "5": hashlib.sha384,
    "6": hashlib.sha512,
    "7": hashlib.blake2b,
    "8": hashlib.blake2s,
    "9": hashlib.sha3_224,
    "10": hashlib.sha3_256,
    "11": hashlib.sha3_384,
    "12": hashlib.sha3_512
}


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
m = input('What mode do you want?\n> ')

algorithm = algorithms.get(m, False)
if not algorithm:
    print("Please choose 1 to 12 next time. Quitting...")
    exit()

hash = algorithm(s.encode("utf-8")).hexdigest()
print(f'This is the hash that you were looking for...\n{hash}')

if input("Want to save it to a file? Y/n\n> ").lower() in ["yes", "y", ""]:
    try:
        print('Saving...')
        time.sleep(3)
        with open("Str_to_hash.txt", "x") as f:
            f.write(f"This is the hash that was created...\n{hash}")
        print('file saved!')
    #Excepcion Handling, the worst way possible (i think)
    except FileExistsError:
        print('File already exists please delete or rename the previus text file')

#Small nod to KMSpico
input("Nothing more to do here, Quitting...")
time.sleep(10)