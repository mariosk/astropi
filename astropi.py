# 50th Elementary School of Patras
# 5th grade class - 10.Feb.2019
# Team: Odysseas Kroustalios, Evi Anagnostopoulou, George Karagiannopoulos 

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

b=(0,0,255)
bl=(0,0,0)
y=(255,255,0)
r=(255,0,0)
g=(0,255,0)
w=(255,255,255)
gr=(128,128,128)
p=(128,0,128)

sense.show_message("Hello from Patras, Greece", text_colour=b, back_colour=y, scroll_speed=0.04)

ody = [b,b,b,g,b,g,b,b,
       g,g,g,b,g,b,g,b,
       g,r,g,g,g,g,g,b,
       g,g,g,b,w,b,w,b,
       b,b,g,w,b,w,b,b,
       b,b,g,g,g,g,g,b,
       b,b,b,b,b,b,b,b,
       b,b,b,b,b,b,b,b]
       
evi = [w,w,g,g,g,w,w,w,
       w,w,w,w,g,w,w,w,
       w,w,w,w,g,w,w,w,
       w,w,r,r,r,r,r,w,
       w,r,r,bl,r,bl,r,r,
       w,r,r,r,r,r,r,r,
       w,w,r,bl,bl,bl,r,w,
       w,w,w,w,r,w,w,w]
       
george=[bl,bl,bl,bl,bl,bl,bl,bl,
        bl,bl,b,b,b,b,bl,bl,
        bl,b,b,b,b,b,b,bl,
        b,bl,bl,r,r,bl,bl,b,
        b,bl,g,bl,bl,g,bl,b,
        bl,b,g,g,g,g,b,bl,
        bl,bl,b,b,b,b,bl,bl,
        bl,bl,bl,b,b,bl,bl,bl]       

sense.show_message("Ody's drawing:", scroll_speed=0.02) 
sense.set_pixels(ody)
sleep(1)
sense.show_message("Evi's drawing:", scroll_speed=0.02)
sense.set_pixels(evi)
sleep(1)
sense.show_message("George's drawing:", scroll_speed=0.02)
sense.set_pixels(george)
sleep(1)

temperature_now=sense.get_temperature()
sense.show_message("The temperature now is: " + str(temperature_now), scroll_speed=0.02) 
sense.show_message("Goodbye now!", scroll_speed=0.02)
