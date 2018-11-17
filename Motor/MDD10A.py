# Code for cantrolling four motors using two MDD10A
import RPi.GPIO as io
import time
import curses

io.setmode(io.BCM)
io.setwarnings(False)

# PWM pin is used for Speed control
# DIR pin is used for Direction control
# Two motors connected to driver 1 and remaining two are connected to driver 2

# Driver 1
RightM1PWM=17
RightM1DIR=22
LeftM1PWM=18
LeftM1DIR=23

# Driver 2
RightM2PWM=6
RightM2DIR=19
LeftM2PWM=12
LeftM2DIR=16

screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

io.setup(RightM1PWM,io.OUT)
io.setup(RightM1DIR,io.OUT)
io.setup(LeftM1DIR,io.OUT)
io.setup(LeftM1PWM,io.OUT)

io.setup(RightM2DIR,io.OUT)
io.setup(RightM2PWM,io.OUT)
io.setup(LeftM2DIR,io.OUT)
io.setup(LeftM2PWM,io.OUT)

io.output(RightM1DIR,False)
io.output(RightM1PWM,False)
io.output(LeftM1PWM,False)
io.output(LeftM1DIR,False)

io.output(RightM2DIR,False)
io.output(RightM2PWM,False)
io.output(LeftM2PWM,False)
io.output(LeftM2DIR,False)

RightM1pwm=io.PWM(RightM1PWM,100)
RightM1pwm.start(0)
RightM1pwm.ChangeDutyCycle(0)

LeftM1pwm=io.PWM(LeftM1PWM,100)
LeftM1pwm.start(0)
LeftM1pwm.ChangeDutyCycle(0)

RightM2pwm=io.PWM(RightM2PWM,100)
RightM2pwm.start(0)
RightM2pwm.ChangeDutyCycle(0)

LeftM2pwm=io.PWM(LeftM2PWM,100)
LeftM2pwm.start(0)
LeftM2pwm.ChangeDutyCycle(0)

try:

	while  True:
		char=screen.getch()
		if char == ord('q'):                       # Quit the program 
			RightM1pwm.ChangeDutyCycle(0)
			LeftM1pwm.ChangeDutyCycle(0)
			RightM2pwm.ChangeDutyCycle(0)
			LeftM2pwm.ChangeDutyCycle(0)
			break
		elif char == curses.KEY_UP:                # Move Robot in Forward direction
			io.output(RightM1DIR,False)
			RightM1pwm.ChangeDutyCycle(100)
			io.output(LeftM1DIR,False)
			LeftM1pwm.ChangeDutyCycle(100)
			io.output(RightM2DIR,False)
			RightM2pwm.ChangeDutyCycle(100)
			io.output(LeftM2DIR,False)
			LeftM2pwm.ChangeDutyCycle(100)
		elif char == curses.KEY_DOWN:              # Move Robot in Reverse direction
			io.output(RightM1DIR,True)
			RightM1pwm.ChangeDutyCycle(100)
			io.output(LeftM1DIR,True)
			LeftM1pwm.ChangeDutyCycle(100)
			io.output(RightM2DIR,True)
			RightM2pwm.ChangeDutyCycle(100)
			io.output(LeftM2DIR,True)
			LeftM2pwm.ChangeDutyCycle(100)
		elif char == curses.KEY_LEFT:             # Left Turn
			io.output(RightM1DIR,False)
			RightM1pwm.ChangeDutyCycle(100)
			io.output(LeftM1DIR,False)
			LeftM1pwm.ChangeDutyCycle(0)
			io.output(RightM2DIR,False)
			RightM2pwm.ChangeDutyCycle(100)
			io.output(LeftM2DIR,False)
			LeftM2pwm.ChangeDutyCycle(0)
		elif char == curses.KEY_RIGHT:             # Right Turn
			io.output(RightM1DIR,False)
			RightM1pwm.ChangeDutyCycle(0)
			io.output(LeftM1DIR,False)
			LeftM1pwm.ChangeDutyCycle(100)
			io.output(RightM2DIR,False)
			RightM2pwm.ChangeDutyCycle(0)
			io.output(LeftM2DIR,False)
			LeftM2pwm.ChangeDutyCycle(100)
		elif char == ord('s'):                      # Stop all motors of Robot
			io.output(RightM1DIR,False)
			RightM1pwm.ChangeDutyCycle(0)
			io.output(LeftM1DIR,False)
			LeftM1pwm.ChangeDutyCycle(0)
			io.output(RightM2DIR,False)
			RightM2pwm.ChangeDutyCycle(0)
			io.output(LeftM2DIR,False)
			LeftM2pwm.ChangeDutyCycle(0)
		elif char == ord('r'):                       # Make robot do 360 degree rotation from same position
			io.output(RightM1DIR,False)
			RightM1pwm.ChangeDutyCycle(100)
			io.output(LeftM1DIR,True)
			LeftM1pwm.ChangeDutyCycle(100)
			io.output(RightM2DIR,False)
			RightM2pwm.ChangeDutyCycle(100)
			io.output(LeftM2DIR,True)
			LeftM2pwm.ChangeDutyCycle(100)

finally:
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
	GPIO.cleanup()
