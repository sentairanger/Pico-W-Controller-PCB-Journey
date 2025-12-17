from time import sleep
from picozero import Button

# Change button pin to 14, 15 or 2 to test as well
button = Button(0)

while True:
    if button.is_pressed:
        print("pressed")
    else:
        print("not pressed")
    sleep(0.1)
