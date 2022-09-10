import time
import machine
import network
#import rp2

STATUSCODES = {network.STAT_IDLE: 'no connection and no activity',
               network.STAT_CONNECTING: 'connecting in progress',
               network.STAT_WRONG_PASSWORD: 'failed due to incorrect password',
               network.STAT_NO_AP_FOUND: 'failed because no access point replied',
               network.STAT_CONNECT_FAIL: 'failed due to other problems',
               network.STAT_GOT_IP: 'connection successful'}

#rp2.country('ES')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# power mode on (deactivate powersaving mode)
wlan.config(pm = 0xa11140)

def printStatusCodes():
    for code in STATUSCODES.keys():
        printStatusCode(code)

def printStatusCode(code):
    print('#[{:>2}] {}'.format(code, STATUSCODES[code]))

def connect(ssid, password):    
    if not wlan.isconnected():
        print('Not Wifi connection available. Trying to connect ' + ssid)
        wlan.ifconfig(('192.168.123.116', '255.255.255.0', '192.168.123.76', '192.168.123.76'))
        wlan.connect(ssid, password)

        # Wait for connect or fail
        max_wait = 10        
        while max_wait > 0:
            if wlan.status() == network.STAT_GOT_IP:
                break
            max_wait -= 1
            time.sleep(1)

        printStatusCode(wlan.status())
    else:
        print('Last connection is still available') 

