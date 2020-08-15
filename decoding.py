import base64

encoded_file = open("/Users/sheldonpang/Downloads/encodedflag.txt", "r")
encoded_data = encoded_file.read()

# Standard Base16/32/64 Decoding
for i in range(0,5):
    encoded_data = base64.b16decode(encoded_data)

for i in range(0,5):
    encoded_data = base64.b32decode(encoded_data)

for i in range(0,5):
    encoded_data = base64.b64decode(encoded_data)

print(encoded_data)