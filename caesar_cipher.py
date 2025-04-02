#caesar cipher
# author = Paavan Shastri
import string
import random
def encrypt(pt,key,all_letters):
    ct=""
    
    for i in pt:
        ct=ct+all_letters[((all_letters.index(i)+key)%len(all_letters))]
    #print(ct)
    return ct

def decrypt(ct,key,all_letters):
    pt=""
    for i in ct:
        res=all_letters.index(i)-key
        #print(res)
        #print(len(all_letters))
        #print(len(all_letters)+res)
        if res<0:
            pt=pt+all_letters[len(all_letters)+res]
        else:
            pt=pt+all_letters[res]
    print(pt)

l1=[]
all_letters=string.ascii_letters+string.punctuation
for i in all_letters:
    l1.append(i)
l1.append(' ')
    #making the list random
random.Random(4).shuffle(l1)

plain_text=input("Enter your messgae: ")
key=int(input("Enter key: "))
print(l1)
#print(len(l1))
#print(shu)
print("Cipher text: ", encrypt(plain_text, key, l1))

#print(ctt)
print("Decrypted text: ")
decrypt(encrypt(plain_text, key, l1), key, l1)