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


