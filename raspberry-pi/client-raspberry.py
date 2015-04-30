# -*- coding: utf-8 -*-
import requests

domain = "localhost:5000"

kind = "nfc"
tag = "xxxxx" #Dato recibido al leer tag NFC

url = "http://"+domain+"/api/1/device/"+kind+"/"+tag+"/check"
r = requests.get(url)


print url
print(r.json())
print("----------------")


parsed_json = r.json()
message = parsed_json['message']
result = parsed_json['result']

print(message)

if result:
    print "Activar Relé"
else:
    print "NO Activar Relé"



