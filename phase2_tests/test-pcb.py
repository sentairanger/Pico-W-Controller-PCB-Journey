from time import sleep
from picozero import Button

backward_button = Button(0)
forward_button = Button(2)
left_button = Button(15)
right_button = Button(14)

while True:
    if backward_button.is_pressed:
        print("backwards")
    elif forward_button.is_pressed:
        print("forward")
    elif left_button.is_pressed:
        print("left")
    elif right_button.is_pressed:
        print("right")
    else:
        print("not pressed")
    sleep(0.1)