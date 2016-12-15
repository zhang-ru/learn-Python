import base64
def to_base_64(string):
    #your code here
    a = base64.b64encode(string.encode()).decode()
    return a.replace("=","")
def from_base_64(string):
    #your code herepass
    mspadding = 4-len(string)%4
    if mspadding:
    	string = string+"="*mspadding
    return base64.b64decode(string).decode()
# answer
from base64 import b64encode, b64decode

def to_base_64(string):
    return b64encode(string).replace("=", '')
    
def from_base_64(string):
    return b64decode(string + "==")

# print(to_base_64('Ja7Baj/Bmvg5EWC3+e2DKnHTc'))
print(from_base_64('IG9pUlhmR2RuMkdoWjc'))