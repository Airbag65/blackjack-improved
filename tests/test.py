from hashlib import md5

print(md5("Hello World!".encode("utf-8")).hexdigest())