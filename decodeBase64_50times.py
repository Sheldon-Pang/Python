import base64

encoded_file = open("/Users/sheldonpang/Downloads/decodeBase64_source.txt", "r")
encoded_data = encoded_file.read()

# Standard Base64 Decoding
for i in range(0,50):
    encoded_data = base64.b64decode(encoded_data)

print(encoded_data)