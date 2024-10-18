import requests

url = 'https://csf101-server-cap1.onrender.com/get/input/361'
txt_file = requests.get(url)

with open('361.txt', 'wb') as file:
    data = file.write(txt_file.content)

print("Downloaded 361.txt")