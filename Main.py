from machine import Pin
import utime

led_sw = Pin(26, Pin.OUT)
button_sw = Pin(22, Pin.IN, Pin.PULL_DOWN)
button_1 = Pin(18, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(19, Pin.IN, Pin.PULL_DOWN)
button_3 = Pin(20, Pin.IN, Pin.PULL_DOWN)
button_4 = Pin(21, Pin.IN, Pin.PULL_DOWN)
while True:
    while True:
        led_sw.value(0)
        if button_1.value() == 0:
            print('projetor on/off')
            button_1.value(1)
            utime.sleep_ms(260)
        if button_2.value() == 0:
            print('+ brilho')
            button_2.value(1)
            utime.sleep_ms(260)
        if button_3.value() ==  0:
            print('- brilho')
            button_3.value(1)
            utime.sleep_ms(260)
        if button_4.value() == 0:
            print('enquadramento')
            button_4.value(1)
            utime.sleep_ms(260)
        if button_sw.value() == 0:
            print('\nar condicionado\n')
            button_sw.value(1)
            utime.sleep_ms(260)
            break      
    while True:     
        led_sw.value(1)
        if button_1.value() == 0:
            print('ar on/off')
            button_1.value(1)
            utime.sleep_ms(260)
        if button_2.value() == 0:
            print('+ graus')
            button_2.value(1)
            utime.sleep_ms(260)
        if button_3.value() ==  0:
            print('- graus')
            button_3.value(1)
            utime.sleep_ms(260)
        if button_4.value() == 0:
            print('direção ar')
            button_4.value(1)
            utime.sleep_ms(260)
        if button_sw.value() == 0:
            print('\nprojetor\n')
            button_sw.value(1)
            utime.sleep_ms(260)
            break
