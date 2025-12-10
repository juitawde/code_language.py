import random
import string

st = input("Enter message: ")
words = st.split(" ")
coding = input("coding or decoding: ")
coding = True if (coding == "coding") else False

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = generate_random_string(3)  
            r2 = generate_random_string(3)  
            r3 = generate_random_string(3)  
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))