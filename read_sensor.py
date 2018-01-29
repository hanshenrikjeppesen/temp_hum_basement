from time import sleep
import pigpio

pi = pigpio.pi()

import DHT22

s = DHT22.sensor(pi, 4)

temp = 0
hum = 0

'''
for i in range(10):
    sleep(2)
    s.trigger()
    temp = temp + int(s.temperature())

temp = temp/10
print('avag temp is=: ' + str(temp))
'''
s.trigger()
print('Temperature is {:3.2f}'.format(s.temperature() / 1.))
print('Humidity is {:3.2f}'.format(s.humidity() / 1.))

      
