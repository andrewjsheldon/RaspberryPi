import sys
import time
import pigpio

pi = pigpio.pi()

# Set RGB Pins
RED   = 17
GREEN = 22
BLUE  = 24

#GREY
pi.set_PWM_dutycycle(RED, 65)
pi.set_PWM_dutycycle(GREEN,65)
pi.set_PWM_dutycycle(BLUE,65)
time.sleep(5)
#BLUE
pi.set_PWM_dutycycle(RED, 25)
pi.set_PWM_dutycycle(GREEN,25)
pi.set_PWM_dutycycle(BLUE, 150)
time.sleep(5)
#GREEN
pi.set_PWM_dutycycle(RED,0)
pi.set_PWM_dutycycle(GREEN,150)
pi.set_PWM_dutycycle(BLUE,0)
time.sleep(5)
#YELLOW
pi.set_PWM_dutycycle(RED, 255)
pi.set_PWM_dutycycle(GREEN,175)
pi.set_PWM_dutycycle(BLUE,0)
time.sleep(5)
#ORANGE
pi.set_PWM_dutycycle(RED, 245)
pi.set_PWM_dutycycle(GREEN,75)
pi.set_PWM_dutycycle(BLUE,0)
time.sleep(5)
#RED
pi.set_PWM_dutycycle(RED, 150)
pi.set_PWM_dutycycle(GREEN,0)
pi.set_PWM_dutycycle(BLUE,0)

pi.stop()
