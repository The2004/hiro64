import base64
import math
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789="
to = chars
def hash(plaintext):
    hashed = 1;
    btext = base64.b64encode(plaintext.encode("utf-8")).decode("utf-8").replace("=","")
    for char in btext:
        hashed += 2 * (chars.rfind(str(char)) + 1) - (chars.rfind(str(char)) + 1) * 0.25
    return int(hashed)

def encrypt(plaintext, key):
    global to
    btext = base64.b64encode(plaintext.encode("utf-8")).decode("utf-8") 
    encodedkey = base64.b64encode(key.encode("utf-8")).decode("utf-8") 
    for i in range(len(to)):
        chosen = to[customrandom(0, len(to), hash(encodedkey[customrandom(0, len(encodedkey), i)]))]
        to = to.replace(chosen, "")
        to = chosen + to
    cip = ''
    for ch in btext:
        cip += to[chars.rfind(ch)]
    print(to)
    to = chars
    
    return cip

def decrypt(ciphertext, key):
    global to
    btext = ciphertext
    encodedkey = base64.b64encode(key.encode("utf-8")).decode("utf-8") 
    for i in range(len(to)):
        chosen = to[customrandom(0, len(to), hash(encodedkey[customrandom(0, len(encodedkey), i)]))]
        to = to.replace(chosen, "")
        to = chosen + to
    plaintext = ''
    for ch in btext:
        plaintext += chars[to.rfind(ch)]
    to = chars
    try:
        return base64.b64decode(plaintext.encode("utf-8")).decode("utf-8")
    except:
        raise Exception("failed to decrypt, either key or ciphertext is incorrect")

def customrandom(min, max, seed):
    return int(math.fabs(math.sin((math.tan(seed * 10 + 1 ) * (max * 2 + 1)) * 3)) * (max - min) + min)

