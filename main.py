import wifi
import ujson
import urequests

def readSecrets():
    with open('secrets.json') as fp:
        secrets = ujson.loads(fp.read())
        return secrets

secrets = readSecrets()

wifi.printStatusCodes()
wlan = wifi.connect(secrets['wifi']['ssid'], secrets['wifi']['pass'])

if wlan.isconnected():
    status = wlan.ifconfig()
    print('IP = ' + status[0])

    # Make GET request
    r = urequests.get("http://date.jsontest.com")
    print(r.json())
    r.close()