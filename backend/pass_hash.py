import hashlib


data="karam"
h=hashlib.new("SHA256")
h.update(data.encode())
y=h.hexdigest()
print(y[0:5])