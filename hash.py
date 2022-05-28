from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

#Input Data
pwrd = bytes(input("Input Password: "), encoding= 'utf-8')
psalt = bytes(input("Input Salt: "), encoding= 'utf-8')
piters = int(input("Input Iterations: "))

dk = pbkdf2_hmac('sha512', pwrd, psalt*9, piters,128)
print(urlsafe_b64encode(dk).decode("utf-8"))
