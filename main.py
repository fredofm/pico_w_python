import wifi
import ujson
import urequests
import machine
import _thread
import utime
import sys
import time
import gc

LED = machine.Pin("LED", machine.Pin.OUT)
RELAY = machine.Pin(15, machine.Pin.OUT)

def init():
    gc.enable()
    LED.off()
    RELAY.value(0)

def readSecrets():
    print("reading Wifi secrets")    
    
    with open('secrets.json') as fp:
        secrets = ujson.loads(fp.read())
        return secrets


def wifiConnect():
    print("Tryin to create Wifi connection")    
        
    if not wifi.wlan.isconnected():                    
        # wifi.printStatusCodes()
        
        try:            
            secrets = readSecrets()
            wifi.connect(secrets['wifi']['ssid'], secrets['wifi']['pass'])            
        except Exception as e:            
            print("Exception when trying to connect " + secrets['wifi']['ssid'])
            print(repr(e))
            sys.print_exception(e)

        if wifi.wlan.isconnected():
            LED.on()
            status = wifi.wlan.ifconfig()
            print('wifi_management IP = ' + status[0])          
        else:
            LED.off()
    else:        
        LED.on()
        

def activateProp():
    print("Activating Prop")
    RELAY.value(1)    
    time.sleep(60)
    deactivateProp()
    
def deactivateProp():
    print("De-activating Prop")    
    RELAY.value(0)        

def showLEDError():
    print("Show error")
    
    LED.toggle()
    time.sleep(0.15)
    LED.toggle()
    time.sleep(0.15)
    LED.toggle()
    time.sleep(0.15)
    LED.toggle()
    time.sleep(0.15)
    LED.toggle()
    time.sleep(0.15)
    LED.toggle()
    time.sleep(0.15)
    LED.toggle()
    time.sleep(0.15)
    LED.toggle()

def getPropRemoteStatus():
    activatePropStatus = False
    propId = 2
    urlBase = "http://192.168.123.60:8080/api/v1/props/"
    url = urlBase + str(propId)
        
    try:
        # Make GET request
        print("Making GET request: {0}".format(url))
        res = urequests.get(url)
        print(res.json()['running'])
        activatePropStatus = res.json()['running']
    except Exception as e:
        print("Exception occurs when GET " + url)
        print(repr(e))
        sys.print_exception(e)
        showLEDError()
    finally:
        try:
            res.close()
        except:
            print("Skipping response closing")

    gc.collect()  
    
    return activatePropStatus

init()
wifiConnect()

#_thread.start_new_thread(threadExecution, ())

last_time1 = time.time()  # holds when we did something #1
remotePropStatus = False

while True:
    
    if not wifi.wlan.isconnected():
        wifiConnect()
    
    if (time.time() - last_time1 > 20):
        remotePropStatus = getPropRemoteStatus()    
    
    print("remotePropStatus: " + str(remotePropStatus) + " Wifi isConnected():" + str(wifi.wlan.isconnected()))
    
    if remotePropStatus or (time.time() - last_time1 > 120.0):  # every 2 seconds        
        remotePropStatus = False
        activateProp()
        last_time1 = time.time() # save when we do the thing
        
        
    utime.sleep(0.5) 
 
