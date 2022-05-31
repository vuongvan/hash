import hashlib
pwrd = bytes(input("Input Password: "), encoding= 'utf-8')
print(hashlib.sha3_512(pwrd).hexdigest())
