import base64
import math
from shutil import ExecError
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
to = chars
def hash(plaintext):
    hashed = 1;
    btext = base64.b64encode(plaintext.encode("ascii")).decode("ascii").replace("=","")
    for char in btext:
        hashed += 2 * (chars.rfind(str(char)) + 1) - (chars.rfind(str(char)) + 1) * 0.25
    return int(hashed)

def encrypt(plaintext, key):
    global to
    if type(key) != int:
        raise Exception("given key must be integer. Use hash() funtion if you want to use strigs as keys")
    btext = base64.b64encode(plaintext.encode("ascii")).decode("ascii")
    for i in range(len(to)):
        chosen = to[customrandom(0, len(to), key + i)]
        to = to.replace(chosen, "")
        to = chosen + to
    cip = ''
    for ch in btext:
        cip += to[chars.rfind(ch)]
    to = chars
    
    return cip

def decrypt(ciphertext, key):
    global to
    if type(key) != int:
        raise Exception("given key must be integer. Use hash() funtion if you want to use strigs as keys")
    btext = ciphertext
    for i in range(len(to)):
        chosen = to[customrandom(0, len(to), key + i)]
        to = to.replace(chosen, "")
        to = chosen + to
    plaintext = ''
    for ch in btext:
        plaintext += chars[to.rfind(ch)]
    to = chars
    try:
        return base64.b64decode(plaintext.encode("ascii")).decode("ascii")[:-1]
    except:
        raise Exception("failed to decrypt, either key or ciphertext is incorrect")

def customrandom(min, max, seed):
    return int(math.fabs(math.sin(seed)) * (max - min) + min)
