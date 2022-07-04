import time
import network

STATUSCODES = {network.STAT_IDLE: 'no connection and no activity',
               network.STAT_CONNECTING: 'connecting in progress',
               network.STAT_WRONG_PASSWORD: 'failed due to incorrect password',
               network.STAT_NO_AP_FOUND: 'failed because no access point replied',
               network.STAT_CONNECT_FAIL: 'failed due to other problems',
               network.STAT_GOT_IP: 'connection successful'}

def printStatusCodes():
    for code in STATUSCODES.keys():
        printStatusCode(code)

def printStatusCode(code):
    print('#[{:>2}] {}'.format(code, STATUSCODES[code]))

def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        print('Last connection is still active, disconnecting...')
        wlan.disconnect()

    wlan.connect(ssid, password)

    # Wait for connect or fail
    max_wait = 10
    print('Trying connect ' + ssid + '...')
    while max_wait > 0:
        if wlan.status() == network.STAT_GOT_IP:
            break
        max_wait -= 1
        time.sleep(1)

    printStatusCode(wlan.status())

    return wlan

