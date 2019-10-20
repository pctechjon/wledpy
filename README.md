# wledpy
Python Library to interface with [WLED](https://github.com/Aircoookie/WLED) JSON API

# installation

Installation: `pip install wledpy-pctechjon`

# usage

The "Hello World" of LED strips:

```
import wledpy.wled as wled

led_strip = wled.Wled("192.168.1.50")
led_strip.turn_on()
```

