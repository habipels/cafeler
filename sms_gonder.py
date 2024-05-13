"""import requests

# your API secret from (Tools -> API Keys) page
apiSecret = "4ee24d34fb8b11570960cb26a87294836e0d8aaf"
deviceId = "00000000-0000-0000-b9d5-82b97010db9b"
phone_list = ['+905395154570']

message = 'Test '
for i in phone_list:
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
import requests

# your API secret from (Tools -> API Keys) page
apiSecret = "4ee24d34fb8b11570960cb26a87294836e0d8aaf"
deviceId = "00000000-0000-0000-b9d5-82b97010db9b"
phone_list = ['905494160542']

message = 'Test '
for i in range(0,10):
    message = {
        "secret": apiSecret,
    "account": "17154397125943a6c821a417791dffc82b4b6268a8663f8860b2340",
    "recipient": phone_list[0],
    "type": "text",
    "message": "Bu mesaj test Ve yazılım tarafından gönderiliyor"
    }

    r = requests.post(url = "https://www.cloud.smschef.com/api/send/whatsapp", params = message)
    
    # do something with response object
    result = r.json()

    print(result)