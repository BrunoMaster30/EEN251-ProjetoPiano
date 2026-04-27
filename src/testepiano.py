from machine import Pin, PWM
import time

# Configuração do buzzer
buzzer = PWM(Pin(17))

# Configuração dos botões (pull-down)
buttons = [
    Pin(2, Pin.IN, Pin.PULL_DOWN),
    Pin(3, Pin.IN, Pin.PULL_DOWN),
    Pin(4, Pin.IN, Pin.PULL_DOWN),
    Pin(5, Pin.IN, Pin.PULL_DOWN),
    Pin(6, Pin.IN, Pin.PULL_DOWN),
    Pin(7, Pin.IN, Pin.PULL_DOWN),
    Pin(8, Pin.IN, Pin.PULL_DOWN),
    Pin(9, Pin.IN, Pin.PULL_DOWN),
    Pin(10, Pin.IN, Pin.PULL_DOWN),
    Pin(11, Pin.IN, Pin.PULL_DOWN),
    Pin(12, Pin.IN, Pin.PULL_DOWN),
    Pin(13, Pin.IN, Pin.PULL_DOWN)
]

led = Pin(25, Pin.OUT)

# Frequências das notas
notes = [
    261, 277, 293, 311, 329, 349,
    369, 392, 415, 440, 466, 493
]

def ok():
    led.on()
    time.sleep(0.1)
    led.off()
    
def play_tone(freq):
    buzzer.freq(freq)
    buzzer.duty_u16(400)  # volume (0 a 65535)

def stop_tone():
    buzzer.duty_u16(0)

# Loop principal
ok()
while True:
    played = False
    
    for i in range(12):
        if buttons[i].value() == 1:
            ok()
            play_tone(notes[i])
            played = True
            break
    
    if not played:
        stop_tone()
    
    time.sleep(0.01)