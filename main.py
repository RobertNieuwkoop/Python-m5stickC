from m5stack import *
from machine import Timer
from random import randint, seed
from utime import ticks_cpu

# ! Important ! 
# Make sure to reset the device when re-uploading the code.
# Failing to do so will make timers overlap and make it appear as if duplicate code is being run.

playerPos = [0, 0]
# Initially clear the screen
lcd.clear()

# Initialise timer on ID #1
timer = Timer(1)
# Function to initialise the timer
def init(p):
  timer.init(period=p, callback=loop)

# Function that will be called each time the timer triggers
def loop(tmr=None):
  lcd.clear()
  lcd.print(playerPos[0], lcd.CENTER, lcd.CENTER)
  playerPos[0] += 20

  # Draw a rectangle on playerPos, 20 wide and 20 high. 
  # https://github.com/m5stack/M5Stack_MicroPython
  lcd.rect(playerPos[0], playerPos[1], 20, 20, 0xFFFFFF, 0xFFFFFF)

# The timer period, in milliseconds
period = 1000
# Start the process
init(period)
