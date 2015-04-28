# -*- coding: utf-8 -*-
import httplib2
import json

domain = "localhost:5000"

kind = "nfc"
tag = "x" #Dato recibido al leer tag NFC

url = "http://"+domain+"/api/1/device/"+kind+"/"+tag+"/check"

h = httplib2.Http(".cache")
(resp_headers, content) = h.request(url, "GET")


print url
print(json.dumps(content))
print ("----------------")


parsed_json = json.loads(content)
message = parsed_json['message']
result = parsed_json['result']

print(message)

if result:
    print "Activar Relé"
else:
    print "NO Activar Relé"



