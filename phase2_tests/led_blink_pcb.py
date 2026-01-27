from picozero import Button, LED
from time import sleep

button = Button(0)
led = LED(3)

while True:
    if button.is_pressed:
        print("on")
        led.on()
    else:
        print("off")
        led.off()
    sleep(0.1)