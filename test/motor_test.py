import RPi.GPIO as gpio
import time
# BOARD vs BCM (BroadCom) : 칩 내부 채널번호 , 물리적 위치 차이

gpio.setmode(gpio.BCM)

# motor A 방향
AIN1 = 22 
AIN2 = 27
# motor B 방향
BIN1 = 25
BIN2 = 24

PWMA = 18
PWMB = 23

gpio.setup(AIN1, gpio.OUT)
gpio.setup(AIN2, gpio.OUT)
gpio.setup(BIN1, gpio.OUT)
gpio.setup(BIN2, gpio.OUT)
gpio.setup(PWMA, gpio.OUT)
gpio.setup(PWMB, gpio.OUT)

PWM_FREQUENCY = 1000 # PWM 주파수
PWM_DUTY_CYCLE_MAX = 100 # 최대 속도

pwm_a = gpio.PWM(PWMA, PWM_FREQUENCY)
pwm_b = gpio.PWM(PWMB, PWM_FREQUENCY)

pwm_a.start(0)
pwm_b.start(0)

gpio.output(AIN1, gpio.LOW)
gpio.output(AIN2, gpio.HIGH)
gpio.output(BIN1, gpio.HIGH)
gpio.output(BIN2, gpio.LOW)
pwm_a.ChangeDutyCycle(40)
pwm_b.ChangeDutyCycle(40)

time.sleep(2)
pwm_a.stop()
pwm_b.stop()
gpio.cleanup()