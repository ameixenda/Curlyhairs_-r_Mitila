def on_received_number(receivedNumber):
    global direccion
    if receivedNumber == 1:
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        neZha.set_motor_speed(neZha.MotorList.M1, 100)
    elif receivedNumber == 2:
        direccion = 1
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 100)
        basic.pause(500)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        direccion = 0
    elif receivedNumber == 3:
        direccion = 2
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 250)
        basic.pause(500)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        direccion = 0
    elif receivedNumber == 4:
        neZha.set_motor_speed(neZha.MotorList.M1, -80)
    elif receivedNumber == 5:
        neZha.stop_all_motor()
radio.on_received_number(on_received_number)

def my_function():
    basic.show_leds("""
        . . . . .
        . # . # #
        # # . # #
        . . . # .
        . . . . .
        """)
    basic.pause(1000)
buttonClicks.on_button_double_clicked(buttonClicks.AorB.A, my_function)

def on_button_pressed_a():
    radio.send_number(2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    radio.send_number(5)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    radio.send_number(1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(3)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    basic.show_icon(IconNames.HEART)
    basic.pause(2000)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_gesture_logo_down():
    radio.send_number(4)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

direccion = 0
direccion = 0
neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
neZha.set_motor_speed(neZha.MotorList.M1, 0)
radio.set_group(1)

def on_forever():
    if direccion == 1:
        basic.show_leds("""
            . . # . .
            . . # # .
            # # # # #
            . . # # .
            . . # . .
            """)
        basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    if direccion == 2:
        basic.show_leds("""
            . . # . .
            . # # . .
            # # # # #
            . # # . .
            . . # . .
            """)
        basic.pause(1000)
basic.forever(on_forever2)

def on_forever3():
    if input.temperature() > 30:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
    else:
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever3)
