import base64

dataString = input('Text to encrypt: ')
dataBytes = dataString.encode("utf-8")
encoded = base64.b64encode(dataBytes)

print(encoded) 