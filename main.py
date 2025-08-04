
import time
from pi_pico_neopixel_tools.color import Color
from pi_pico_neopixel_tools.led_strip import LedStrip


led_strip = LedStrip(20,10)



if __name__ == "__main__":
    led_strip.fill(Color.orange())
    led_strip.brightness(0)

    while 1 < 2:
        for i in range(255):
            print(i)
            led_strip.brightness(i)
            led_strip.fill(Color.orange())
            time.sleep(0.3)
        
        for i in range(255, 0, -1):
            led_strip.brightness(i)
            led_strip.fill(Color.orange())
            time.sleep(0.3)