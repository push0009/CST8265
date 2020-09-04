import hashlib

filename = 'D:\WebDev\Web Security Basics\Lab11\Lab-11_package\MD5\MD5.java'
hasher = hashlib.md5()
with open(filename,'rb') as open_file:
    content = open_file.read()
    hasher.update(content)
print(hasher.hexdigest())