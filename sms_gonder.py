"""import requests
import random
import datetime
print(datetime.datetime.now())
# your API secret from (Tools -> API Keys) page
apiSecret = "4ee24d34fb8b11570960cb26a87294836e0d8aaf"
deviceId = "00000000-0000-0000-760b-9f944deb7994"
phone_list = ['+9609990001']#400 kadar 
test = ""
for i in range(33600):
    a = str(9609000000 + i)
    test = test +"+"+a+","

print(test,len(test))
message = {
    "secret": apiSecret,
    "mode": "devices",
    "campaign": "",
    "numbers": test,
    "groups": "1,2,3,4",
    "device": "00000000-0000-0000-d57d-f30cb6a89289",
    "sim": 1,
    "priority": 1,
    "message": "Hello World!"
}

r = requests.post(url = "https://www.cloud.smschef.com/api/send/sms.bulk", params = message)
    
    # do something with response object
result = r.json()

print(result)
"""

#delete sms
"""for i in test:
    message = {
    "secret": apiSecret,
    "id": smsId
}

    r = requests.post(url = "https://www.cloud.smschef.com/api/delete/sms.sent", params = message)
    
    # do something with response object
    result = r.json()
    print(result)
"""
"""
message = 'ConnectConnectConnectConnect'
for i in test:
    message = {
        "secret": apiSecret,
        "mode": "devices",
        "device": deviceId,
        "sim": 1,
        "priority": 1,
        "phone": i,
        "message": message
    }

    r = requests.post(url = "https://www.cloud.smschef.com/api/send/sms", params = message)
    
    # do something with response object
    result = r.json()

    print(result)"""
#print(datetime.datetime.now())

import requests
import datetime
# your API secret from (Tools -> API Keys) page
apiSecret = "ee6cfe62b5b603367df4eabea6c5c0312db42b61"
deviceId = "00000000-0000-0000-b9d5-82b97010db9b"
phone_list = ['905494160542']
test = []
for i in range(9607001052,9607999999):
    test.append(i)
a  = datetime.datetime.now()
for i in test:
    message = {
        "secret": apiSecret,
    "account": "1715788432251e16a2aac0ca4847adf561483381bf6644da9013d44",
    "recipient": i,
    "type": "text",
    "message": """🔗 Sign up now: https://ronybet.com/en/aff/gift 
👉 Special offer for new members: Sign up through this link and instantly get 50 FREE SPINS! No additional steps needed, just click, register, and play! 💫
🔗 Sign up now: https://ronybet.com/en/aff/gift"""
    }

    r = requests.post(url = "https://www.cloud.smschef.com/api/send/whatsapp", params = message)
    
    # do something with response object
    result = r.json()

    print(result)
print(a)
print(datetime.datetime.now())
"+9609******"
"+9607******"