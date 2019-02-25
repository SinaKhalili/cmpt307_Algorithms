import random
import time

def divide(x, y):
    a = x/y
    b = x % y
    return (a,b)

def bezout(a, b):
    if b == 0:
        return 1, 0, a
    else:
        q, r = divide(a, b)
        x, y, g = bezout(b, r)
        return y, x - q * y, g

def generateprime(length ):
    num = random.randint(1,9)
    for i in range(length):
        num = num*10 + random.randint(0,9)

    if( pow(2,num-1,num) == 1 and
            pow(3,num-1,num) == 1 and
            pow(5,num-1,num) == 1):
        return num
    else:
        return generateprime(length)

def generateRSA(len = 300, e = 65537, p = 0, q = 0, message = 42):
    #This generates a private-key public-key
    #Notes: p and q aren't checked so up to the user
    #WARN: the message isn't padded, it assumes the user padded & encoded
    a = len
    print("your p is : ")
    if(p == 0):
        p = generateprime(a)
    print(p)
    print("your q is : ")
    if(q == 0):
        q = generateprime(a)
    print(q)
    print("your n is : ")
    n = p*q
    print(n)
    print("your phi(n) is : ")
    phi = (p-1)*(q-1)
    print(phi)
    if (phi % e == 0):
        print("Bad e choice. Using 65537.")
        e = 65537
    print("Generating decryption key as modular inverse of encryption key...")
    d, _, _ = bezout(e, phi)
    print("Your decryption key is: ")
    print(d)
    if(d < 0):
        print("Since it is negative, we will add until it is not...")
        i = 0
        while(d < 0):
            d = d + phi 
        print("Your new non-negative encryption key is:")
        print(d)
    print("Here is your public key:")
    print(" e = " + str(e) + " , n = " + str(n) )
    print("Send it to your friends and family and tell them to raise their message to e mod n")
    print("Encrypting your message")    
    c = pow(message,e, n)
    print(" It is : ")
    print(c)
    message = pow(c,d, n)
    print("It is : ")
    print(message)


if __name__ == '__main__':
    #This main function generates a private-key public-key
    #Alternatively could use the generate 
    print("enter len of desired keys. Apparently 2048 bits ~ 616 digits is the norm")
    a = input()
    print("your p is : ")
    p = generateprime(a)
    print(p)
    print("your q is : ")
    q = generateprime(a)
    print(q)
    print("your n is : ")
    n = p*q
    print(n)
    print("your phi(n) is : ")
    phi = (p-1)*(q-1)
    print(phi)
    print("what is your desired encryption key e, standard is  65537 ")
    e = input()
    if (phi % e == 0):
        print("bad choice. Using 65537.")
        e = 65537
    print("Generating decryption key as modular inverse of encryption key...")
    d, _, _ = bezout(e, phi)
    print("Your decryption key is: ")
    print(d)
    if(d < 0):
        print("Since it is negative, we will add until it is not...")
        i = 0
        while(d < 0):
            d = d + phi 
        print("Your new non-negative encryption key is:")
        print(d)
    print("Here is your public key:")
    print(" e = " + str(e) + " , n = " + str(n) )
    print("Send it to your friends and family and tell them to raise their message to e mod n")
    print("Taking e*d mod phi gives us " + str((e*d) % phi))
    print(" what would you like to encrypt?")
    m = input()
    c = pow(m,e, n)
    print(" It is : ")
    print(c)
    print("I will now decrypt it")
    message = pow(c,d, n)
    print("It is : ")
    print(message)
    print("Ta-da!")


    
    
