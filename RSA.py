import string, random
from generate_prime import *

def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modular_inverse(a,m):
    # extended euclid algorithm
    g, x, y = iterative_egcd(a, m) 
    if g != 1:
        return None
    else:
        return x % m

def create_keys():
    print("creating primes ....")
    P = generate_prime_number(128)
    Q = generate_prime_number(128)
    N = P * Q
    phi_N = (P - 1) * (Q - 1)
    print("Choosing E.....")
    E, D = 1 , None
    print("Creating Decyption keys......")
    while phi_N%E == 0 or D is None:  
        E = randrange(1,phi_N-1)
        D = modular_inverse(E,phi_N)
    print(D)
    print("Sending them as files ....")    
    with open("decrypt"+str(getrandbits(10))+".txt","w+") as f:
        f.write(",".join([str(D),str(N)]))
    with open("encrypt"+str(getrandbits(10))+".txt","w+") as f:
        f.write(",".join([str(E),str(N)]))
    return (E,N) 

def parse_input(file_name):
    with open(file_name) as f:
        return [int(x) for x in f.read().split(",")]

def encrypt_chunk(chunk,E,N):
    content = int("".join([str(ord(c)) for c in chunk]))
    return pow(content,E,N)

def add_stopage(chunk):
    return "".join([c + 2 * chr(0) for c in str(chunk)])

def stringify_chunk(chunk):
    return "".join([chr(int(n)+ord('a')) for n in str(chunk)])

def destringify_chunk(chunk):
    return "".join([str(ord(x) - 97) for x in chunk])

def encrypt(content,pub_key = None):
    E, N =None ,None
    if pub_key is None:
        print("Howdy, you have not entered the public key")
        s = input("Do you want to generate new keys Y/N: ").lower()
        if s == "yes" or s == "y":
           E,N = create_keys()
        else:
             print("Are you @ me!!")
             return
    else:
        E,N = parse_input(pub_key)
    new_content = ""
    for i in range(0,len(content),15):
        x = encrypt_chunk(add_stopage(content[i:i+15]),E,N)
        new_content+=stringify_chunk(x)+" "
    return new_content[:-1]

def extract_message(chunk):
    z = []
    content = ""
    for i in range(2,len(chunk)):
        if chunk[i]!='0' and chunk[i-1] == '0' and chunk[i-2] == '0':  z += [i-2,i-1]
    i = 0
    z.insert(0,-1)
    while i+1 < len(z):
        content+=chr(int(chunk[z[i]+1 : z[i+1]]))
        i+=2     
    content+=chr(int(chunk[z[i]+1 : -2]))
    return content

def decrypt(content,priv_key=None):
    if priv_key is None: 
        print("Are you @ me!!")
        return
    D,N = parse_input(priv_key)
    new_content = ""
    for chunk in content.split(" "):
        c = destringify_chunk(chunk)
        x = pow(int(c),D,N)
        new_content+=extract_message(str(x))
    return new_content

# print(decrypt(encrypt("hello world I study at BMSCE and I like programming!!!","encrypt13.txt"),"decrypt663.txt"))
# print(decrypt("jgcafhihciahhihcagefbgihdcagfdaifigajhcjbfahdfjfifiibgaeedceeffcagacaibjghii","decrypt663.txt"))