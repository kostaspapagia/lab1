import requests  # εισαγωγή της βιβλιοθήκης
import json

url=input("give a valid url:")

r=requests.get(url)

for i,j in r.headers.items():
    print(i,"=", j)

if r.headers.get('Server')!=0:
    print("\n")
    print("Server software:",r.headers.get('Server'))

s=0
if r.cookies!=0:
    print("\n")
    print("Cookies:",r.cookies)
    for k in r.cookies:
        s=s+1
        print("\n")
        print("Cookie number:",s,"Cookie name:", k.name ,"Valid for:", k.expires)







