import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # Set Pi to use GPIO pin numbers ; (GPIO.BOARD) would use the numbers assigned to each GPIO pin
                          
led = 18                         
trig = 4
echo = 17

#                             key : dict[key]
#                distance (in cm) : led frequency
#  the closer we get to the sensor, the brighter the led ( distance down = led frequency up)
dict = {
         1:100 , 2:100 , 3:100 , 4:100 , 5:100 , 6:99 , 7:99 , 8:99 , 9:99 , 10:98 ,
         11:98 , 12:97 , 13:97 , 14:96 , 15:96 , 16:95 , 17:95 , 18:94 , 19:94 , 20:93 ,
         21:93 , 22:92 , 23:92 , 24:91 , 25:91 , 26:90 , 27:90 , 28:89 , 29:88 , 30:87 ,
         31:87 , 32:86 , 33:86 , 34:85 , 35:85 , 36:84 , 37:84 , 38:83 , 39:83 , 40:82 ,
         41:82 , 42:81 , 43:81 , 44:80 , 45:80 , 46:79 , 47:79 , 48:78 , 49:78 , 50:77 ,
         51:77 , 52:76 , 53:76 , 54:75 , 55:75 , 56:74 , 57:74 , 58:73 , 59:73 , 60:72 ,
         61:72 , 62:71 , 63:71 , 64:70 , 65:70 , 66:69 , 67:69 , 68:68 , 69:68 , 70:67 ,
         71:67 , 72:66 , 73:66 , 74:65 , 75:65 , 76:64 , 77:64 , 78:63 , 79:63 , 80:62 ,
         81:62 , 82:61 , 83:61 , 84:60 , 85:60 , 86:59 , 87:59 , 88:58 , 89:58 , 90:57 ,
         91:57 , 92:56 , 93:55 , 94:54 , 95:54 , 96:53 , 97:53 , 98:52 , 99:52 , 100 :51,
         101:51, 102:50, 103:50, 104:49, 105:49, 106:48, 107:48, 108:47, 109:47, 110:46,
         111:46, 112:45, 113:45, 114:44, 115:44, 116:43, 117:43, 118:42, 119:42, 120:41,
         121:41, 122:40, 123:40, 124:39, 125:39, 126:38, 127:38, 128:37, 129:37, 130:36,
         131:36, 132:35, 133:35, 134:34, 135:34, 136:33, 137:33, 138:32, 139:32, 140:31,
         141:31, 142:30, 143:30, 144:29, 145:29, 146:28, 147:28, 148:27, 149:27, 150:26,
         151:26, 152:25, 153:25, 154:24, 155:24 , 156:23 , 157:23 , 158:22 , 159:22 , 160:21 ,
         161:21 , 162:20 , 163:20 , 164:19 , 165:19 , 166:18 , 167:18 , 168:17 , 169:17 , 170:16 ,
         170:16 , 171:15 , 172:15 , 173:14 , 174:14 , 175:13 , 176:13 , 177:12 , 178:12 , 179:11 , 180:11 ,
         181:10 , 182:10 , 183:9 , 184:9 , 185:8 , 186:8 , 187:7 , 188:7 , 189:6 , 190:6 ,
         191:5 , 192:5 , 193:4 , 194:4 , 195:3 , 196:3 , 197:2 , 198:2 , 199:1 , 200 : 0}

GPIO.setup(led, GPIO.OUT)  # led = our output
pwm = GPIO.PWM(led, 100)   # initialise (channel, frequency)



# main loop of program
x = 0                              # set x variable to 0 for 0%
print("Press Ctl + C to exit")
pwm.start(0)                      # Start PWM with 0% duty cycle

try:
  while True:
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)


    GPIO.output(trig, False)
    time.sleep(0.2)
    
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    while GPIO.input(echo)==0:
        pulse_start = time.time()
        
    while GPIO.input(echo)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 0)
    print("distance: ", distance, " cm")
    time.sleep(0.1)
    

    for key in dict:
        if distance == key:
            pwm.ChangeDutyCycle(dict[key])
            time.sleep(0.5)

    
        
except KeyboardInterrupt:
  print("Ctl + C pressed - ending program")



pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode



# this code is for a pulsing LED

    #for x in range(0, 101, 5):    # Loop 0 to 100 stepping dc by 5 each loop
     # pwm.ChangeDutyCycle(x)
      #time.sleep(0.05)             # wait .05 seconds at current LED brightness
      #print(dc)
    #for x in range(95, 0, -5):    # Loop 95 to 5 stepping dc down by 5 each loop
     # pwm.ChangeDutyCycle(x)
      #time.sleep(0.05)             # wait .05 seconds at current LED brightness
      #print(dc)