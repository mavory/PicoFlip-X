import machine, neopixel, time, ssd1306

NEOPIXEL_PIN = 25
LED_EXTERNAL_PIN = 16
SDA_PIN = 4
SCL_PIN = 5
OLED_WIDTH = 128
OLED_HEIGHT = 64
OLED_I2C_ADDR = 0x3C 

i2c = machine.I2C(0, sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN))

led_ext = machine.Pin(LED_EXTERNAL_PIN, machine.Pin.OUT)
try:
    # 8mA
    led_ext.init(machine.Pin.OUT, drive=2)
except:
    pass 

pixel = neopixel.NeoPixel(machine.Pin(NEOPIXEL_PIN), 1)

# OLED 
try:
    oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c, addr=OLED_I2C_ADDR)
except:
    oled = None

def init_mpu():
    try: i2c.writeto_mem(0x68, 0x6B, b'\x00')
    except: pass

def get_mpu_pos():
    def read_w(reg):
        try:
            h = i2c.readfrom_mem(0x68, reg, 1)[0]
            l = i2c.readfrom_mem(0x68, reg+1, 1)[0]
            v = (h << 8) | l
            return v - 65536 if v > 32767 else v
        except: return 0
    ax, ay, az = read_w(0x3B), read_w(0x3D), read_w(0x3F)
    limit = 8000
    if az < -8000: return "UPSIDE DOWN"
    if ay > limit: return "TILT FRONT"
    if ay < -limit: return "TILT BACK"
    if ax > limit: return "SIDE LEFT"
    if ax < -limit: return "SIDE RIGHT"
    return "LEVEL"

def get_sht():
    try:
        i2c.writeto(0x44, b'\xFD')
        time.sleep(0.01)
        d = i2c.readfrom(0x44, 6)
        return -45 + 175 * (d[0]<<8|d[1])/65535, -6 + 125 * (d[3]<<8|d[4])/65535
    except: return None, None

def hsv_to_rgb(h, s, v):
    i = int(h*6); f = h*6-i; p, q, t = v*(1-s), v*(1-s*f), v*(1-s*(1-f))
    i %= 6
    if i==0: return v,t,p
    if i==1: return v,q,p
    if i==2: return p,v,t
    if i==3: return p,v,q
    if i==4: return t,p,v
    return v,p,q

# maiiin
init_mpu()
hue = 0.0
last_blink = time.ticks_ms()
last_print = time.ticks_ms()

print("PicoFlip X: English firmware online.")

while True:
    now = time.ticks_ms()
    
    # NeoPixel 
    r, g, b = hsv_to_rgb(hue, 1.0, 0.1)
    pixel[0] = (int(r*255), int(g*255), int(b*255))
    pixel.write()
    hue = (hue + 0.002) % 1.0 
    
    # LED 
    if time.ticks_diff(now, last_blink) >= 1000:
        led_ext.value(not led_ext.value())
        last_blink = now
        
    # Data
    if time.ticks_diff(now, last_print) >= 500:
        temp, humi = get_sht()
        pos = get_mpu_pos()
        
        if oled:
            oled.fill(0)
            oled.text("--- PICOFLIP X ---", 0, 0)
            oled.text(f"Temp: {temp:.1f} C" if temp else "Temp: Error", 0, 20)
            oled.text(f"Humi: {humi:.1f} %" if humi else "Humi: Error", 0, 32)
            oled.text(f"Pos: {pos}", 0, 50)
            oled.show()
        
        # Serial monitor pro Thonny
        t_str = f"{temp:.1f}C" if temp else "Err"
        h_str = f"{humi:.1f}%" if humi else "Err"
        print(f"[{t_str} | {h_str}] Orientation: {pos}")
        
        last_print = now
    
    time.sleep(0.02)