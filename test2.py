import machine
import dht
import time

meric = machine.Pin(27)
led1 = machine.Pin(2,machine.Pin.OUT)
led2 = machine.Pin(3,machine.Pin.OUT)
led3 = machine.Pin(4,machine.Pin.OUT)
led4 = machine.Pin(5,machine.Pin.OUT)

buttton = machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_UP)

sensor = dht.DHT11(meric)

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)

mereni = 1


while True:
    if buttton.value() == 0:
        if mereni == 1:
            mereni = 2
        else:
            mereni = 1
    
    sensor.measure() 
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    

    if mereni == 1:
            if temp < 20:
                led1.value(1)
                print('Temperature: %3.1f C' %temp)
                print('Temperature: %3.1f F' %temp_f)
                time.sleep(time.sleep(0.5))
                led1.value(0)
            elif temp < 25:
                led2.value(1)
                print('Temperature: %3.1f C' %temp)
                print('Temperature: %3.1f F' %temp_f)
                time.sleep(0.5)
                led2.value(0)
            elif temp < 27:
                led3.value(1)
                print('Temperature: %3.1f C' %temp)
                print('Temperature: %3.1f F' %temp_f)
                time.sleep(0.5)
                led3.value(0)
            elif temp < 30:
                led4.value(1)
                print('Temperature: %3.1f C' %temp)
                print('Temperature: %3.1f F' %temp_f)
                time.sleep(0.5)
                led4.value(0)


    if mereni == 2:
            if hum < 25:
                led1.value(1)
                print('Humidity: %3.1f %%' %hum)
                time.sleep(0.5)
                led1.value(0)
            elif hum < 50:
                led2.value(1)
                print('Humidity: %3.1f %%' %hum)
                time.sleep(0.5)
                led2.value(0)
            elif hum < 75:
                led3.value(1)
                print('Humidity: %3.1f %%' %hum)
                time.sleep(0.5)
                led3.value(0)
            elif hum < 100:
                led4.value(1)
                print('Humidity: %3.1f %%' %hum)
                time.sleep(0.5)
                led4.value(0)