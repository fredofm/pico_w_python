# pico_w_python

At this momment there is no circuitpython support for the new Pico W version, so I made this MicroPython example to test 
the wireless connection on a RaspBerry Pico W.

## Secrets

I'm using ujson library to get my secrets from a json file. To get this example working place 
a *secrets.json* file at the root directory with the following structure:

```json
{
	"wifi": {
		"ssid": "YOUR SSID",
		"pass": "YOUR PASSWORD"
	}
}
```

## Run

I'm running this program on a Raspeberry Pico W using Thonny.

If everything goes fine you should get the following shell output:

```text
#[ 0] no connection and no activity
#[ 1] connecting in progress
#[-3] failed due to incorrect password
#[-2] failed because no access point replied
#[-1] failed due to other problems
#[ 3] connection successful
Last connection is still active, disconnecting...
Trying connect Xana...
#[ 3] connection successful
IP = 192.168.123.124
{'milliseconds_since_epoch': 1656961317486, 'date': '07-04-2022', 'time': '07:01:57 PM'}
```


