import pyfirmata

comport='Arduino Uno'

board=pyfirmata.Arduino(comport)


led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')

def led(fingerUp):
    if fingerUp==[0,0,0,0,0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)

    elif fingerUp==[0,1,0,0,0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
    elif fingerUp==[0,1,1,0,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)   
    elif fingerUp==[1,1,1,0,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
    elif fingerUp==[1,0,0,0,0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)   
    elif fingerUp==[0,0,1,0,0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
    elif fingerUp==[1,0,1,0,0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(1)
    elif fingerUp==[1,1,0,0,0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(1)