def on_button_pressed_a():
    global entry
    entry = "" + entry + "A"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global entry
    if password == entry:
        basic.show_icon(IconNames.YES)
        pins.servo_write_pin(AnalogPin.P0, 90)
    else:
        basic.show_icon(IconNames.NO)
    basic.pause(500)
    basic.clear_screen()
    entry = ""
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global entry
    entry = "" + entry + "B"
input.on_button_pressed(Button.B, on_button_pressed_b)

entry = ""
password = ""
password = "AABAA"
entry = ""
pins.servo_write_pin(AnalogPin.P0, 0)