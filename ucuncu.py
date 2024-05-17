import requests
import random
import datetime
print(datetime.datetime.now())
apiSecret = "ee6cfe62b5b603367df4eabea6c5c0312db42b61"
deviceId = "00000000-0000-0000-cf0a-35a13eaa8bec"
test = []
c = 0
for i in range(9607967245,9607999999):
    if c == 33600:
        break
    a = "+"+str(i)
    message = """https://Rony.bet/en/aff/gift 
Win at Maldives leading casino site! Sign up, get 50 free spins as a gift  https://Rony.bet/en/aff/gift"""

    message = {
        "secret": apiSecret,
        "mode": "devices",
        "device": deviceId,
        "sim": 1,
        "priority": 1,
        "phone": a,
        "message": message
    }

    r = requests.post(url = "https://www.cloud.smschef.com/api/send/sms", params = message)
    
    # do something with response object
    result = r.json()

    print(c,result,i)
    c = c+1
