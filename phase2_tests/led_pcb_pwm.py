from picozero import Pot, PWMLED
from time import sleep

led = PWMLED(3)
pot = Pot(26)

while True:
    led.value = pot.value
    sleep(0.1)