from m5stack import *
from machine import Timer
import time

lcd.clear(lcd.BLACK)
playerPos = [0, 0]


while True:
    if btnA.wasPressed():
        lcd.text(lcd.CENTER, lcd.CENTER, 'user applll')
        playerPos = [0, 0]

    if btnB.wasReleased():
        lcd.text(lcd.CENTER, lcd.CENTER, 'user applll099')


    lcd.clear()
    lcd.print(playerPos[0], lcd.CENTER, lcd.CENTER)
    playerPos[0] += 20

    # Draw a rectangle on playerPos, 20 wide and 20 high. 
    # https://github.com/m5stack/M5Stack_MicroPython
    lcd.rect(playerPos[0], playerPos[1], 20, 20, 0xFFFFFF, 0xFFFFFF)
    time.sleep_ms(500) 