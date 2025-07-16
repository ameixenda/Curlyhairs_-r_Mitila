radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    if (receivedNumber == 1) {
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        neZha.setMotorSpeed(neZha.MotorList.M1, 100)
    } else if (receivedNumber == 2) {
        direccion = 1
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 100)
        basic.pause(500)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        direccion = 0
    } else if (receivedNumber == 3) {
        direccion = 2
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 250)
        basic.pause(500)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        direccion = 0
    } else if (receivedNumber == 4) {
        neZha.setMotorSpeed(neZha.MotorList.M1, -80)
    } else if (receivedNumber == 5) {
        neZha.stopAllMotor()
    }
    
})
buttonClicks.onButtonDoubleClicked(buttonClicks.AorB.A, function my_function() {
    basic.showLeds(`
        . . . . .
        . # . # #
        # # . # #
        . . . # .
        . . . . .
        `)
    basic.pause(1000)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendNumber(2)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    radio.sendNumber(5)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(3)
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    basic.showIcon(IconNames.Heart)
    basic.pause(2000)
})
input.onGesture(Gesture.LogoDown, function on_gesture_logo_down() {
    radio.sendNumber(4)
})
let direccion = 0
direccion = 0
neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
neZha.setMotorSpeed(neZha.MotorList.M1, 0)
radio.setGroup(1)
basic.forever(function on_forever() {
    if (direccion == 1) {
        basic.showLeds(`
            . . # . .
            . . # # .
            # # # # #
            . . # # .
            . . # . .
            `)
        basic.pause(1000)
    }
    
})
basic.forever(function on_forever2() {
    if (direccion == 2) {
        basic.showLeds(`
            . . # . .
            . # # . .
            # # # # #
            . # # . .
            . . # . .
            `)
        basic.pause(1000)
    }
    
})
basic.forever(function on_forever3() {
    if (input.temperature() > 30) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    
})
